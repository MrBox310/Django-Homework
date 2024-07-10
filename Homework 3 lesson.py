from random import randint,choice
import os
import time

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def zamena(znak):
    if len(str(znak))-1:
        return f" {znak} "
    else:
        return f"  {znak} "

def textres(lis,nickname):
    print(f"====== Карточка {nickname} ======")
    for u in lis:
        print("".join(list(map(str,list(map(zamena,u))))))
    print("="*36)
    print()

def genernums():
    askd=[]
    sdf=15
    while sdf!=0:
        sa=randint(0,90)
        if not(sa in askd):
            askd.append(sa)
            sdf-=1
    return askd

def generpole(lis,askd):
    aw=0
    for u in lis:
        mn=5
        while mn!=0:
            sd=randint(0,8)
            if u[sd]==" ":
                u[sd]=askd[aw]
                mn-=1
                aw+=1
    return lis

def firslist():
    ksd=[]
    for u in range(3):
        sk=[]
        for t in range(9):
            sk.append(" ")
        ksd.append(sk)
    return ksd 

class Human:
    def __init__(self):
        self.nums=genernums()
        self.poll=firslist()
        self.polle=generpole(self.poll,self.nums)
        self.name="Human"
        

class Bot:
    def __init__(self):
        self.nums=genernums()
        self.poll=firslist()
        self.polle=generpole(self.poll,self.nums)
        self.name="Bot"


print("Всех приветствую в нашей игре")
game=True
lisplar=[]
lisnam=[]
hm=1
bt=1
lisk=["h","b"]
colplar=int(input("Напишите количество игроков: "))
for u in range(colplar):
    srt=str(input("Игрок (h) или Бот (b) - "))
    if not(srt in lisk):
        srt="h"
    
    if srt=="h":
        lisplar.append(Human())
        lisnam.append(f"Human player {hm}")
        hm+=1
    else:
        lisplar.append(Bot())
        lisnam.append(f"Bot player {bt}")
        bt+=1
print()
for u in range(len(lisplar)):
    textres(lisplar[u].polle,lisnam[u])

lisvar=["cls","con"]
allnums=lambda x: len(set([element for each_list in x.polle for element in each_list]))==2
lismuns=[]
lismyn=list(range(91))
#print(lismyn)
while game:
    #clear()
    num=choice(lismyn)
    del lismyn[lismyn.index(num)]
    print("="*10+f"Рандомное число: {num}"+"="*10)
    for u in range(len(lisplar)):
        textres(lisplar[u].polle,lisnam[u])
    for u in range(len(lisplar)):
        try:
            if lisplar[u].name=="Human":
                otvet=str(input(f"Реакция игрока {lisnam[u]}: (cls) - Зачернуть, (con) - Продолжить "))
                if not(otvet in lisvar):
                    otvet="con"
                if otvet=="cls":
                    if num in lisplar[u].nums:
                        lisk=lisplar[u].poll
                        for lis1 in range(len(lisk)):
                            if num in lisk[lis1]:
                                nm2=lisk[lis1].index(num)
                                nm1=lis1
                        lisplar[u].poll[nm1][nm2]="--"
                    else:
                        del lisplar[u]
                        del lisnam[u]
                        continue
                elif otvet=="con":
                    if num in lisplar[u].nums:
                        del lisplar[u]
                        del lisnam[u]
                        continue
            else:
                if num in lisplar[u].nums:
                    lisk=lisplar[u].poll
                    for lis1 in range(len(lisk)):
                        if num in lisk[lis1]:
                            nm2=lisk[lis1].index(num)
                            nm1=lis1
                    lisplar[u].poll[nm1][nm2]="--"
        except:
            pass
    
        if len(lisplar)==1 or (True in list(map(allnums,lisplar))):
            game=0
    time.sleep(0)
        
if len(lisplar)>1:
    for y in range(len(lisplar)):
        if len(set([element for each_list in lisplar[y].polle for element in each_list]))==2:
            print(f"Победитель игры - {lisnam[y]}")
else:
    print(f"Победитель игры - {lisnam[0]}")
print("Всем спасибо за игру")
input()
