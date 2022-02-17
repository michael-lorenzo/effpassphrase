import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="effpassphrase",
    version="0.1.1",
    author="Michael Lorenzo",
    author_email="python@michael-lorenzo.com",
    description="Uses the EFF's long word list to generate a high entropy passphrase.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/michael-lorenzo/effpassphrase",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["effpassphrase=effpassphrase:create_passphrase"]},
    include_package_data=True,
    install_requires=["click"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
