# import speech_recognition as sr
# # from google_trans_new import google_translator
# from translate import Translator
# from gtts import gTTS
# from playsound import playsound
#
# r = sr.Recognizer()
# # translator=google_translator()
# translator = Translator(to_lang="mr")
# with sr.Microphone() as source:
#     print("Speak now!")
#     audio = r.listen(source)
#
#     try:
#         speech_text = r.recognize_google(audio)
#         print("Recognized speech:", speech_text)
#     except sr.UnknownValueError:
#         print("Speech recognition could not understand the input.")
#     except sr.RequestError:
#         print("Could not request the result from google")
#
#     # translated_text= translator.translate(speech_text,lang_tgt='mr')
#     translated_text = translator.translate(speech_text)
#     # print(translated_text)
#     print("Translated text:", translated_text)
#
#     voice=gTTS(translated_text,lang='mr')
#     voice.save('voice.mp3')
#
#     playsound("voice.mp3")
#
#
import speech_recognition as sr
from translate import Translator
from gtts import gTTS
import pygame

r = sr.Recognizer()
translator = Translator(to_lang="hi")

pygame.mixer.init()

with sr.Microphone() as source:
    print("Speak now!")
    audio = r.listen(source)

try:
    speech_text = r.recognize_google(audio)
    print("Recognized speech:", speech_text)
except sr.UnknownValueError:
    print("Speech recognition could not understand the input.")
except sr.RequestError:
    print("Could not request the result from Google.")

translated_text = translator.translate(speech_text)
print("Translated text:", translated_text)

voice = gTTS(translated_text, lang='hi')
voice.save('voice.mp3')

pygame.mixer.music.load('voice.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue
