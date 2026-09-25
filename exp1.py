with open("/Users/denje/Desktop/GitHub/CL-PROJET/corpus.txt", "r", encoding= "utf-8") as f:
    #opens the file / UTF-8 so special characters load correctly.
    text = f.read()
import re
sentences = re.split(r'(?<=[.!?])\s+', text.strip()) #the pattern (?<=[.!?]) checks that the position right before the is preceded by .  !  or ? but doesnt consume it so the punctuation stays attached to the sentence.
tokens = text.split()
num_docs = 1
num_sentences= len(sentences) #count of sentences
num_tokens = len(tokens) #total token count
types = set(tokens) #converts token list into a set and removes duplicates
num_types = len(types) #count of types
ttr = num_types/num_tokens #type to token ratio

from collections import Counter
freq = Counter(tokens) #how many times a token appears
most_common=freq.most_common(20) #top 20 most frequent

print(f"Sentences: {num_sentences}")
print(f"Tokens: {num_tokens}")
print(f"Types: {num_types}")
print(f"TTR: {ttr:.4f}")
print("\nTop 20 tokens:")
for word, count in most_common:
    print(f"{word}\t{count}")