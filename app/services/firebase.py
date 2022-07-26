import firebase_admin
from firebase_admin import credentials, firestore, storage

certfication = {
    "type": "service_account",
    "project_id": "desa-siawung",
    "private_key_id": "609a914beee81db2d651fadd46485ea6b2568ffc",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCQwQL1ay29bFjU\nSvsmaWjwe3HgIdy6Rqf2OcZJOHPXGIPvFeRYA2LDNTX+7vEwGebNcwhcVRWesm90\nOz4qgDny0eA7H4F9Dt1TqmzaohHADeubvzq6RE7v19y7IgYvToUfOfQQl1dD6RfG\n1AkGmdEFdg5cRF7Rp8uSVpp8bQiz0eviB5ESgVgb9xth5DX/+EEZTi9epzybigEp\nzV/dsb5KT3a6PBAGrTDuXutmFLJadmtaoEgWSAtJRxGEA+mSz+RyS51cywiLMKzO\nFWLS4XtkZnrgeuCIJ49zgb1fB6/X2iS/3TFbJk6ErcgA+qyipeuimXetUBdnPItW\nSUWZkhuBAgMBAAECggEANZqUCufWt1fBCVR+7rmIN82u3M4NXBnAJyk76W9zTkrw\nyH+14HXYg+tXhIFdZW+iDaC0juSfLfZr2YH6wmhbjTT1MU+4duQjR9FLoCb2JcXB\n4xoMmF+lT6IDRnUSD0CngWnHnME+epJ90I5CjWQ2iCwwozBaYI8fjqBtcvg5icT7\nXyi2KQAYUW34uo68QSA25OuZOovtvThdgR3tJIQAkL7j/sVp3Lm6YNK5zHpodQDa\nAMsGCz98Qk0SQDBjA2KLz7UGu+q7RnqV6lACLnQU7Ff5SbuKoKCVM6nm5w2LH8dX\nxwcwMHSM3Hwvlp9ljxhyvsqKULSUo1rD3RJP/ckTNQKBgQDA4HqecAHyh/+wlskS\n3Q/Xf0qsYsSq3/p9Ov8Iy2gJfnopuOZeVg8g0Zsch5J7Z2JW8MnsUEq9LQa8mmQE\nwr02dZIEDBAHIgtcubN/N+WdeMVIaAPFnQbnTpHa13Mi5dPtii8NHnEWcHybqY/y\nfvZOlV4voqn52OPfTwkoeIPFLwKBgQDAILhna2aFLPKIFK/fR5yJko+y5LVdv5bJ\nQIffs18eY4PRHg3HWtzrg5cF/j8orwb3zJzUO9IKZvZe65nY8AoUoaFitOok+lNK\nDrquPGoSreFV5TNJE57sY9t9IMKM6Q2dY3NEuDOAaLy/1Owfc7IgLUDsd9DVP0gW\naTjzY09eTwKBgQC+Lxr5i1yAN5XqHGSckxoB1eRd4u4lx8EJJtk/ZMJrSilPZqDR\nOG6mX8hg81V/FUwkij2xJOLtcq6H3nztLNDCGGAoWXScc/dcMUhLE2T4R5PQd6/w\ndYvPHOw5K+S97n1wZqdKek/sXnKgUyw7YvGgPyymL/EHCdR350kSfPMBxQKBgQCc\nFvk6LGtyLv4ryILKJ+fpbQUKFf2zWIAsqRy6hYP1sGvbbUtMd2mcfaAo4lJ1vx0u\nHTIcyyzt/pCStV6cfQfzkw0GoGzJ9gXM2QKZo8OZwWKc4kU0TZiD/OzJT+A/kufY\nwn9XiT9uR6lxQI9FTj2dHqbsdrtXRL5QVtRKCJjmyQKBgQCx2fPtcgvKMliZeFrZ\nlO8WtbFspXFQS9CXi5Bz5w52vToY6US7+0yR0FlIK0Mu7JqZWOaEuYxWLWSB4lBM\nY/ew0MZksXAYouKBZw8H8Daov9marI+5c3OlnNTM2K1EE5no2DK5s++BpiUAC+U7\nQtsBBlD5kJFvOHW4vg5EMx7jng==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-r2dau@desa-siawung.iam.gserviceaccount.com",
    "client_id": "116685482899439557299",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-r2dau%40desa-siawung.iam.gserviceaccount.com",
}

cred = credentials.Certificate(certfication)
firebase_admin.initialize_app(cred, {"storageBucket": "gs://desa-siawung.appspot.com"})
DB = firestore.client()
Storage = storage.bucket()
