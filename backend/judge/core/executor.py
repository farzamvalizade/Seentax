import io
import tarfile
import time


class CodeExecutor:
    def __init__(self, container, language_config, time_limit, memory_limit):
        self.container = container
        self.language_config = language_config
        self.time_limit = time_limit
        self.memory_limit = memory_limit

    def copy_code(self, code, file_name):
        tar_stream = io.BytesIO()
        with tarfile.open(fileobj=tar_stream, mode="w") as tar:
            data = code.encode()
            info = tarfile.TarInfo(name=file_name)
            info.size = len(data)
            tar.addfile(info, io.BytesIO(data))
        tar_stream.seek(0)
        self.container.put_archive("/app", tar_stream)

    def compile(self):
        if not self.language_config.get("need_compile"):
            return {"success": True}

        compile_cmd = self.language_config["compile_command"]
        exec_result = self.container.exec_run(
            compile_cmd, workdir="/app", user="1000:1000"
        )
        if exec_result.exit_code != 0:
            return {"success": False, "stderr": exec_result.output.decode()}
        return {"success": True}

    def run_test(self, input_data, expected_output):
        command = f"sh -c 'cat <<EOF | timeout {self.time_limit/1000}s {self.language_config['run_command']}\n{input_data}\nEOF'"
        start = time.time()
        exec_result = self.container.exec_run(
            command, workdir="/app", user="1000:1000"
        )
        elapsed = int((time.time() - start) * 1000)

        stdout = exec_result.output.decode("utf-8", errors="ignore").strip()
        verdict = "AC" if stdout == expected_output.strip() else "WA"

        if exec_result.exit_code == 124:
            verdict = "TLE"

        return {
            "verdict": verdict,
            "stdout": stdout,
            "stderr": "",
            "exit_code": exec_result.exit_code,
            "time_ms": elapsed,
            "memory_kb": 0,
        }
