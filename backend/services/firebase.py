import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Firebase:
    def __init__(self):
        if not firebase_admin._apps:
            if os.path.exists("firebase.key.json"):
                cred = credentials.Certificate("firebase.key.json")
            else:
                firebase_credentials = {
                    "type": "service_account",
                    "project_id": os.getenv("project_id"),
                    "private_key": os.getenv("private_key"),
                    "client_email": os.getenv("client_email"),
                    "client_id": os.getenv("client_id"),
                    "auth_uri": os.getenv("auth_uri"),
                    "token_uri": os.getenv("token_uri"),
                    "auth_provider_x509_cert_url": os.getenv("auth_provider_x509_cert_url"),
                    "client_x509_cert_url": os.getenv("client_x509_cert_url"),
                    "universe_domain": "googleapis.com"
                }
            cred = credentials.Certificate(firebase_credentials)
            firebase_admin.initialize_app(cred)

        self.db = firestore.client()

    def get_db(self) -> firestore.client:
        return self.db
