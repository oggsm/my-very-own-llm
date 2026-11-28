# My Very Own LLM

Build a small language model from scratch and learn how it works by writing the code yourself. The project is for anyone comfortable running a terminal command and reading basic Python. You can learn the machine learning concepts as you go.

The goal is to build and train a model with around 20 million parameters on a home computer. We'll start with small examples you can run on a CPU and work toward a model that can generate short replies.

## Try the tokenizer

From the repository folder, run this command with Python 3. The demo uses only the Python standard library.

```sh
python3 chat.py
```

Type `hello` and press Enter.

```text
> hello
[104, 101, 108, 108, 111]
hello
```

Each number is a byte in the UTF-8 representation of the text. In this project, each byte is a token, one unit the model will read or predict. The demo converts the input to tokens and then decodes those tokens back into text. Try a Cyrillic letter or an emoji and see how many tokens it takes.

## What you'll build

1. **A tokenizer.** Convert text to token IDs and turn those IDs back into text. The first demo is ready in [`tokenizer.py`](tokenizer.py).
2. **Training examples.** Take a short window of tokens and pair it with the same window shifted one position to the right. For example, `hel` pairs with `ell` because the next characters after `h`, `he`, and `hel` are `e`, `l`, and `l`. This step is in progress in [`data.py`](data.py).
3. **A model.** Turn token IDs into vectors using embeddings. Use attention to combine information from earlier tokens and predict the next one.
4. **A training loop.** Compare the predictions with the correct next tokens, measure the errors, and update the model's weights.
5. **A text generator.** Give the trained model a prompt and extend it one token at a time. Try it on short dialogue prompts and see where its replies make sense.

The tokenizer demo is available now. The model, training loop, and text generator are planned.

## License

The code is licensed under the [GNU Affero General Public License v3](LICENSE).
