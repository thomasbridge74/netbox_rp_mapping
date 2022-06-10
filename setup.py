from setuptools import find_packages, setup

with open("README.md") as file:
    long_description = file.read()

setup(
    name="netbox-rp-mapping",
    version="0.1",
    description="Manage static RP Maps in NetBox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Framework :: Django",
        "Programming Language :: Python :: 3",
    ],
    zip_safe=False,
)
