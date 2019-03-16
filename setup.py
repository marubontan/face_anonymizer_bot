from setuptools import setup

def parse_requirements(fname):
    with open(fname, 'r') as f:
        dependencies = f.read().split("\n")

    for dependency in dependencies:
        clean_dependency = dependency.strip()
        if clean_dependency:
            yield clean_dependency


setup(
    name="face_anonymizer_bot",
    version="1.0.0",
    install_requires=list(parse_requirements("requirements.txt")),
    entry_points = {
        "console_scripts": ["face_anonymize=face_anonymizer_bot.__main__:main"]
    }
)
