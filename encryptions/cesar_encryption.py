import string
from random import randint
punct_chars = string.punctuation


def encryption(message: str, cesar_key: int = 3) -> str:
    '''
    Cesar Cypher
    In encryption is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
    '''
    encode = temp = ""
    for ch in message:
        if ch.isspace() or ch.isdigit() or ch in punct_chars:
            temp = ch
        else:
            temp = chr((ord(ch.lower()) + cesar_key - ord("a")) % 26 + ord("a"))  # nopep8
        encode += temp.upper() if ch.isupper() else temp
    return encode


def decryption(encode_msg: str, cesar_key: int) -> str:
    decode = temp = ""
    for ch in encode_msg:
        if ch.isspace() or ch.isdigit() or ch in punct_chars:
            temp = ch
        elif ord(ch.lower()) - cesar_key < ord("a"):
            temp = chr(ord("z") + ord(ch.lower()) - ord("a") - cesar_key + 1)
        else:
            temp = chr(ord(ch.lower()) - cesar_key)
        decode += temp.upper() if ch.isupper() else temp
    return decode


if __name__ == "__main__":
    msg = "lets try to do a big message and see what is the output"
    key = randint(1, 10)
    # key = 25
    encode_msg = encryption(msg, key)
    decode_msg = decryption(encode_msg, key)
    print(f"""
    Message: {msg}
    Key:     {key}
    Encode:  {encode_msg}
    Decode:  {decode_msg}
        """)
    # d = {}
    # for ch in string.ascii_uppercase:
    #     d[ch] = ord(ch)
    # for k, v in d.items():
    #     print(k, v)
