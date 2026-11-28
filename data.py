import random
from pathlib import Path

from tokenizer import encode

DATA_PATH = Path(__file__).parent / "data" / "omer_seyfettin.txt"


def load_text(path=DATA_PATH):
    with open(path, encoding="utf-8") as file:
        return file.read()


def split_token_ids(token_ids, train_fraction=0.9):
    # The first part is for training. The last part is kept for testing.
    split_at = int(len(token_ids) * train_fraction)
    return token_ids[:split_at], token_ids[split_at:]


def get_example(token_ids, start, context_size):
    end = start + context_size
    inputs = token_ids[start:end]
    targets = token_ids[start + 1:end + 1]
    return inputs, targets


def get_batch(token_ids, batch_size, context_size):
    last_start = len(token_ids) - context_size - 1
    if last_start < 0:
        raise ValueError("the text must be longer than context_size tokens")

    batch_inputs = []
    batch_targets = []
    for _ in range(batch_size):
        start = random.randint(0, last_start)
        inputs, targets = get_example(token_ids, start, context_size)
        batch_inputs.append(inputs)
        batch_targets.append(targets)

    return batch_inputs, batch_targets


def make_examples(text, context_size):
    # Builds every example at once, so use it only for short texts.
    token_ids = encode(text)
    examples = []

    for start in range(len(token_ids) - context_size):
        examples.append(get_example(token_ids, start, context_size))

    return examples


if __name__ == "__main__":
    random.seed(0)

    token_ids = encode(load_text())
    train_ids, test_ids = split_token_ids(token_ids)
    print("tokens:", len(token_ids))
    print("train tokens:", len(train_ids))
    print("test tokens:", len(test_ids))

    # The model only sees numbers. We decode them here so that we can read them.
    inputs, targets = get_batch(train_ids, batch_size=4, context_size=16)
    for x, y in zip(inputs, targets):
        x_text = bytes(x).decode("utf-8", errors="replace")
        y_text = bytes(y).decode("utf-8", errors="replace")
        print(repr(x_text), "->", repr(y_text))
