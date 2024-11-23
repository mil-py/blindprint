from msvcrt import getwche
from gtts import gTTS
import os

def t2s(txt,lang='ru'):
    if txt :
        tts = gTTS(text=txt,lang=lang)
        tts.save("output.mp3")
        os.system("start output.mp3")
while True:
    w=''
    while (b:=getwche()) != ' ':
         w+=b

    t2s(w)
