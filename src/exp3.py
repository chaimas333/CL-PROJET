import re #regex module for costum tokenizer
import nltk #NLP library with standard tokenizer
nltk.download('punkt') #downloads NLTK pretrained sentence segmentation models
nltk.download('punkt_tab') #same as above
from nltk.tokenize import word_tokenize 

# --- Test sentence (same as Exp 2) ---
text = ("Dr. Smith works at HHU. The price is 12.50 euros. "
        "Visit https://example.com for more information. "
        "My email is test@example.com. NLP is state-of-the-art. "
        "This isn't a simple example. The student studies Computerlinguistik.")

# --- Gold standard (correct tokenization) ---
gold = ['Dr.', 'Smith', 'works', 'at', 'HHU', '.', 'The', 'price', 'is', '12.50',
        'euros', '.', 'Visit', 'https://example.com', 'for', 'more', 'information', '.',
        'My', 'email', 'is', 'test@example.com', '.', 'NLP', 'is', 'state-of-the-art', '.',
        'This', "isn't", 'a', 'simple', 'example', '.', 'The', 'student', 'studies',
        'Computerlinguistik', '.']

# --- Custom regex tokenizer (Exp 2) ---
def regex_tokenize(text): 
    return re.findall(r"\w+|[^\w\s]", text) #returns all non overlapping match of pattern in text as list

pred_regex = regex_tokenize(text) #runs it and stores the resulting token list

# --- Standard NLP tokenizer (NLTK) ---
pred_nltk = word_tokenize(text) #calls NLTK pretrained tokenizer on text using rule/statistical based knowledge

# --- Comparison ---
def compare(name, pred, gold): #label (name) predicted token list (pred) and gold list
    print(f"\n{name}") 
    print(f"Tokens: {len(pred)}  |  Gold: {len(gold)}") #token count for quick comparison
    print(pred) #full token list

compare("Custom Regex Tokenizer", pred_regex, gold)
compare("NLTK word_tokenize", pred_nltk, gold)
print(f"\nGold Standard ({len(gold)} tokens)")
print(gold)
#calls compare once per tokenizer then prints gold list with its length

# --- Quantitative evaluation: exact match rate ---
def match_rate(pred, gold):
    matches = sum(1 for p, g in zip(pred, gold) if p == g) #pairs up elements pos by pos
    #yields 1 for every pos where pred and gold tokens match then sums- giving total matching pos
    return matches / len(gold) #dividing, gives the fraction of gold tokens matched @ same pos 

print(f"\nRegex match rate vs gold: {match_rate(pred_regex, gold):.2%}")
print(f"NLTK match rate vs gold: {match_rate(pred_nltk, gold):.2%}")
#prints both tokenizers' match rates against gold for direct comparison.