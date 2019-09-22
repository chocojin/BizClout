from google.cloud import language_v1
from google.cloud.language_v1 import enums
from google.cloud import firestore


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
   
def locations(text_content):
    """
    Analyzing Entities in a String
 
    Args:
      text_content The text content to analyze
    """
 
    client = language_v1.LanguageServiceClient()
 
    # text_content = 'California is a state.'
 
    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT
 
    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
 
    language = "en"
 
 
    document = {"content": text_content, "type": type_, "language": language}
 
    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8
 
    response = client.analyze_entities(document, encoding_type=encoding_type)
    # Loop through entitites returned from the API
    locations=''
    for entity in response.entities:
        flag=0
        if flag<1:
            if "LOCATION" is (enums.Entity.Type(entity.type).name):
                locations=locations+entity.name
                flag=1
        else:
             if "LOCATION" is (enums.Entity.Type(entity.type).name):
                locations=locations+" & "+entity.name
    return locations


db = firestore.Client()
 
docs = db.collection(u'influencers').stream()


for doc in docs:
    descr=doc.to_dict().get('description')
    cat=categories(descr)
    doc_ref = db.collection(u'newinfluencers').document(doc.id)
    doc_ref.set({
      u'categories': cat
    })
