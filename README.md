python-paddingoracle: A python 3 portable, padding oracle exploit API
=====================================================================

python-paddingoracle is an API that provides pentesters a customizable
alternative to `PadBuster`_ and other padding oracle exploit tools that can't
easily (without a heavy rewrite) be used in unique, per-app scenarios. Think
non-HTTP applications, raw sockets, client applications, unique encodings, etc.

## Usage:

To use the paddingoracle API, simply implement the **oracle()** method from the
PaddingOracle API and raise a **BadPaddingException** when the decrypter
reveals a padding oracle. To decrypt data, pass raw encrypted bytes to
**decrypt()** with a block size (typically 8 or 16) and optional iv parameter.

See `example.py` for an example. 

python-paddingoracle is a Python implementation heavily based on `PadBuster`,
an automated script for performing Padding Oracle attacks, developed by
Brian Holyfield of Gotham Digital Science.

`PadBuster`: https://github.com/GDSSecurity/PadBuster
