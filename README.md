# 06682_final_project

[![Run Tests](https://github.com/Han0928/openalex-works/actions/workflows/my-workflow.yaml/badge.svg)](https://github.com/Han0928/openalex-works/actions/workflows/my-workflow.yaml)


## Introduction
This package was created as the final project for course 06682. 
OpenAlex-Works is a Python package that provides an OpenAlexWorks class to retrieve RIS and BibTeX entries for a given Digital Object Identifier (DOI).

## Installation
The folder contains a package called:s23openalex, To install the package via pip, run: pip install openalex-works

## Usage
### Command Line Interface
After installing the package, you can use the command line interface (CLI) to get RIS or BibTeX entries for a DOI. 
To get an RIS entry, run: openalexworks get-ris <doi>
To get a BibTeX entry, run: openalexworks get-bibtex <doi>
Replace <doi> with the DOI for which you want to get the entry.

### OpenAlexWorks Class
You can also use the OpenAlexWorks class directly in your Python code. Here's an example:
from openalex.works import OpenAlexWorks

works = OpenAlexWorks('<your_api_key>')
ris_entry = works.get_ris('<doi>')
bibtex_entry = works.get_bibtex('<doi>')
Replace <your_api_key> with your OpenAlex API key, and <doi> with the DOI for which you want to get the entry.

### Testing
This package includes tests to ensure that it works correctly. 
### Code Quality
The code in this package has been formatted and checked for quality using black and pylint. To check your code, run: pylint openalex
### License
This package is licensed under the MIT License. See the LICENSE file for more information.






