# Retry with a clean import and install bibtexparser if missing
!pip install bibtexparser

from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import homogenize_latex_encoding, convert_to_unicode
from bibtexparser.load import loads
import pandas as pd

# Load the .bib file content
bib_file_path = "/mnt/data/2598_AWS_MASTER.bib"
with open(bib_file_path, "r", encoding="utf-8") as file:
    bib_content = file.read()

# Parse the BibTeX entries
parser = BibTexParser(common_strings=True)
parser.customization = lambda record: convert_to_unicode(homogenize_latex_encoding(record))
bib_database = loads(bib_content, parser=parser)

# Extract and analyze fields
entries_data = []
for entry in bib_database.entries:
    entry_type = entry.get("ENTRYTYPE", "unknown").lower()
    cite_key = entry.get("ID", "unknown")
    fields = list(entry.keys())
    entries_data.append({
        "cite_key": cite_key,
        "entry_type": entry_type,
        "num_fields": len(fields),
        "has_doi": "doi" in entry,
        "has_author": "author" in entry,
        "has_title": "title" in entry,
        "has_year": "year" in entry,
        "has_journal/booktitle": "journal" in entry or "booktitle" in entry,
    })

df = pd.DataFrame(entries_data)
df_summary = df.groupby("entry_type").agg({
    "cite_key": "count",
    "has_doi": "sum",
    "has_author": "sum",
    "has_title": "sum",
    "has_year": "sum",
    "has_journal/booktitle": "sum"
}).rename(columns={"cite_key": "count"}).sort_values(by="count", ascending=False)

import caas_jupyter_tools as cj
cj.display_dataframe_to_user(name="BibTeX Entry Type Summary", dataframe=df_summary)

# Also return the first few entries that are missing critical fields
df_incomplete = df[
    ~df["has_author"] | ~df["has_title"] | ~df["has_year"]
].sort_values(by="entry_type")
df_incomplete.head(10)
