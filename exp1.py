with open("/Users/denje/Desktop/CL-PROJET/PREPA-TESTS/corpus.txt", "r", encoding="utf-8") as f:
    text = f.read()
import re
sentences = re.split(r'(?<=[.!?])\s+', text.strip())
tokens = text.split()
num_docs = 1
num_sentences= len(sentences)
num_tokens = len(tokens)
types = set(tokens)
num_types = len(types)
ttr = num_types/num_tokens

from collections import Counter
freq = Counter(tokens)
most_common=freq.most_common(20)

print(f"Sentences: {num_sentences}")
print(f"Tokens: {num_tokens}")
print(f"Types: {num_types}")
print(f"TTR: {ttr:.4f}")
print("\nTop 20 tokens:")
for word, count in most_common:
    print(f"{word}\t{count}")