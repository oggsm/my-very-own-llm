# Steps

This file records every step of the project: what we built, why we built it that way, and how you can try it. Follow the steps in order to build your own small language model.

## Step 1: A byte tokenizer (`tokenizer.py`)

**What:** `encode` turns text into its UTF-8 bytes. Each byte is one token, so every token ID is a number from 0 to 255. `decode` turns the bytes back into text.

**Why:** A model can only compute with numbers. UTF-8 can write every character of every language, so 256 token IDs are enough for any text and no character is ever "unknown". The cost is length: a letter such as `ş` takes two tokens. Our dataset has 668,290 characters and 739,322 tokens, which is 10.6% longer.

**Try:** `python3 chat.py`, then type a word.

## Step 2: A small, free dataset (`data/`)

**What:** `data/omer_seyfettin.txt` holds 71 stories by Ömer Seyfettin from Turkish Wikisource.

**Why:** A model knows only the text it reads. We publish the data together with the code, so the text must be legal to share. The author died in 1920, so his works are in the public domain in Turkey. `data/SOURCE.md` explains the licence and lists the exact pages that were downloaded.

## Step 3: Training examples (`data.py`)

**What:** A window of `context_size` tokens is the input. The same window moved one token to the right is the target. With the text `hello` and `context_size` 3, the input `hel` has the target `ell`: after `h` comes `e`, after `he` comes `l`, and after `hel` comes `l`. One window therefore holds `context_size` questions with their answers.

**Why:** The text itself already contains the right answer for every position, so nobody has to label anything by hand.

## Step 4: Train and test split

**What:** `split_token_ids` keeps the first 90% of the tokens for training (665,389 tokens) and the last 10% for testing (73,933 tokens).

**Why:** The model never trains on the test part. If the loss is low on the training part but high on the test part, the model memorised the text instead of learning the language. We cut the text at one point instead of picking random windows for the test part, because windows overlap: random windows would put almost the same text into both parts.

## Step 5: Cut examples only when needed

**What:** The token IDs stay in one list. `get_example` cuts a single window from a given start position.

**Why:** `make_examples` builds every window in advance. With `context_size` 64, it needed about 900 MB of memory for our 0.74 MB dataset. Cutting windows when they are needed uses about 12 MB in total. `make_examples` is still there for short texts.

## Step 6: Random batches

**What:** `get_batch` picks `batch_size` random start positions in the training part and returns the inputs and targets as two lists of lists. A batch is a group of examples that the model processes at the same time.

**Why:**

- Random positions keep the model from reading the text in order, so no training step is shaped by a single story.
- Many examples at once are faster to compute together, and each weight update follows the average of many examples instead of a single one.
- `random.seed(0)` makes every run pick the same batches, so the results can be repeated.

**Note:** A window can start or end in the middle of a letter that takes several bytes. When we decode such a window, Python shows `�` in place of the broken letter. This does not affect the model, because the model reads bytes.

**Try:** `python3 data.py`

## Next step

`model.py`: a bigram model, which predicts the next token from the last token only.
