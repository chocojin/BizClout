from google.cloud import firestore
import youtubeCon.py


db = firestore.Client()

docs = db.collection(u'influencers').stream()

for doc in docs:
    descr=doc.to_dict()
    cat=youtubeCon.category(descr)
    doc_ref = db.collection(u'newinfluencers').document(doc.id)
    doc_ref.set({
      u'categories': cat
    })


