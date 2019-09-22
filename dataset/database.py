from google.cloud import firestore

# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client()

doc_ref = db.collection(u'influencers').document(u'kaurBeauty')
doc_ref.set({
    u'description': u'I\'m a makeup artist and medical student (aspiring \
    dermatologist) based in Northern California! Here on my channel, you will \
    find makeup, lifestyle, fashion, and medicine; be sure to subscribe so you \
    on’t miss out on anything! Xoxo'
})
doc_ref = db.collection(u'influencers').document(u'Food Wishes')
doc_ref.set({
    u'description': u'Hello this is Chef John, and welcome to the Food Wishes \
    channel, where the food is the star. Watch these fun-to-make, and \
    easy-to-follow recipes, and you\'ll improve your culinary skills dramatically! \
    I post new videos on Tuesdays and Fridays (usually), so keep checking back! \
    Even better, join the community of astonishingly amazing people who subscribe \
    to my channel, so you don’t miss a thing. For more, find all my recipes on \
    Allrecipes.com and foodwishes.com, where I share the story, ingredients, \
    and details that go along with these recipes. Not to mention lots of other \
    fabulous fun for foodies!'
})
doc_ref = db.collection(u'influencers').document(u'PatrickStarrr ')
doc_ref.set({
    u'description': u'Hey YouTube! This is my Makeup, Beauty and Lifestyle \
    channel! "MAKEUP IS A ONE SIZE FITS ALL".I love makeup, photography and \
    YouTube! I want boys in BEAUTY! I am a professional makeup and I want to \
    share everything I know about makeup and beauty! I myself am always learning\
    as well! In the makeup industry there is no degree of success and you will\
    always learn something new- whether it is new trends or techniques! I \
    absolutely love working with people and I especially enjoy doing others \
    makeup here on my channel! If you see me, say HELLO! "Life Opens Up When \
    You Do"'
})
doc_ref = db.collection(u'influencers').document(u'Cooking With Sros')
doc_ref.set({
    u'description': u'Hi my beloved visitors and subscribers. My name is Sros. I \
    am here to serve all of you with food cooking recipe such as modern recipe, \
    popular recipes, family scale recipes, seafood recipe, rustic recipe, and \
    other yummy recipe in my location. Actually, I am not a professional chef, \
    yet I would like to try to share homemade food to the world and the other \
    food visitors to know about my food style and process which I discovered and \
    learned since I was a child with my mom, relative and neighbors.'
})
doc_ref = db.collection(u'influencers').document(u'Dave Beaulieu')
doc_ref.set({
    u'description': u'Cooking new and interesting food is my passion.  But it\'s \
    not always about the recipe.  Of course I use recipes, but more importantly, \
    I focus on the cooking techniques that make great food. I\'m not a chef.  I\'m \
    a dad.  I\'m a husband...and I have a day job.  Over the years, I\'ve taught \
    myself, with cooking shows, books, magazines, and of course Youtube, how to \
    cook.   And I\'ve found that rather than focus on the very specific steps in \
    a very specific recipe, if I focused on how the cook was putting ingredients \
    together, how they figured out when things were cooked enough, etc, I could \
    translate those techniques to new and different recipes - So that truly, No \
    Recipe was Required.'
})
doc_ref = db.collection(u'influencers').document(u'James Charles')
doc_ref.set({
    u'description': u'Hey YouTube! This is my Makeup, Beauty and Lifestyle \
    channel! "MAKEUP IS A ONE SIZE FITS ALL".I love makeup, photography and \
    YouTube! I want boys in BEAUTY! I am a professional makeup and I want to \
    share everything I know about makeup and beauty! I myself am always learning\
    as well! In the makeup industry there is no degree of success and you will\
    always learn something new- whether it is new trends or techniques! I \
    absolutely love working with people and I especially enjoy doing others \
    makeup here on my channel! If you see me, say HELLO! "Life Opens Up When \
    You Do"'
})
doc_ref = db.collection(u'influencers').document(u'Kylie Jenner')
doc_ref.set({
    u'description': u'Exclusive videos from Kylie Jenner. I enjoy making beauty\
    and lifestyle videos. I believe that everyone can be beautiful Behind-the-scenes \
    content, makeup videos, beauty tutorials and more.'
})
doc_ref = db.collection(u'influencers').document(u'Kendall Jenner')
doc_ref.set({
    u'description': u'Exclusive clips from Kendall Jenner’s Official App!\
    The Kendall Jenner Official App gives Kendall\'s audience unprecedented and\
    exclusive personal access to her life. Through the app, Kendall shares \
    original and curated content from fashion, makeup, and beauty to travel and \
    lifestyle, interactive experiences, live streaming, access to offline \
    events, and much more. Kendall is giving her fans more access, content and \
    experiences here, than she has ever offered before. Features include, \
    personal diaries from Kendall, live streaming video and behind-the-scenes \
    content, how to get Kendall’s style (shopping tips, fashion and beauty \
    advice, and where to buy), special access to events and giveaways,\
    Kendall\'s favorite products, exclusive personal photographs and video, \
    and more.'
})
doc_ref = db.collection(u'influencers').document(u'Marlena Stell')
doc_ref.set({
    u'description': u'My purpose for this channel is to inspire ALL women of \
    all ages, sizes, skin color, and ethnicities to feel their best on the \
    inside and out. My sole calling in life is to build others up and to help \
    them feel beautiful. "Beauty begins the moment you decide to be yourself" \
    -Coco Chanel Thank you for allowing me to follow my passion and for all \
    the support for Makeup Geek!'
})
doc_ref = db.collection(u'influencers').document(u'Glen & Friends Cooking')
doc_ref.set({
    u'description': u'New name but we\'re still all about food, cooking and \
    recipes. Glen And  Friends Cooking gives you easy to follow video instructions \
    about food, cooking and recipes. Each week we will upload 5 new recipe, food, \
    and cooking videos where the recipes are tested, tested, and tested again. \
    You can trust us when we say that these great  recipes work..'
})
doc_ref = db.collection(u'influencers').document(u'KathleenLights')
doc_ref.set({
    u'description': u'Hey! I\'m Kathleen. An oddball Aquarius with a love for all\
    things makeup and beauty! I keep it simple on this channel with reviews and tutorials \
    and sometimes I do fun challenges, but for the most part, I stay pretty old school. \
    I upload on Mondays, Wednesdays and Fridays unless otherwise noted (usually \
    on Twitter so be sure to follow me there). If I am doing a sponsored video, \
    it will be on one of my off days so you get bonus content :) I absolutely \
    love getting ideas from you guys so please always tell me what kind of \
    videos you want to see in the comments and don\'t forget to subscribe and \
    click the notification bell to stay up to date with my content.'
})
doc_ref = db.collection(u'influencers').document(u'Bailey Sarian')
doc_ref.set({
    u'description': u'Hi my name is Bailey Sarian and I am here to talk about \
    True Crime & Makeup. YES its an odd combination, but I couldn\'t just pick \
    ONE topic to focus on, why not mix them both together?'
})
doc_ref = db.collection(u'influencers').document(u'SAM THE COOKING GUY')
doc_ref.set({
    u'description': u'I\'m Sam, and this is my Youtube channel - welcome to my \
    world of cooking! If you love food that’s big in taste, small in effort, \
    and served with a healthy dose of irreverence… well, you’ve definitely come \
    to the right place. Watch my videos for easy to make recipes…kitchen \
    basics…and live Q&A episodes where I answer all of your cooking questions. \
    My goal is to show you that cooking doesn’t have to be hard, it just has to \
    be delicious.'
})
