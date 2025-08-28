import os

from docker import DockerClient
from judge.models import ProgrammingLanguage


def build_image(language: ProgrammingLanguage):
    client = DockerClient.from_env()
    dockerfile_dir = os.path.dirname(language.dockerfile_path.path)
    image_tag = f"judge-{language.name.lower().replace(' ', '_')}:latest"

    print(f"[+] Building image for {language.name} from {dockerfile_dir}...")
    client.images.build(
        path=dockerfile_dir,
        dockerfile="Dockerfile",
        tag=image_tag,
        rm=True
    )
    return image_tag
