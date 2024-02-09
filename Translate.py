from googletrans import Translator, LANGUAGES

def translate_to_gujarati(text):
    # Initialize the Translator
    translator = Translator()
    
    # Translate text from English to Gujarati
    translated_text = translator.translate(text, src='en', dest='gu')
    
    return translated_text.text

english_text = "hello welcome to evalute my task"
gujarati_text = translate_to_gujarati(english_text)
print(f"Translated Text: {gujarati_text}")