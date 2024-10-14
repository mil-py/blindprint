import random

ltask = [
        '',
        'asdf','asdfg',
        "zxcv", "zxcvb",
        "qwer", "qwert",
        "asdfgqwert","asdfgzxcvb",
        "zxcvbqwert", "asdfgzxcvbqwert"
    ]
rtask = [
        '',
        "jkl;'",  "hjkl;'",
        "m,./",  "nm,./",
        "uiop[]",  "yuiop[]\\",
        "hjkl;'+nm,./",  "hjkl;'+yuiop[]\\",
        "yuiop[]\\+nm,./",  "hjkl;'+yuiop[]\\+nm,./"

    ]


def blindp(string):
    newstr = ''
    for i in range(0,15):
        newstr = newstr + string[random.randint(0, len(string)-1)]
    #vstavim probely krome nachala i konza

    for s in range(1, len(newstr)-2):
        if random.randint(1,3) == 1 and newstr[s-1] != " ":
            newstr = newstr[0:s]+' '+newstr[s:-1]
    # if newstr[len(string)-1]==" ":
    #     newstr = newstr[0:-1]
    print("Повторите строку и нажмите ENTER")


    print(newstr)
    err=True
    while err:
        
      userString=input()
      if userString == newstr:
        err = False
        print("Верно!")

      else:
        print("ОШИБКА!")


while True:
    print("traning - 1, exit - 0 ")
    if input('>>') == '0':
        break

    print("input left hand task:")
    print("0 - left hand relax")
    print("1 - asdf",' / ', "2 - asdfg")
    print("3 - zxcv",' / ',"4 - zxcvb")
    print("5 - qwer", ' / ', "6 - qwert")
    print("7 - asdfg+qwert", ' / ', "8 - asdfg+zxcvb")
    print("9 - zxcvb+qwert", ' / ', "10 - asdfg+zxcvb+qwert")
    l=int(input('>>'))



    print("input right hand task:")
    print("0 - right hand relax")
    print("1 - jkl;'",' / ',"2 - hjkl;'")
    print("3 - m,./", ' / ', "4 - nm,./")
    print("5 - uiop[]", ' / ', "6 - yuiop[]\\")
    print("7 - hjkl;'+nm,./", ' / ', "8 - hjkl;'+yuiop[]\\")
    print("9 - yuiop[]\\+nm,./", ' / ', "10 - hjkl;'+yuiop[]\\+nm,./")
    r = int(input('>>'))

    string = ltask[l]+rtask[r]

    for i in range(1,10):

        blindp(string)
