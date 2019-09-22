from google.cloud import language_v1
from google.cloud.language_v1 import enums
 
description="I'm a makeup artist and medical student (aspiring dermatologist) based in California! Here on my channel, you will find makeup, lifestyle, fashion, and medicine; be sure to subscribe so you don’t miss out on anything!"


def categories(text_content):
    """
    Classifying Content in a String
 
    Args:
      text_content The text content to analyze. Must include at least 20 words.
    """
 
    client = language_v1.LanguageServiceClient()
 
    # text_content = 'That actor on TV makes movies in Hollywood and also stars in a variety of popular new TV shows.'
 
    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT
 
    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}
 
    response = client.classify_text(document)
    # Loop through classified categories returned from the API
    cat=''
    for category in response.categories:
        # Get the name of the category representing the document.
        # See the predefined taxonomy of categories:
        # https://cloud.google.com/natural-language/docs/categories
        flag=0
        if flag<1:
            cat=cat+category.name
            flag=1
        else:
            cat=cat+" & "+category.name
    return cat
   

 
data={}

categories=categories(text_content)

 

