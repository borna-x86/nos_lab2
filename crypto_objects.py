from enum import Enum
import pickle
from Crypto.PublicKey import RSA


class Method(Enum):
    RSA = 0
    AES = 1


class EncryptionMode(Enum):
    ECB = 0
    CBC = 1
    CTR = 2


class CryptoObject:
    def __init__(self):
        self.method = None
        self.description = None

    @staticmethod
    def from_file(filename):
        data = None
        with open(filename, "rb") as f:
            data = pickle.load(f)

        return data

    def to_file(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)


class AESCryptedFile(CryptoObject):
    def __init__(self, filename, encryption_mode, cyphertext, init_vec=None):
        super().__init__()

        self.method = "AES"
        self.description = "Encrypted File"

        self.filename = filename
        self.cyphertext = cyphertext
        self.encryption_mode = encryption_mode
        self.init_vec = init_vec


class AESKey(CryptoObject):
    def __init__(self, key):
        super().__init__()

        self.method = "AES"
        self.description = "Secret Key"

        self.key = key


class RSAPublicKey(CryptoObject):
    def __init__(self, key_len, modulus, public_exponent):
        super().__init__()

        self.method = Method.RSA
        self.description = "Public Key"

        self.key_len = key_len
        self.modulus = modulus
        self.public_exponent = public_exponent

    def as_crypto_key(self):
        return RSA.construct((self.modulus, self.public_exponent), consistency_check=True)

    @staticmethod
    def from_crypto_key(key_size, key):
        return RSAPublicKey(key_size, key.n, key.e)


class RSAPrivateKey(CryptoObject):
    def __init__(self, key_len, modulus, private_exponent, public_exponent):
        super().__init__()

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
