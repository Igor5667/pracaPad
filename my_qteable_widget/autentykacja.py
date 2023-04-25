import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyBI1XpbIPQLsT2M76yynrukZDwkBbZ83mk",
  "authDomain": "python-3d870.firebaseapp.com",
  "databaseURL": "https://python-3d870-default-rtdb.firebaseio.com",
  "projectId": "python-3d870",
  "storageBucket": "python-3d870.appspot.com",
  "messagingSenderId": "389918346580",
  "appId": "1:389918346580:web:3fb0d7fb2251bdc1c5ccc1",
  "measurementId": "G-M9JMWPH26C"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

email = "kebs@super.pl"
password = "SuperKing"

auth.create_user_with_email_and_password(email, password)
auth.sing_in_email_and_password(email, password)
print("oki")