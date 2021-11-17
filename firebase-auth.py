import pyrebase

firebaseConfig = {
	'apiKey': "AIzaSyCMEEQ4rALIOf5lX0YuCvXXFABPk1ZvLjg",
    'authDomain': "databasedj-45b67.firebaseapp.com",
    'databaseURL': "https://databasedj-45b67-default-rtdb.firebaseio.com",
    'projectId': "databasedj-45b67",
    'storageBucket': "databasedj-45b67.appspot.com",
    'messagingSenderId': "606108675515",
    'appId': "1:606108675515:web:df26139a23b59f7f03e89e",}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
database = firebase.database()