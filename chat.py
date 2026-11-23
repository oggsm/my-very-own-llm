from tokenizer import encode, decode

prompt = input("> ")
token_ids = encode(prompt)

print(token_ids)
print(decode(token_ids))
