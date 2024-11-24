from msvcrt import getwche
from gtts import gTTS
import os


def t2s(txt, lang='ru'):
    if txt:
        tts = gTTS(text=txt, lang=lang)
        tts.save("output.mp3")
        os.system("start output.mp3")

w=''
while  w != 'конец':
    w = ''
    while True:

        b = getwche()
        # print(ord(b))
        #
        # if b == ' ' :
        #     break
        if ord(b) == 13:
            print()
            t2s(w)
            break
        w += b


