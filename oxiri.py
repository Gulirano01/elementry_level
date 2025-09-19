# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 14:38:53 2025

@author: User
"""

class Gullar:
    def __init__(self,tur,rang,narx):
        self.tur=tur
        self.rang=rang
        self.narx=narx
        
    def info(self):
        inf=f"{self.tur},rangi:{self.rang},narxi:{self.narx}"
        return inf
        
lola=Gullar("piyozdoshlar","oq","40000")        
        