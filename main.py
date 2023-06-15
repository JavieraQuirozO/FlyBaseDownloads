#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 18:22:34 2023

@author: usuario
"""

import FlyBaseDownloads as FBD

#%%
#Ejemplo

Sinonimos = FBD.Synonyms.get()

GO = FBD.GOAnn.get()

#%%

Ontology = FBD.Ontology_Terms

graph = Ontology.DO_ontology()

#%%

Genes = FBD.Genes

NonRNA = Genes.Noncoding_RNAs()

affy1 = Genes.FBgn_exons2affy1()

#%%
Organism = FBD.Organisms.Species_list()

#%%
Insertions = FBD.Insertions

Gal4 = Insertions.GAL4_drivers()
#%%
map_in = Insertions.Map_insertions()

#%%
Clones = FBD.Clones.genomic_clone_data()

#%%
References = FBD.References.FBrf_PMid_PMCid_doi()