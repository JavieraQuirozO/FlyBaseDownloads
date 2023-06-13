# FlyBaseDownloads

Python package to facilitate the download of data from FlyBase. Most of the available data from their official wiki can be downloaded. One of the purposes of this library is to organize the data as closely as possible to the source, **FlyBase**. Despite not being the official package, it is organized by data class/type and provides direct downloads of the current bulk data files from the FTP site.


# Bulk data files

In order to simplify the download of FlyBase files, the names have been kept as close as possible. To access the data, follow these steps:

1. Install the library using the pip command.

> pip install FlyBaseDownloads

2. Import the library into your file.

> import FlyBaseDownloads as FBD

3. Access the different classes of the library described below.



## Synonyms

To download the file, execute the following command.
> Synonyms = FBD.Synonyms.get()

The file reports current symbols and synonyms for the following objects in FlyBase: genes (FBgn), alleles (FBal), balancers (FBba), aberrations (FBab), transgenic constructs (FBtp), insertions (FBti), transcripts (FBtr), and proteins (FBpp).

Columns Description

| Column heading           | Content Description          |
|----------------------|--------------------|
| primary_FBid   | Primary FlyBase identifier for the object |
| organism_abbreviation   | Abbreviation (from the Species Abbreviations list) indicating the species of origin |
| current_symbol   | Current symbol used in FlyBase for the object |
| current_fullname   | Current full name used in FlyBase for the object|
| fullname_synonym(s)   | 	Non-current full name(s) associated with the object (pipe separated values) |
| symbol_synonym(s)   | Non-current symbol(s) associated with the object (pipe separated values) |


## Genes
#### Genetic interaction table
#### RNA-Seq RPKM values
#### RNA-Seq RPKM values matrix
#### Single Cell RNA-Seq Gene Expression
#### Physical interaction MITAB file
#### Functional complementation table
#### FBgn to DB Accession IDs
#### FBgn to Annotation ID
#### FBgn to GLEANR IDs
#### FBgn to FBtr to FBpp IDs
#### FBgn to FBtr to FBpp IDs (expanded)
#### FBgn exons to Affy1 
#### FBgn exons to Affy2
#### Genes Sequence Ontology (SO) data
#### Genes map table
#### Best gene summaries
#### Gene Snapshots
#### Unique protein isoforms
#### Enzyme data
