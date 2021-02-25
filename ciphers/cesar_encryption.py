import string
from random import randint
punct_chars = string.punctuation


def encipher(message: str, cesar_key: int = 3) -> str:
    '''
    The Caesar cipher is one of the earliest known and simplest ciphers. It is a type of substitution cipher in which each letter in the plaintext is 'shifted' a certain number of places down the alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on. The method is named after Julius Caesar, who apparently used it to communicate with his generals.
    '''
    encode = temp = ""
    for ch in message:
        if ch.isspace() or ch.isdigit() or ch in punct_chars:
            temp = ch
        else:
            temp = chr((ord(ch.lower()) + cesar_key - ord("a")) % 26 + ord("a"))  # nopep8
        encode += temp.upper() if ch.isupper() else temp
    return encode


def decipher(encode_msg: str, cesar_key: int) -> str:
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
    encode_msg = encipher(msg, key)
    decode_msg = decipher(encode_msg, key)
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
