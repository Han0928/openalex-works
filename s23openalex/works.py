import requests
import bibtexparser


class Works:
    def __init__(self, oaid):
        self.oaid = oaid
        self.req = requests.get(f'https://api.openalex.org/works/{oaid}')
        self.data = self.req.json()

    @property        
    def ris(self):
        fields = []
        if self.data['type'] == 'journal-article':
            fields += ['TY  - JOUR']
        else:
            raise Exception("Unsupported type {self.data['type']}")
        
        for author in self.data['authorships']:
            fields += [f'AU  - {author["author"]["display_name"]}']
            
        fields += [f'PY  - {self.data["publication_year"]}']
        fields += [f'TI  - {self.data["title"]}']
        fields += [f'JO  - {self.data["host_venue"]["display_name"]}']
        fields += [f'VL  - {self.data["biblio"]["volume"]}']
        
        if self.data['biblio']['issue']:
            fields += [f'IS  - {self.data["biblio"]["issue"]}']
        
        fields += [f'SP  - {self.data["biblio"]["first_page"]}']
        fields += [f'EP  - {self.data["biblio"]["last_page"]}']
        fields += [f'DO  - {self.data["doi"]}']
        fields += ['ER  -']
                
        ris = '\n'.join(fields)
        
        return ris

    @property
    def bibtex_entry(self):
        bibtex_data = {
            "ENTRYTYPE": "article",
            "ID": self.data["id"],
            "author": " and ".join([au["author"]["display_name"] for au in self.data["authorships"]]),
            "title": self.data["title"],
            "journal": self.data["host_venue"]["display_name"],
            "volume": self.data["biblio"]["volume"],
            "number": self.data["biblio"]["issue"],
            "pages": f"{self.data['biblio']['first_page']}-{self.data['biblio']['last_page']}",
            "year": str(self.data["publication_year"]),
            "doi": self.data["doi"]
        }
        
        db = bibtexparser.bibdatabase.BibDatabase()
        db.entries = [bibtex_data]
        writer = bibtexparser.bwriter.BibTexWriter()
        return writer.write(db).strip()


