# ght

[![PyPI](https://img.shields.io/pypi/v/ght.svg)](https://pypi.org/project/ght/)
[![Changelog](https://img.shields.io/github/v/release/dominikb1888/ght?include_prereleases&label=changelog)](https://github.com/dominikb1888/ght/releases)
[![Tests](https://github.com/dominikb1888/ght/workflows/Test/badge.svg)](https://github.com/dominikb1888/ght/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/dominikb1888/ght/blob/master/LICENSE)

A set of github tools for managing groups

## Installation

Install this tool using `pip`:

    pip install ght

## Usage

For help, run:

    ght --help

You can also use:

    python -m ght --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd ght
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
