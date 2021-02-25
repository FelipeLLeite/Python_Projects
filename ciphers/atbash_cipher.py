import string
from random import randint
punct_chars = string.punctuation
alphabet = string.ascii_lowercase
reverse_alphabet = alphabet[::-1]


def encipher(msg: str) -> str:
    '''
    The Atbash cipher is a substitution cipher with a specific key where the letters of the alphabet are reversed. I.e. all 'A's are replaced with 'Z's, all 'B's are replaced with 'Y's, and so on. It was originally used for the Hebrew alphabet, but can be used for any alphabet.
    '''
    encode = temp = ""
    for ch in msg:
        if ch.isspace() or ch.isdigit() or ch in punct_chars:
            temp = ch
        else:
            temp = reverse_alphabet[ord(ch.lower()) - ord("a")]  # nopep8
        encode += temp.upper() if ch.isupper() else temp
    return encode


def decipher(encode_msg: str) -> str:
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
    encode_msg = encipher(msg)
    decode_msg = decipher(encode_msg)
    print(f"""
    Message: {msg}
    Encode:  {encode_msg}
    Decode:  {decode_msg}
    """)
    # print(reverse_alphabet)
