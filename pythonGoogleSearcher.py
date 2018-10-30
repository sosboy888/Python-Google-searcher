# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 11:35:52 2018

@author: sosboy888
"""

import webbrowser

def googleSearch(searchTerm,new=2,autoraise=True):
    webbrowser.open("https://www.google.com/?#q="+searchTerm,new=2,autoraise=True)
googleSearch("hello world")