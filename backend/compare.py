import math
from google.cloud import firestore


from google.cloud import language_v1
from google.cloud.language_v1 import enums
 
text_content="Marianne and Keith Bean have been involved with the food industry for several years. They opened their first restaurant in Antlers, Oklahoma in 1981, and their second in Hugo in 1988. Although praised for the quality of many of the items on their menu, they have attained a special notoriety for their desserts. After years of requests for their flavored whipped cream toppings, they have decided to pursue marketing these products separately from the restaurants. Marianne and Keith Bean have developed several recipes for flavored whipped cream topping. They include chocolate, raspberry, cinnamon almond, and strawberry. These flavored dessert toppings have been used in the setting of their two restaurants over the past 18 years, and have been produced in large quantities. The estimated shelf life of the product is 21 days at refrigeration temperatures and up to six months when frozen. The Beans intend to market this product in its frozen state in 8 and 12-ounce plastic tubs. They also intend to have the products available in six ounce pressurized cans. Special attention has been given to developing an attractive label that will stress the gourmet/specialty nature of the products."


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
   

 


bizCat=categories(text_content)

 



def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      

def comp(bizCat, influCat):
    bizCat=bizCat.replace(" & ","/")
    influCat=influCat.replace(" & ", "/")
    bizCat=bizCat.split("/");
    influCat=influCat.split("/");
    
    bizCat=Remove(bizCat)
    influCat=Remove(influCat)
    
    diffSet=set(bizCat)-set(influCat)

    return len(diffSet)




db = firestore.Client()
 
docs = db.collection(u'newinfluencers').stream()

valList=[]
influList=[]

for doc in docs:
    influCat=doc.to_dict().get('categories')
    val=comp(bizCat,influCat)
    valList.append(val)
    influList.append(doc.id)
    
   

valList, influList = (list(x) for x in zip(*sorted(zip(valList, influList))))
print (influList)