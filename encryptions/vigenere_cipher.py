# string library to
import string
from random import randint

# Global variables
punct = string.punctuation
alphabet = string.ascii_lowercase


def print_dict(d: dict, key: str = None) -> None:
    if key:
        for ch in key:
            print(d[ch.lower()])
    else:
        for k, v in d.items():
            print(k, v)


def generate_random_key() -> str:
    size = randint(1, 10)
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
        temp = key[idx].lower()
        if ch.isupper():
            encode += d[key[idx].lower()][ord(ch.lower()) - ord("a")].upper()
            idx += 1
        elif ch.isspace() or ch.isdigit() or ch in punct:
            encode += ch
        else:
            encode += d[key[idx].lower()][ord(ch.lower()) - ord("a")]
            idx += 1
        idx = 0 if idx == len(key) else idx
    return "".join(encode)


def decryption(encode: str, key: str) -> str:
    decode = ""

    idx = len(encode) % len(key) if len(key) < len(encode) else 0
    for ch in encode:
        temp = key[idx].lower()
        if ch.isupper():
            decode += alphabet[d[key[idx].lower()].index(ch.lower())].upper()
            idx += 1
        elif ch.isspace() or ch.isdigit() or ch in punct:
            decode += ch
        else:
            decode += alphabet[d[key[idx].lower()].index(ch.lower())]
            idx += 1
        idx = 0 if idx == len(key) else idx

    return "".join(decode)


if __name__ == "__main__":
    d = build_table()
    msg = "Felipe ama a Barbara"
    key = generate_random_key()
    key = "ejipzja"
    
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
