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
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmubAUdLisMBENOoQmfQ8
4nt53P4hKlTp9d8dTJC9C9k3YPjPCsbRLiVAQCDIAK1h1I7qw6Iv8WYZDXdbxaP8
jA+fHcFzOXnWMfkt2/cdDi+NQFygNlnzmccjNcAMNeLElw2nLI568VugTgIRptq3
dVHd8BYNzZJzD39dWmkldh3+NvJ623zSlsLe68dq6D28bz87RfRQuWrx9qmEp+Kk
DEeRN+t5FwCajfhdQ/Lq64mHrPkI3hdRvfe0n0YD6D7vDNZMtucMi9Viko+Dh62I
TTVbY8heZkQDuErw9lAKB+GMulCFHscUnp94KikhNfTZkluYWC0J9or6NYyS1skv
EQIDAQAB
-----END PUBLIC KEY-----"""
        ),
        cannot_give_to={"Malik", "Ariana"},
    ),
    Participant(
        id="Eli",
        public_key=RSA.import_key(
            """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAgFFeRbinoCUZtUrug1lh
H5VfOGtUZVNXznR2W3ljylWE7Dj5MeCj7RgQYef+cDORyB+Tn6RB0Vsxvpp9BBZK
IL3Nw7MQCFwyehiE2C04rGV7eiPkzgFO572nxzUjuWmpAw5mpvczK2kujMFBII28
6MQCLcnCAilek4YdzqV8NCdS4nHNf3/JfEqOSlaU3TTppHSiN2dhxGiU9ZXBIpWT
knRBqIzdQmlhHKRkHjcasg//8Cj94ZZZThy9H54+b8+268TNV3hTVMGT6A33/mks
NbxamxrGEsIOvCWix0xshL7/g8IHCLdWItHkq4d/mN2qeiuOOb8A55jMxxY3/eY8
IQIDAQAB
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
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAl8o0v29n8Kiat/q7emN1
a58RoFJzxRqYvIhwBEVsnyIq4YlG1tkF4sYxaZUpaW+Zw3cXEunEZ4efQhFcCpRp
w1pwZEeMCjjy7ARm+1CR/jC/bW74HcX+WNxL83+HFLPVhkGZHokUqVCWUN4ApyJx
Cbq61iV1wEb2CmC7zinKiRtgAqkmkCV7qnrochAEhfaAmuBaM+ouAR9xE0EVk8eo
9af1MW3WeWYBORGCVHDrI3af8iJ7bYvJGSdtZgAfQoEIji9Q+ZC9b+gawZqLIug9
LfvGgSK5IR6eDT7SYNzx/LiU6/GoephskYvAm3bH8T6qOEbLg6yX6Fe0fA4gSZx8
AwIDAQAB
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
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyGx1Whf6kaDp46WiowrW
uPG36cOy1hZTQZVpsTdxZt96oLT4nE6+WbNNF/yglmW5a+uy5X0OmRL8YmrFMHvi
OTW9N3g3wvU/vc6B9b9td4RIRRKdg3ZnM9AzR5n788pv3VthJjem+jiPdGN2czxn
33lAXBfmmaln9EZ9d04hpbZpqNOo6mcAsWWeGnDQHtNz0QoFRlYyyitV3qpeSKca
XIhS+WAgmlRnpbSxm9+Knex32S3AtpbN1OlIxeX73zUW+6frH7rVoASBDzALlud5
kdv7JlhZZ+DKIYJpu+dQAl7jconajQZGXC/vV4Vp9hdsLNAHzRZiBkAZhbSk19xr
TwIDAQAB
-----END PUBLIC KEY-----"""
        ),
        cannot_give_to={"Abhinav", "Eli"},
    ),
]

DRY_RUN = len({x.public_key.export_key() for x in PARTICIPANTS}) != len(PARTICIPANTS)
