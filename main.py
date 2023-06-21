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

GAF = FBD.GOAnn.GAF()

#%%

Genes = FBD.Genes

NonRNA = Genes.Noncoding_RNAs()

affy1 = Genes.FBgn_exons2affy1()

#%%
Gene_groups = FBD.Gene_groups
Gene_groups_data = Gene_groups.Gene_group() 
Gene_groups_data
Gene_groups_HGNC= Gene_groups.Gene_groups_HGNC() 
Gene_groups_HGNC
Pathway_group = Gene_groups.Pathway_group() 
Pathway_group


#%%

Organisms = FBD.Organisms
Species = Organisms.Species_list()

#%%

Ontology = FBD.Ontology_Terms

#%%
FBbt = Ontology.FBbt()
FBdv= Ontology.FBdv()
FBcv= Ontology.FBcv()
FBsv= Ontology.FBsv()
GO = Ontology.GO()
FBbi = Ontology.FBbi()
DO = Ontology.DO()

#%%
Insertions = FBD.Insertions

map_Insertions = Insertions.Map_insertions()

Gal4 = Insertions.GAL4_drivers()


#%%
Clones = FBD.Clones

c_cDNAs = Clones.cDNA_clone_data()
c_genomic = Clones.genomic_clone_data()

#%%
References = FBD.References.FBrf_PMid_PMCid_doi()




