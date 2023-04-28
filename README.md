# 06682_final_project

[![Run Tests](https://github.com/Han0928/openalex-works/actions/workflows/my-workflow.yaml/badge.svg)](https://github.com/Han0928/openalex-works/actions/workflows/my-workflow.yaml)


## Introduction
This package was created as the final project for course 06682. 
OpenAlex-Works is a Python package that provides an OpenAlexWorks class to retrieve RIS and BibTeX entries for a given OpenAlex ID.

## Installation
The folder contains a package called:s23openalex, To install the package via pip, run: pip install openalex-works

## Usage
### Command Line Interface
After installing the package, you can use the command line interface (CLI) to get RIS or BibTeX entries for a given OpenAlex ID. 
python -m pkg2.s23openalex.works <OpenAlex ID> [--format FORMAT]

Replace <OpenAlex ID> with the OpenAlex ID of the work you want to retrieve the citation for, and FORMAT with either ris or bibtex. If FORMAT is not specified, it defaults to ris.

### Testing
This package includes tests to ensure that it works correctly: pkg2/s23openalex/test_ref.py. 
### Code Quality
The code in this package has been formatted and checked for quality using black and pylint.
To check your code, run: 
  pylint openalex
  
### License
This package is licensed under the MIT License. See the LICENSE file for more information.






