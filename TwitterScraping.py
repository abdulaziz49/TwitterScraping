from selenium import webdriver 
from colorama import Fore , init
import bs4
import re
import time


#methods read the links.txt file content then return array
def files():
    try:
        Attemps = 0
        links = []
        urls = open('links.txt', 'r')
        for link in urls:
            links.append(str(link))
            Attemps +=1
        return links , Attemps
    except FileNotFoundError as e:
        print("links.txt not found")


#methods recived the array that have links and Extract the data
def job(links , Attemps):
    counter = 0 #Count the Number of Account Or links you insert
    result = open("Result.txt" , mode="a" , encoding="utf-8") #Create a result file to save the data
    MyList = []
    for link in links:
        browser.get(link)
        time.sleep(3) # The Time that I need to open a Twitter page and download the data from the server
        #these will be change from person to another , if you have a good connection you can remove
        #the function but if not increase the time
        page = bs4.BeautifulSoup(browser.page_source , 'html.parser')
        notfound = "This account doesn’t exist"
        suspended = "Account suspended"
        strcounter = str(counter)
        chick = page.findAll('span',class_="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
        for d in chick:
            MyList.append(d.string)
        try:
            if notfound in str(MyList[7]):
                word = strcounter+":@"+link[20:]+" "+"".join(notfound)
                result.writelines(word+"\n")
                counter+=1
                print(f"{Fore.MAGENTA}{counter}/{Attemps} Has Chicked")
            elif suspended in str(MyList[7]):
                word = strcounter+":"+link[20:]+" "+"".join(suspended)
                result.writelines(word+"\n")
                counter+=1
                print(f"{Fore.MAGENTA}{counter}/{Attemps} Has Chicked")
            else:
                name = MyList[4].string
                for v in MyList:
                    if "Joined" in str(v):
                        date = str(v)
                    if "@" in str(v):
                        user = str(v)
                temp = re.findall("\d{4}" , date)
                word = strcounter+":"+user+":"+name+":"+temp[0]
                result.writelines(word+"\n")
                counter+=1
                print(f"{Fore.MAGENTA}{counter}/{Attemps} Has checked")
            MyList.clear()
        except IndexError as e:
                word = strcounter+":"+"in this user @"+link[20:]+" I can't load the page"
                result.writelines(word+"\n")
                counter+=1
                MyList.clear()


#Auto Rest color for console
init(autoreset=True)
#Open the selenium webdriver
browser = webdriver.Edge()
#methods read the links.txt file content then return array and count of Attemps Line 9
links,Attemps = files()
#methods recived the array that have links and Extract the data Line 23
job(links , Attemps)