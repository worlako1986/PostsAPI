from hashlib import sha256


def hash_password(password: str):
    return sha256(str(password).encode('utf-8')).hexdigest()