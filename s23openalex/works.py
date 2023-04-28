"""
Module for interacting with the OpenAlex API.

This module provides a `Works` class that represents a work in the OpenAlex database.
The `Works` class has two properties: `ris` and `bibtex_entry`, which return the RIS
and BibTeX formatted citations for the work respectively.
"""

import requests
import bibtexparser


class Works:
    """
    A class that represents a work in the OpenAlex database.
    """

    def __init__(self, oaid):
        """
        Initializes a Works instance with the given OpenAlex ID.

        :param oaid: The OpenAlex ID of the work.
        """
        self.oaid = oaid
        try:
            self.req = requests.get(
                f"https://api.openalex.org/works/{oaid}", timeout=10
            )
            self.data = self.req.json()
        except requests.exceptions.RequestException as ex:
            raise ValueError("Failed to fetch data from API") from ex

    @property
    def ris(self):
        """
        Returns the RIS formatted citation for the work.

        :return: The RIS formatted citation string.
        """
        fields = []

        if self.data["type"] == "journal-article":
            fields += ["TY  - JOUR"]
        else:
            raise TypeError(f"Unsupported type {self.data['type']}")

        for author in self.data["authorships"]:
            fields += [f'AU  - {author["author"]["display_name"]}']

        fields += [
            f'PY  - {self.data["publication_year"]}',
            f'TI  - {self.data["title"]}',
            f'JO  - {self.data["host_venue"]["display_name"]}',
            f'VL  - {self.data["biblio"]["volume"]}',
        ]

        if self.data["biblio"]["issue"]:
            fields += [f'IS  - {self.data["biblio"]["issue"]}']

        fields += [
            f'SP  - {self.data["biblio"]["first_page"]}',
            f'EP  - {self.data["biblio"]["last_page"]}',
            f'DO  - {self.data["doi"]}',
            "ER  -",
        ]

        ris = "\n".join(fields)

        return ris

    @property
    def bibtex_entry(self):
        """
        Returns the BibTeX formatted citation for the work.

        :return: The BibTeX formatted citation string.
        """
        author_names = [au["author"]["display_name"] for au in self.data["authorships"]]
        author_string = " and ".join(author_names)

        bibtex_data = {
            "ENTRYTYPE": "article",
            "ID": self.data["id"],
            "author": author_string,
            "title": self.data["title"],
            "journal": self.data["host_venue"]["display_name"],
            "volume": self.data["biblio"]["volume"],
            "number": self.data["biblio"]["issue"],
            "pages": f"{self.data['biblio']['first_page']}-{self.data['biblio']['last_page']}",
            "year": str(self.data["publication_year"]),
            "doi": self.data["doi"],
        }

        bib_database = bibtexparser.bibdatabase.BibDatabase()
        bib_database.entries = [bibtex_data]
        writer = bibtexparser.bwriter.BibTexWriter()
        return writer.write(bib_database).strip()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Get RIS or BibTeX entry for an OpenAlex ID"
    )
    parser.add_argument("oaid", help="The OpenAlex ID of the work")
    parser.add_argument(
        "--format", help="The output format (ris or bibtex)", default="ris"
    )

    args = parser.parse_args()

    works = Works(args.oaid)

    if args.format == "ris":
        print(works.ris)
    elif args.format == "bibtex":
        print(works.bibtex_entry)
    else:
        print('Invalid format. Must be either "ris" or "bibtex"')
