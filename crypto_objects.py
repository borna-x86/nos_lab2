from enum import Enum

from Crypto.PublicKey import RSA

class Method(Enum):
    RSA = 0

class CryptoObject:
    def __init__(self):
        self.method = None
        self.description = None


class RSAPublicKey:
    def __init__(self, key_len, modulus, public_exponent):
        self.method = Method.RSA
        self.description = "Public Key"

        self.key_len = key_len
        self.modulus = modulus
        self.public_exponent = public_exponent

    @staticmethod
    def from_crypto_key(key_size, key):
        return RSAPublicKey(key_size, key.n, key.e)

class RSAPrivateKey:
    def __init__(self, key_len, modulus, private_exponent, public_exponent):
        self.method = Method.RSA
        self.description = "Private Key"

        self.key_len = key_len
        self.modulus = modulus
        self.private_exponent = private_exponent
        self.public_exponent = public_exponent

    def as_crypto_key(self):
        return RSA.construct((self.modulus, self.public_exponent, self.private_exponent), consistency_check=True)

    @staticmethod
    def from_crypto_key(key_size, key):
        return RSAPrivateKey(key_size, key.n, key.d, key.e)