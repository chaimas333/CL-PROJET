import re

def naivetokenize(text):
    return re.findall(r"\w+|[^\w\s]", text) #findall (pattern, text): finds all matches of pattern in text. that pattern means match either one or more word characters (\w+ -> letters digits underscore ex: Dr.) or any single non-word non-whitespace character ([^\w\s] -> punctuation like .  ,  @  -) and it returns a list of tokens.

with open ("/Users/denje/Desktop/CL-PROJET/PREPA-TESTS/tokenization_test.txt", "r", encoding="utf-8") as f:
    lines =[l.strip() for l in f if l.strip()]#iterates line by line. l.strip() removes leading/trailing whitespace. "if l,strip()" removes empty lines.
    
with open ("/Users/denje/Desktop/CL-PROJET/PREPA-TESTS/gold_tokens.txt", "r", encoding="utf-8") as f:
    gold_tokens = [l.strip() for l in f if l.strip()] #same thing just with the gold tokens which end up as my list of correct tokens to compare against
    
pred_tokens =[]
for line in lines:
    pred_tokens.extend(naivetokenize(line))
    #Initializes an empty list. For each sentence in lines, runs tokenizer and appends its tokens to pred_tokens
    #(.extend() adds all items from the returned list, not the list itself). After the loop, pred_tokens holds every predicted token across the whole file, in order.
    
print(f"Predicted tokens: {len(pred_tokens)}")
print(f"Gold tokens: {len(gold_tokens)}")
print()
print("PRED:", pred_tokens)
print()
print("GOLD:", gold_tokens)