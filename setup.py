from setuptools import find_packages, setup


try:
    with open("requirements.txt", "r") as f:
        install_requires = [x.strip() for x in f.readlines()]
except IOError:
    install_requires = []


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="guestbook",
    version="0.2.0",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/tompakarlsson/guestbook",
    author="Tomas Karlsson",
    author_email="tompa.karlsson@gmail.com",
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)