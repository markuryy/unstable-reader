from setuptools import setup, find_packages

setup(
    name="unstable_reader",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "piexif",
        "Pillow",
    ],
    description="A package to extract metadata from images generated by stable diffusion tools",
    author="Markury",
    author_email="github@markury.dev",
)