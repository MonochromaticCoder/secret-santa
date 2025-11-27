from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RsaKey
from dataclasses import dataclass


@dataclass
class Participant:
    id: str
    public_key: RsaKey
    cannot_give_to: set[str]


PARTICIPANTS = [
    Participant(
        id="Abhinav",
        public_key=RSA.import_key(
            """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuIufx04d9Ip/BCEivtVD
HPMRB2vBbXpkphkQcyYkZ9BcZxrOFzdFfssYaj6a+0bQyx7KsxI3qOCfZFmVGyjt
zD2ZExAXUwstKMMVnifqPBD5CUaH51t3Ofxvhj46pTVaTDc3m+6JEjNoWI7bXZF0
UJHGutfgoyc65p9rVdnLq10iNizw/dUWUqoVDKb3ivM32xzMRKmM9FSdXd2bIVWI
vB/k/KepcIeVxk3pUM84HapJi/xYks1bZKIirDQdKp+0w0VTilId6f4mMEzk+NQG
+QR77KREuB2ny5IsMTPEckwnqXIvq5fIdlBTOMG0Pfjq+YlR7wueMqH/EEP6doKh
pwIDAQAB
-----END PUBLIC KEY-----"""
        ),
        cannot_give_to={"Xinru", "Xiao"},
    ),
    Participant(
        id="Ariana",
        public_key=RSA.import_key(
            """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAp5XR3PBy8iZkpAbpf3eu
Py+34KQVCpvVb545kaAJ5AgOGReWz3WysyhaohjwMBuoUZ+mVQtbt+fl18DSGPaQ
y0R8xyHXusZtEfytVREKNnYvcLVATIPS3YoIIY2Fmaf1qaCgYPMhaQ5Tahkw9I6S
SqiGv0lUFiLEsKrwPpSlztrPNRiHht3oLPFrBBp3HkSgimFapf+SeGdWPZAaim4k
WA+ZKHPvuSHd8j/IoW+fBn0Q/aqvnYHQsar+1lz4VYNSuhVxUgUoYbx9QHUxHFa2
o/EI6hDMhI0Yw+Z7mUfx+d8JaOIqelizNQRoW/VNqVhHoG9/miFIlIspwCnvIdiw
OwIDAQAB
-----END PUBLIC KEY-----"""
        ),
        cannot_give_to={"Xiao", "Abhinav"},
    ),
    Participant(
        id="Chaoyi",
        public_key=RSA.import_key(
            """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmyACe2uCTWN3peknBCwC
r3YUjaAfarti4PHeLE4l/ytXhy8Jd7B/Px4xQClgxP9h/P6PaZ3ztfMivZzN8y/c
VdOZoVbHSlLh5cAnJICOKcE/BmZuQfzEEZzSw+xG5sHH3LaZzPkunBW/6Q0iLsba
5K0LKw1VZxBvgf+rrVN4h5ceSDrv/YaI04R8ihy8qr7SRoCS5S4T+w5yYjywmznD
eS/RAo5S/QOURiKvj9Wy/BG5t7enqhM1gOTwnLqwze2rIbnkD9G8ZqfN+ikpNjwU
tmU6oMnJDQkK6m1EGNi72YAUQ1cixUMvoNtJsS+kjbjKto3pe1C8RxxpTwxK6/qe
vQIDAQAB
-----END PUBLIC KEY-----"""
        ),
        cannot_give_to={"Malik", "Ariana"},
    ),
    Participant(
        id="Eli",
        public_key=RSA.import_key(
            """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmyACe2uCTWN3peknBCwC
r3YUjaAfarti4PHeLE4l/ytXhy8Jd7B/Px4xQClgxP9h/P6PaZ3ztfMivZzN8y/c
VdOZoVbHSlLh5cAnJICOKcE/BmZuQfzEEZzSw+xG5sHH3LaZzPkunBW/6Q0iLsba
5K0LKw1VZxBvgf+rrVN4h5ceSDrv/YaI04R8ihy8qr7SRoCS5S4T+w5yYjywmznD
eS/RAo5S/QOURiKvj9Wy/BG5t7enqhM1gOTwnLqwze2rIbnkD9G8ZqfN+ikpNjwU
tmU6oMnJDQkK6m1EGNi72YAUQ1cixUMvoNtJsS+kjbjKto3pe1C8RxxpTwxK6/qe
vQIDAQAB
-----END PUBLIC KEY-----"""
        ),
        cannot_give_to={"Seray", "Malik"},
    ),
    Participant(
        id="Malik",
        public_key=RSA.import_key(
            """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmyACe2uCTWN3peknBCwC
r3YUjaAfarti4PHeLE4l/ytXhy8Jd7B/Px4xQClgxP9h/P6PaZ3ztfMivZzN8y/c
VdOZoVbHSlLh5cAnJICOKcE/BmZuQfzEEZzSw+xG5sHH3LaZzPkunBW/6Q0iLsba
5K0LKw1VZxBvgf+rrVN4h5ceSDrv/YaI04R8ihy8qr7SRoCS5S4T+w5yYjywmznD
eS/RAo5S/QOURiKvj9Wy/BG5t7enqhM1gOTwnLqwze2rIbnkD9G8ZqfN+ikpNjwU
tmU6oMnJDQkK6m1EGNi72YAUQ1cixUMvoNtJsS+kjbjKto3pe1C8RxxpTwxK6/qe
vQIDAQAB
-----END PUBLIC KEY-----"""
        ),
        cannot_give_to={"Chaoyi", "Syed"},
    ),
    Participant(
        id="Seray",
        public_key=RSA.import_key(
            """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmyACe2uCTWN3peknBCwC
r3YUjaAfarti4PHeLE4l/ytXhy8Jd7B/Px4xQClgxP9h/P6PaZ3ztfMivZzN8y/c
VdOZoVbHSlLh5cAnJICOKcE/BmZuQfzEEZzSw+xG5sHH3LaZzPkunBW/6Q0iLsba
5K0LKw1VZxBvgf+rrVN4h5ceSDrv/YaI04R8ihy8qr7SRoCS5S4T+w5yYjywmznD
eS/RAo5S/QOURiKvj9Wy/BG5t7enqhM1gOTwnLqwze2rIbnkD9G8ZqfN+ikpNjwU
tmU6oMnJDQkK6m1EGNi72YAUQ1cixUMvoNtJsS+kjbjKto3pe1C8RxxpTwxK6/qe
vQIDAQAB
-----END PUBLIC KEY-----"""
        ),
        cannot_give_to={"Eli", "Chaoyi"},
    ),
    Participant(
        id="Syed",
        public_key=RSA.import_key(
            """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtYYw5BxsLz9VEegDtnuH
19DFh9Ml8OFJZBHLBJEEs/dt19pMtwWJEVGqRcQZdZgI2AbqDxJs1o3vIZT9mmfl
V41FzAO6vGmAkSmGPTlHZrU/B2uPwo2TMb4sgjMVdDh2Eyov6cHDNN8u2dDqtcFN
7YEHVaXF8n4qmtQlP9GX3P2KtNqQbZiE7cATe2vxpGCr10vdaq6PT6N89z37thXw
BUjaZusSMX9HxZ4SiL2nHx8FAyYmDYnlR68JrjqzxJZZIt7+6TMPNXUkbI27sSYT
KKTSnhKaeYhcop0nwkulY+MkRzqVtRu0yPwbeBFZuygAEOVvxniJVCmwnLgkO6In
KQIDAQAB
-----END PUBLIC KEY-----"""
        ),
        cannot_give_to={"Xinru"},
    ),
    Participant(
        id="Xiao",
        public_key=RSA.import_key(
            """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0B1EjJyNJ+mQdfYroik2
yovmNh5GMfk5fjCof8vJ87VVoD8McoaJuYtmtNX6JYR0QLOjwBvnSgYO4LU5O92F
biABl8lwwj+iXXrXRMrKXmdSrv0uZtgMMAp8s8jCw1IaZxh22Pky2oDB3FPzhSpE
5vKAmPxWFjcMxWhaVbnrVXUabQhWV16povImispYBA7vXUjPgitj+p7mesnuBLia
0+4tg1WgsveIw8ZMgS+mzO2I3PMeuzF2DZyfPhHI6M5uxCkKWcUTunG0SMDRjsnT
5ercfkNQV0U2iW8+OToXFm3piHvejKWX3b/FoYxT/KWJIiWA2Washq/v9do6KJ+4
RQIDAQAB
-----END PUBLIC KEY-----"""
        ),
        cannot_give_to={"Ariana", "Seray"},
    ),
    Participant(
        id="Xinru",
        public_key=RSA.import_key(
            """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmyACe2uCTWN3peknBCwC
r3YUjaAfarti4PHeLE4l/ytXhy8Jd7B/Px4xQClgxP9h/P6PaZ3ztfMivZzN8y/c
VdOZoVbHSlLh5cAnJICOKcE/BmZuQfzEEZzSw+xG5sHH3LaZzPkunBW/6Q0iLsba
5K0LKw1VZxBvgf+rrVN4h5ceSDrv/YaI04R8ihy8qr7SRoCS5S4T+w5yYjywmznD
eS/RAo5S/QOURiKvj9Wy/BG5t7enqhM1gOTwnLqwze2rIbnkD9G8ZqfN+ikpNjwU
tmU6oMnJDQkK6m1EGNi72YAUQ1cixUMvoNtJsS+kjbjKto3pe1C8RxxpTwxK6/qe
vQIDAQAB
-----END PUBLIC KEY-----"""
        ),
        cannot_give_to={"Abhinav", "Eli"},
    ),
]

DRY_RUN = len({x.public_key.export_key() for x in PARTICIPANTS}) != len(PARTICIPANTS)
