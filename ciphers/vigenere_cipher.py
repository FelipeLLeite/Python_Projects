# string library to
import string
from random import randint

# Global variables
punct_chars = string.punctuation
alphabet = string.ascii_lowercase


def print_dict(d: dict, key: str = None) -> None:
    if key:
        for ch in key:
            print(d[ch.lower()])
    else:
        for k, v in d.items():
            print(k, v)


def generate_random_key() -> str:
    size = randint(1, 15)
    res = ""
    for _ in range(size):
        res += alphabet[randint(0, len(alphabet)-1)]
    return res


def build_table() -> dict:
    d = dict()

    def _build_char_list(ch: str) -> list:
        result = []
        cnt = 0
        new_cnt = ord("a")
        while len(result) != len(string.ascii_lowercase):
            if ord(ch) + cnt <= 122:
                result.append(chr(ord(ch) + cnt))
                cnt += 1
            else:
                result.append(chr(new_cnt))
                new_cnt += 1
        return result

    letters = string.ascii_lowercase
    for character in letters:
        d[character] = _build_char_list(character)
    return d


def encryption(msg: str, key: str) -> str:
    idx = 0
    encode = ""
    for ch in msg:
        idx = 0 if idx == len(key) else idx
        cesar_key = ord(key[idx].lower()) - ord("a")
        if ch.isspace() or ch.isdigit() or ch in punct_chars:
            temp = ch
        else:
            temp = chr((ord(ch.lower()) + cesar_key - ord("a")) % 26 + ord("a"))  # nopep8
        encode += temp.upper() if ch.isupper() else temp
        idx += 1
    return "".join(encode)


def decryption(encode_msg: str, key: str) -> str:
    decode = ""
    idx = 0
    for ch in encode_msg:
        idx = 0 if idx == len(key) else idx
        cesar_key = ord(key[idx].lower()) - ord("a")
        if ch.isspace() or ch.isdigit() or ch in punct_chars:
            temp = ch
        elif ord(ch.lower()) - cesar_key < ord("a"):
            temp = chr(ord("z") + ord(ch.lower()) - ord("a") - cesar_key + 1)
        else:
            temp = chr(ord(ch.lower()) - cesar_key)
        decode += temp.upper() if ch.isupper() else temp
        idx += 1
    return decode


if __name__ == "__main__":
    d = build_table()
    msg = "Lets try another message"
    key = generate_random_key()
    # key = "ejipzja"

    encode_msg = encryption(msg, key)
    decode_msg = decryption(encode_msg, key)

    print(f"""
Message: {msg}
Key:     {key}
Encode:  {encode_msg}
Decode:  {decode_msg}
    """)


# Erros
# Message: Felipe ama a Barbara (20)
# Key:     ejipzja              (7)
# Encode:  Jntxon aqj i Qzabeai (20)
# Decode:  Jjkpzo rqf z Ikbsewz (20)

# Message: Felipe ama a Barbara
# Key:     nvshgsz
# Encode:  Szdpvw zzv s Igjanms
# Decode:  Tmixoq hai x Qzdiozx
