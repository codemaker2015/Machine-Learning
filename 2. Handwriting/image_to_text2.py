# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 12:49:43 2018

@author: Codemaker
"""

import pytesseract
from PIL import Image
print( pytesseract.image_to_string(Image.open('test.png')))