#!/usr/bin/python3
# Polarity Detection of Normalised Text
# Created by Team Axenhammer, https://github.com/Axenhammer
# Licensed as MIT

import re, os, shutil, sys
from textblob import TextBlob

def main(Input_String):
    num = 0
    # For Splitting Paragraphs into List of Sentences
    output = []
    products = Input_String.split(".")
    postive = 0
    negative = 0
    #print("Polarity ranges from (-1 -> 1)")
    for product in products:
        arr = []
        product = product.strip()
        if (product != ""):
            blob = TextBlob(product)
            Polarity = float(blob.sentiment.polarity)
            arr.append(Polarity)
            #print("\"" + product + "\" -> ", Polarity)
            if (Polarity > 0):
                if (Polarity < 0.5):
                #    print("Emotion: Mildly Positive")
                    emo = "Emotion: Mildly Positive"
                else:
                #    print("Emotion: Strongly Positive")
                    emo = "Emotion: Strongly Positive"

            elif (Polarity < 0):
                Polarity = (-1)*Polarity
                if (Polarity < 0.5):
                #    print("Emotion: Mildly Negative")
                    emo = "Emotion: Mildly Negative"
                else:
                #    print("Emotion: Strongly Negative")
                    emo = "Emotion: Strongly Negative"

            else:
                #print("Emotion: Impassive")
                emo = "Emotion: Impassive"
            arr.append(emo)
            output.append(arr)
            num += 1
            
    return output

if __name__ == '__main__':
    Input_String = sys.argv[1]
    main(Input_String)
