#!/usr/bin/python3
""" function that prints a text """


def text_indentation(text):
    """ print texte """
    punctuation = [".", "?", ":"]
    value = False
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in text:
        if i in punctuation:
            print(i)
            print()
            value = True
        else:
            if value is False:
                print(i, end="")
            else:
                if i != " ":
                    print(i, end="")
                    value = False
