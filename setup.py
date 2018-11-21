import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='s3manager',
    version='1.2',
    packages=setuptools.find_packages(),
    author="Anshul Gupta",
    author_email="anshulgupta217@gmail.com",
    description="This packages helps to upload and delete files to s3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anshul217/AWS-S3-MANAGER/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
