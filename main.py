import base64
import os

import pandas as pd

from filtering import deduplicate, keep_chinese, min_length, remove_punctuation, remove_stopwords


def decode_token(x):
    raw_bytes = base64.b64decode(x)
    try:
        return raw_bytes.decode("utf-8")
    except UnicodeDecodeError:
        return raw_bytes.decode("latin-1")


def apply_filter(series, processes):
    for process in processes:
        series = process(series)
    return series.sort_values(key=lambda x: x.str.len(), ascending=False)


def main():
    file_path = "./downloaded/o200k_base.tiktoken"
    if not os.path.exists(file_path):
        df = pd.read_csv("https://openaipublic.blob.core.windows.net/encodings/o200k_base.tiktoken")
        df.to_csv(file_path, index=False)

    df = pd.read_csv(file_path, header=None)
    tokens_base64 = df[0].str.split().str[0]
    tokens = tokens_base64.apply(decode_token)
    filtered = apply_filter(tokens, [remove_punctuation, keep_chinese, min_length, remove_stopwords, deduplicate])
    filtered_df = tokens[filtered.index].reset_index()
    filtered_df.columns = ["Index in Tokenizer", "Token"]
    filtered_df.to_csv("./o200k_base_filtered.csv", index=False)

    filtered_df.to_markdown("result.md", index=False)


if __name__ == "__main__":
    main()
