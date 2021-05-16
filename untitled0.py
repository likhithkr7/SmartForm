#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:32:15 2021

@author: likith
"""
# from translate import Translator
# translator= Translator(from_lang="english",to_lang="spanish")
# translation = translator.translate("Good")
# print(translation)

from googletrans import Translator
translator = Translator()
text = "He is good"
try:
    fl = 'en'
    dl = 'kn'
    text_to_translate = translator.translate(text,src = fl, dest = dl)
    text_to_translate = text_to_translate.text 
    print(text_to_translate)
except:
    print("error")

# from googletrans import Translator


# translator = Translator()  # initalize the Translator object
# translations = translator.translate(['see if this helps', 'tarun'], dest='hi')  # translate two phrases to Hindi
# for translation in translations:  # print every translation
#     print(translation.text)