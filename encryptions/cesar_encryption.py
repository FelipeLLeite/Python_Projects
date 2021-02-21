import string
upper_chars = string.ascii_uppercase
lower_chars = string.ascii_lowercase


def encryption(message: str, cesar_key: int = 3) -> str:
    '''
    Cesar Cypher
    In encryption is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
    '''
    result = ""
    for ch in message:
        if ch.isspace():
            result += " "
        elif (ch.isupper()):
            # Encrypt uppercase characters in plain text
            result += chr((ord(ch) + cesar_key - 65) % 26 + 65)
        else:
            # Encrypt lowercase characters in plain text
            result += chr((ord(ch) + cesar_key - 97) % 26 + 97)
    return result


def decryption(encode_msg: str, cesar_key: int) -> str:
    decode = ""
    for ch in encode_msg:
        pass
    return ""


if __name__ == "__main__":
    msg = "Felipe Lopes Leite"
    key = 10
    print(encryption(msg, key))
