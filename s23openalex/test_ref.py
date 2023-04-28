"""
Test module for the Works class in the s23openalex package.
"""

from s23openalex.works import Works

REF_RIS = """TY  - JOUR
AU  - John R. Kitchin
PY  - 2015
TI  - Examples of Effective Data Sharing in Scientific Publishing
JO  - ACS Catalysis
VL  - 5
IS  - 6
SP  - 3894
EP  - 3899
DO  - https://doi.org/10.1021/acscatal.5b00538
ER  -"""

REF_BIBTEX = """@article{https://openalex.org/W2288114809,
 author = {John R. Kitchin},
 doi = {https://doi.org/10.1021/acscatal.5b00538},
 journal = {ACS Catalysis},
 number = {6},
 pages = {3894-3899},
 title = {Examples of Effective Data Sharing in Scientific Publishing},
 volume = {5},
 year = {2015}
}"""


def test_ris_works():
    """Test that the RIS output of Works is correct."""
    works = Works("https://doi.org/10.1021/acscatal.5b00538")
    assert REF_RIS == works.ris


def test_bibtex_works():
    """Test that the BibTeX output of Works is correct."""
    works = Works("https://doi.org/10.1021/acscatal.5b00538")
    assert REF_BIBTEX == works.bibtex_entry
