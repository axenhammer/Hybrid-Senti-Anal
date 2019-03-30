import csv, re, sys
#from spellchecker import SpellChecker
import re, operator, sys
import re, os, shutil, sys
from textblob import TextBlob
import acronym_resolution
import key_phrases
import polarity_textblob
def main():
  String = input('Enter text')
  text = acronym_resolution.translator(String) #op
  keyphrases = key_phrases.main(text) #op
  output = polarity_textblob.main(String)
  actual_output = str(output) #op

  print(actual_output)
main()
