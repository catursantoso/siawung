import firebase_admin
from firebase_admin import credentials, firestore, storage

certfication = {
    "type": "service_account",
    "project_id": "web-desa-siawung",
    "private_key_id": "01f2154f1ee7a4ae98e88f67e74d4d041050ba5e",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCvdX8BD51WpHdY\nEWPapexoNmqWn4hvSXvaKB7puFuYwW/39aE16js59FDstxBPGxGGX6vrfcQdElTg\nQMjPsgw7UHuEcHYbiDEKJwtwRnG6R4Xm6GwrWyPR0WDcImWke28R6//voz5Sf4o9\nccJwcegLnkdRWITTw4CQZCG6h+uHXNnUPId72FbtuXcQSBTESu0vvbLNCOOial9q\nQDaivQqRpjeiLSUjmdXbFagnFvu3U9sV83VV+xBvAP4t6KuADbNN5M5lb1zVfqqg\nZO2QEXVpfd4278P17AmihT/KjyUEejdf8UbKjieEDFZjaI8ld3nYtLlyrMW6EM1w\nATS8jet5AgMBAAECggEABGSzxmoGrYm2t0zQLERlVAKwzo62EttLL547j+ye1odZ\nb2MGI1x3GS9l61d2IBT0bmHs4xumEnhICcl1fcXeiomsXheWzX+ugquRnMEWzexG\njQ6azscccX+Fpl1yIBk7Ib7ADNcQk25AHuO/U6N2hPv0mzPVN5w4luT69zm6Cwyc\nhl4CFC4Zt+ItkFwNxP0La7yy+JvmPtlBghMkvGSfcq3vQwM/lgb/i3PSC+A7CVTc\nKlJUBViWv8QwQtrt3yvkdfMI9NCD0UpW+TdIDqOIGLFYciBg1OLuTdea/m0Ywnne\n5ypWTFn0J5KshqTRp0hi7ZEzajVeLTsj25q0n3ZxFQKBgQDWvg0NhVjuNZ6n1IQi\nrSnuHbb2IYvYBEK7vvyhMX5fIv2pV31jeH67cpBGuW7984jlgkKGMk3quE33dU9w\n2VFfHU/E4U2aarqnMgAuSlvYkP67qrm+2GDk96Aa+0D/F60u1abnEo9sHjn7yeCc\n/g35UkbBHhuFJtOEIpn7FoifnwKBgQDRK1GSRRhOq1QmCv8M6oqL0ZQe50Hxct0r\npstV3ZxLwW+fxbFhD1MEz0UHnkknzDur6ln8wyv2Y7c76T3asbFPYN2X0FfzHsSY\no4z0A3j4EnXowM+wXWK1eST5b6lhbbdyJfGJQ5PyilpfYuBaWQPBberGWIBYCcB4\ndHjRaaM95wKBgF2t/ye82nTgs1vn29T80ePs1po9PDJ6eVpKEQ+I9eYu75Xmcu7n\n6/F+Iu6XipICod/tmXPNkiwpRuoDJSrHwzXJJblvyFjq4o55w5ZuHe82IcpgyjM1\nVd/NHu1mWo5uF8Dst6jqceLqtMTg5rnWIuZ3PCKXLc5Ch9eG+MGOrP9lAoGBAIjC\nzAjZCHWXa+Ob2Ps29vNISpKSHfmiYp3B5rzzsteNWFCcz8doX52Lb9T1V1ugG3vi\nNIghjEMDG7EeZYTyHb6K1RgH7xlVCrHKbcS16Ig6ecF/H8xuorWIyfYVXigHtqP5\nzx0yhC9W6pPncE1iWiREm/ansvLdHW0kqkIx0bwNAoGAY0v5P3FKinYoSp/uRpHz\nQBfIsiMeVSEXmXw5KHibBwEl9dodAyfGu/kjoTB68X/f19EsO2OV36U/sDLWk8Yz\nTIp5GeQziLPLjQhWp7BsUnVbiE1wJXX3sqP6+R4gCT2ECWjCsCZY4i9sgsubKsia\nxGNe6n5ENq56Su+8S0+QhB8=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-b3x7z@web-desa-siawung.iam.gserviceaccount.com",
    "client_id": "110259073771176570749",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-b3x7z%40web-desa-siawung.iam.gserviceaccount.com",
}


cred = credentials.Certificate(certfication)
firebase_admin.initialize_app(cred, {"storageBucket": "web-desa-siawung.appspot.com"})
DB = firestore.client()
Storage = storage.bucket()
