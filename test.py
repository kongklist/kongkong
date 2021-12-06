import googletrans
from googletrans import Translator
 
# print(googletrans.LANGUAGES)
text1 =""
 
translator = Translator()
trans1 = translator.translate(text1, src='ko', dest='en')
 
print("English to Japanese: ", trans1.text)


# 'el': 'greek','en': 'english'   'fr': 'french', 'es': 'spanish', ja
