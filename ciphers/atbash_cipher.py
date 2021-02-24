import string
from random import randint
punct_chars = string.punctuation
alphabet = string.ascii_lowercase
reverse_alphabet = alphabet[::-1]


def encryption(msg: str) -> str:
    encode = temp = ""
    for ch in msg:
        if ch.isspace() or ch.isdigit() or ch in punct_chars:
            temp = ch
        else:
            temp = reverse_alphabet[ord(ch.lower()) - ord("a")]  # nopep8
        encode += temp.upper() if ch.isupper() else temp
    return encode


def decryption(encode_msg: str) -> str:
    decode = temp = ""
    for ch in encode_msg:
        if ch.isspace() or ch.isdigit() or ch in punct_chars:
            temp = ch
        else:
            temp = alphabet[abs(ord(ch.lower()) - ord("z"))]  # nopep8
        decode += temp.upper() if ch.isupper() else temp
    return decode


if __name__ == "__main__":
    msg = "string.ascii_letters"
    key = randint(1, 10)
    # key = 25
    encode_msg = encryption(msg)
    decode_msg = decryption(encode_msg)
    print(f"""
    Message: {msg}
    Key:     {key}
    Encode:  {encode_msg}
    Decode:  {decode_msg}
        """)
    # print(reverse_alphabet)
