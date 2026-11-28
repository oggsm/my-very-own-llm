from tokenizer import encode


def make_examples(text, context_size):
    token_ids = encode(text)
    examples = []

    for start in range(len(token_ids) - context_size):
        end = start + context_size
        inputs = token_ids[start:end]
        targets = token_ids[start + 1:end + 1]
        examples.append((inputs, targets))

    return examples


if __name__ == "__main__":
    for inputs, targets in make_examples("hello", 3):
        print(inputs, "->", targets)














