# easy_string

## Basic structure 


packaging_tutorial <br>
├── LICENSE <br>
├── pyproject.toml <br>
├── README.md <br>
├── src/<br>
│-- - - -   └── example_package_YOUR_USERNAME_HERE/<br>
│-- - - -        ├── __init__.py<br>
│-- - - -        └── example.py<br>
└── tests/

## Configuring metadata (toml file)
### Example using hatchling

```
[project]
name = "example_package_YOUR_USERNAME_HERE"
version = "0.0.1"
authors = [
  { name="Example Author", email="author@example.com" },
]
description = "A small example package"
readme = "README.md"
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
]
license = "MIT"
license-files = ["LICEN[CS]E*"]

[project.urls]
Homepage = "https://github.com/pypa/sampleproject"
Issues = "https://github.com/pypa/sampleproject/issues"
```

## Install build

``
python -m pip install --upgrade build
``

## Build

``
py -m build
``

Will generate dist folder

## Generate API token

https://test.pypi.org/

## Install twine
#### To upload the distributions packages generated with the build
``
python -m pip install --upgrade twine
``

## Upload all the files from the dist folder
``
python -m twine upload --repository testpypi dist/*
``
* Enter the API token when prompted

obs: if uploading to real PyPi, remove the testpypi and --repository. Should be something like this: ``python -m twine upload dist/*``



## Link for the package online will display

OBS: If we have another version, the version from the projet toml needs to change, otherwise ther will be an error for package with the same version/name

## Installing packages from PiPy Test

``
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps easy_string
``

OBS: if in real PiPy, install the package like any other package: `` python -m pip install [package name] ``

## Use thepackage
Import it <br>
``
from easy_string import easy_string
`` <br>
Use it normally
``
easy_string.word_count("hello my heelo my world")
``


