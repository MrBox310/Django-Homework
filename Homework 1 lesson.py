import requests
from bs4 import BeautifulSoup
import time

print("Start - Начало работы\nExit - Выход")
print()
while True:
    los=str(input()).lower()
    text=""
    if los=="start":
        resmak=str(input("Вывод результата:\nConsole - в консоль\nFile - в файл\n")).lower()
        linkis=str(input("Ссылка сайта: "))
        if str(requests.get("https://www.google.com"))=='<Response [200]>':
            if str(requests.get(linkis))=='<Response [200]>':
                response=requests.get(linkis)
                soup=BeautifulSoup(response.content,"html.parser")
                links=soup.find_all("a")
                for u in links:
                    try:
                        text+=str(u)+"\n"
                        response=requests.get(u.get("href"))
                        soup=BeautifulSoup(response.content,"html.parser")
                        lonks=soup.find_all("a")
                        for y in lonks:
                            text+="-"*5+str(y)+"\n"
                    except:
                        pass
            else:
                print("Ссылка нерабочая")
        else:
            print("Нет подключения к интернету")
        if resmak!="console" and resmak!="file":
            resmak="console"
        if resmak == "console":
            print(text)
        elif resmak == "file":
            file=open("Result.txt","w",encoding="cp1251")
            file.write(text)
            file.close()
        print("Процесс завершен")
    elif los=="exit":
        break

print("До скорого")
time.sleep(5)
