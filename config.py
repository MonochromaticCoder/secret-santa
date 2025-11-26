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
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmyACe2uCTWN3peknBCwC
r3YUjaAfarti4PHeLE4l/ytXhy8Jd7B/Px4xQClgxP9h/P6PaZ3ztfMivZzN8y/c
VdOZoVbHSlLh5cAnJICOKcE/BmZuQfzEEZzSw+xG5sHH3LaZzPkunBW/6Q0iLsba
5K0LKw1VZxBvgf+rrVN4h5ceSDrv/YaI04R8ihy8qr7SRoCS5S4T+w5yYjywmznD
eS/RAo5S/QOURiKvj9Wy/BG5t7enqhM1gOTwnLqwze2rIbnkD9G8ZqfN+ikpNjwU
tmU6oMnJDQkK6m1EGNi72YAUQ1cixUMvoNtJsS+kjbjKto3pe1C8RxxpTwxK6/qe
vQIDAQAB
-----END PUBLIC KEY-----"""
        ),
        cannot_give_to={"Xinru", "Xiao"},
    ),
    Participant(
        id="Ariana",
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
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmyACe2uCTWN3peknBCwC
r3YUjaAfarti4PHeLE4l/ytXhy8Jd7B/Px4xQClgxP9h/P6PaZ3ztfMivZzN8y/c
VdOZoVbHSlLh5cAnJICOKcE/BmZuQfzEEZzSw+xG5sHH3LaZzPkunBW/6Q0iLsba
5K0LKw1VZxBvgf+rrVN4h5ceSDrv/YaI04R8ihy8qr7SRoCS5S4T+w5yYjywmznD
eS/RAo5S/QOURiKvj9Wy/BG5t7enqhM1gOTwnLqwze2rIbnkD9G8ZqfN+ikpNjwU
tmU6oMnJDQkK6m1EGNi72YAUQ1cixUMvoNtJsS+kjbjKto3pe1C8RxxpTwxK6/qe
vQIDAQAB
-----END PUBLIC KEY-----"""
        ),
        cannot_give_to={"Xinru"},
    ),
    Participant(
        id="Xiao",
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
