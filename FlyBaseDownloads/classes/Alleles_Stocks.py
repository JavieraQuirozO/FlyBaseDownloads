#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 17:28:18 2023

@author: usuario
"""

from FlyBaseDownloads.Downloads import Downloads 

class Alleles_Stocks():
    
    def __init__(self, main_url):
    
        self.main_url = main_url
        self.gen_url = ''
        
    def get(self):
        
        url = self.main_url + self.gen_url + self.un_url
        downloads = Downloads(url)
        
        return downloads.get(self.header)
        
    def Stock(self):
        self.gen_url = 'stocks/'
        self.un_url = 'stocks_*.tsv.gz'
        self.header = 0
        return self.get()
        
    def Allele_genetic_interactions(self):
        self.gen_url = 'alleles/'
        self.un_url = 'allele_genetic_interactions_*.tsv.gz'
        self.header = 3
        return self.get()
            
    def Phenotypic(self):
        self.gen_url = 'alleles/'
        self.un_url = 'genotype_phenotype_data_*.tsv.gz'
        self.header = 4
        return self.get()
    
    def FBal_to_FBgn(self):
        self.gen_url = 'alleles/'
        self.un_url = 'fbal_to_fbgn_fb_*.tsv.gz'
        self.header = 1
        return self.get()