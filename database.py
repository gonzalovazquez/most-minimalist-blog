import pyrebase

config = {
  "apiKey": " AIzaSyB6SKFYNWI9gpduiT2Qnvb-jP08rMF8yjs",
  "authDomain": "minimalist-blog.firebaseapp.com",
  "databaseURL": "https://minimalist-blog-c74d1.firebaseio.com/",
  "storageBucket": "minimalist-blog.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def create_entry(name, body, date):
    db.child("posts").push({
        "name": name,
        "body": body,
        "date": date
    })
    print("Saving to database")

def retrieve_entries():
    posts = db.child("posts").get()
    print(posts.val())
    return posts.val()