# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 12:29:33 2018

@author: sosboy888
"""

import pythonGoogleSearcher
#calling googleSearch with default arguments
pythonGoogleSearcher.googleSearch("What is the capital of Australia?")
#calling googleSearch with a new window
pythonGoogleSearcher.googleSearch("What is the capital of Australia?",new=1)
#calling googleSearch with a new window and autoraise disabled
pythonGoogleSearcher.googleSearch("What is the capital of Australia?",new=1,autoraise=False)
