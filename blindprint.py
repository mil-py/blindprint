import random

ltask = [
    '',
    'asdf', 'asdfg',
    "zxcv", "zxcvb",
    "qwer", "qwert",
    "asdfgqwert", "asdfgzxcvb",
    "zxcvbqwert", "asdfgzxcvbqwert"
]
rtask = [
    '',
    "jkl;'", "hjkl;'",
    "m,./", "nm,./",
    "uiop[]", "yuiop[]\\",
    "hjkl;'+nm,./", "hjkl;'+yuiop[]\\",
    "yuiop[]\\+nm,./", "hjkl;'+yuiop[]\\+nm,./"

]

r_keys = [
    [''],
    ['jy6', 'jy67u', 'jnmh', 'jmnhuy67'],
    ['ki8', 'k,', 'k8i,'],
    ['lo9', 'l.o9'],
    [";'/", "p[]\\", ";0-="]
]
l_keys = [
    [''],
    ['fgrt', 'fgrt45', 'fgbv', 'fgrt45vb'],
    ['de3', 'dc', 'dce3'],
    ['sw2', 'sx', 'sxw2'],
    ['aqz', 'aq1`', 'azq1`']
]


def blindp(string):
    if len(string) <= 1:
        return
    newstr = ''
    for i in range(0, 15):
        newstr = newstr + string[random.randint(0, len(string) - 1)]
    # vstavim probely krome nachala i konza

    for s in range(1, len(newstr) - 2):
        if random.randint(1, 3) == 1 and newstr[s - 1] != " ":
            newstr = newstr[0:s] + ' ' + newstr[s:-1]
    # if newstr[len(string)-1]==" ":
    #     newstr = newstr[0:-1]
    print("Повторите строку и нажмите ENTER")

    print(newstr)
    err = True
    while err:

        userString = input()
        if userString == newstr:
            err = False
            print("Верно!")

        else:
            print("ОШИБКА!")


while True:
    print("fingers traning - 1, свое задание -2,  exit - 0 ")
    way = input('>>')
    if way == '0':
        break
    elif way == '2':
        string = input("введите задание >>")  # ввод своего задания
        for i in range(1, 5):
            blindp(string)
    else:

        print("введите задание для левой руки ")
        print("например 11223, 0 - рука оттдыхает")
        print("1 - указательный")
        print("2 - средний")
        print("3 - безымянный")
        print("4 - мизинец")

        l = input('>>')


        print("введите задание для правой руки ")
        print("например 13, 0 - рука оттдыхает")
        print("1 - указательный")
        print("2 - средний")
        print("3 - безымянный")
        print("4 - мизинец")

        r = input('>>')


        for sym in l:
            for str_ in l_keys[int(sym)]:
                blindp(str_)
                blindp(str_)
                blindp(str_)

        for sym in r:
            for str_ in r_keys[int(sym)]:
                blindp(str_)
                blindp(str_)
                blindp(str_)



