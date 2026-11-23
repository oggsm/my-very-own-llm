def encode(text):
    token_ids = list(text.encode("utf-8"))
    return token_ids

def decode(token_ids):
    text = bytes(token_ids).decode("utf-8")
    return text
