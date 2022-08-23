from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = [x.strip() for x in f.readlines()]

setup.setup(
    name="ELKLogging",
    version="0.0.1",
    author="YoungDo Park",
    author_email="pyd0309@gmail.com",
    description="Logging to Logstash/File/Stream",
    url="https://github.com/pyd0309/ELKLogger.git",
    packages=find_packages(),
    keywords=["logging", "ELK"],
    install_requires=requirements,
    python_requires=">=3.6",
)