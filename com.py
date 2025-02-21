from gtts import gTTS

text = 'can i learning trade and be a good and profited trader ? I can ?'

language_text = 'en'

audio = gTTS(text=text, lang=language_text)

audio.save('trade.mp3')
