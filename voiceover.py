from gtts import gTTS

def createVoiceover(text, filename):
    language = 'en'
    speech = gTTS(text = text, lang = language, slow = False)
    speech.save(filename)