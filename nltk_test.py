import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize 

texto = "NLTK es una biblioteca de procesamiento del lenguaje natural.¡Es genial!" 
tokens = word_tokenize(texto) 
print(tokens) 