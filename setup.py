from setuptools import setup, find_packages

setup(
    name="typeshit",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pynput",
        "langdetect",
    ],
    entry_points={
        "console_scripts": [
            "typeshit=typeshit.main:main",
        ],
    },
    author="Ebrahim Ramadan",
    author_email="ramadanebrahim791@gmail.com",
    description="wrong lang? you got typeshit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Ebrahim-Ramadan/wetype-tool",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)