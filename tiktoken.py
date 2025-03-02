import tiktoken
enc = tiktoken.encoding_for_model("gpt-40")

tokens = enc.encode("Hello, world!")
print(tokens)
print(enc.decode(tokens))