import random

random_number = random.randint(0, 9)



asd = "asdf"
hj="jkl;'"
qw="qwert"
yu="yuiop[]"
zx="zxcvb"
nm="nm,./"



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

for i in range(1,10):

  blindp("asdf")
