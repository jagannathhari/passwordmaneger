import base64

import bcrypt

SALT = b'8G\x18jW\xc9\xb1\xad\xd2.zI\x9a\xf7\xc8c~\xf3+\xfd\x19\xf4^Q\xaf\xae\xb8\xf2E\xb0e\x1d'
import pyaes
import pyscrypt
import binascii
import os
import secrets


def hash_paswd(paswd):
    password = paswd.encode("utf-8")
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed.decode("utf-8")


def validate_paswd(paswd, hashed):
    password = paswd.encode("utf-8")
    hash_ = hashed.encode("utf-8")
    if bcrypt.checkpw(password, hash_):
        return True
    else:
        False


def key_from_paswd(password):
    N = 2048
    r = 1
    p = 1
    key = pyscrypt.hash(password.encode('utf-8'), SALT, N, r, p, 32)
    print("calling key")
    return key


def encrypt_txt(data, password):
    iv = os.urandom(16)
    encrypter = pyaes.Encrypter(pyaes.AESModeOfOperationCBC(password, iv))
    ciphertext = encrypter.feed(data.encode('utf8'))
    ciphertext += encrypter.feed()
    return (base64.b64encode(ciphertext).decode('utf8'), base64.b64encode(iv).decode('utf-8'))


def decrypt_txt(data, iv, password):
    ciphertext = base64.decodebytes(data.encode('utf-8'))

    iv = base64.decodebytes(iv.encode('utf-8'))
    decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationCBC(password, iv))
    try:
        decryptedData = decrypter.feed(ciphertext)
        decryptedData += decrypter.feed()
        return decryptedData.decode("utf-8")
    except:
        return False


if __name__ == "__main__":
    #encrypter = pyaes.Encrypter(pyaes.AESModeOfOperationCBC(key, iv))
    a = encrypt_txt("aaaaaaaaaaaaaaaa", "jjj")
    print(len(key_from_paswd("sfjhdjsfh")))
    print(decrypt_txt(a[0], a[1], "jjj"))
