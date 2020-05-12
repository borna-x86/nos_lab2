from Crypto.Cipher import AES
from Crypto.Util import Padding
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP

import crypto_objects as co


# Todo: needs to take a key crypto_object not a bytes key?
def symmetric_encrypt(data_file, cypher, key, key_size, encryption_mode):
    """
    Creates crypto_objects from parameters the user enters in the GUI.

    :param data_file: string, path to file to encrypt
    :param cypher: one of {"AES", "3-DES"}
    :param key: key to encrypt with. If None, a random key will be chosen.
    :param key_size: for AES, one of {128, 192, 256}, for 3-DES one of {192, 128}
    :param encryption_mode: one of {"ECB", "CBC", "CTR"}

    :return: (key,
    """
    if encryption_mode not in ("ECB", "CBC", "CTR"):
        raise ValueError("encryption mode invalid")

    if cypher not in ("AES", "3-DES"):
        raise ValueError("cypher not supported")

    if key is not None and len(key) != key_size:
        raise ValueError("key_size and len(key) differ")

    if key is None:
        key = Random.get_random_bytes(key_size//8)

    plaintext = b""
    with open(data_file, "rb") as f:
        plaintext = f.read()

    block_size_bytes = 8 if cypher is "3-DES" else 16
    plaintext = Padding.pad(plaintext, block_size_bytes)

    # AES Cypher
    if cypher is "AES":
        if key_size not in (128, 192, 256):
            raise ValueError("AES key size not supported")

        # ECB mode
        if encryption_mode is "ECB":
            cypher = AES.new(key, AES.MODE_ECB)
            cyphertext = cypher.encrypt(plaintext)
            return co.AESKey(key), co.AESCryptedFile(data_file, encryption_mode, cyphertext)


def symmetric_decrypt(crypted_file, key):
    """
    Decrypts crypted_file (AESCryptedFile) object into a file crypted_file.filename using
    key (AESKey).

    :param crypted_file: AESCryptedFile - file to decrypt
    :param key: AESKey - decryption key

    :return created filename
    """

    if crypted_file.method == "AES" and crypted_file.encryption_mode == "ECB":
        decypher = AES.new(key.key, AES.MODE_ECB)

        with open(crypted_file.filename, "wb") as plaintext_file:
            plaintext_file.write(Padding.unpad(decypher.decrypt(crypted_file.cyphertext), 16))

        return crypted_file.filename

    else:
        raise NotImplemented("cypher-mode pair not supported")


def asymmetric_encrypt(plaintext, rsa_key):
    return PKCS1_OAEP.new(rsa_key).encrypt(plaintext)


def assymetric_decrypt(cyphertext, rsa_key):
    return PKCS1_OAEP.new(rsa_key).decrypt(cyphertext)


if __name__ == '__main__':
    # Symmetric encryption/decryption example
    #aes_key, aes_crypted_file = symmetric_encrypt('plaintext.txt', "AES", None, 192, "ECB")
    #aes_crypted_file.filename = "plaintext.txt"
    #import os
    #print(os.remove("plaintext.txt"))

    #print(symmetric_decrypt(aes_crypted_file, aes_key))

    # Digital envelope test


    pass
