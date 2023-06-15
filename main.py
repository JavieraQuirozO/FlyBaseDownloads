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

GO = FBD.Gene_Ontology_annotation.get()

#%%

Ontology = FBD.Ontology_Terms

graph = Ontology.DO_ontology()

