import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="myproto",
    version="0.0.1",
    author="pliesveld",
    author_email="author@example.com",
    description="A sample library demonstrating protobuf",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pliesveld/tutorial-protobuf",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
