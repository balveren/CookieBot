#import libraries
from selenium import webdriver
from termcolor import colored
import time

#internet check durumu eklenecek

sorgu = input("Enter url (Ex: https:google.com):\n")
sorgu = sorgu.split()
#importing driver and running in the background
option = webdriver.ChromeOptions()
option.headless = True
driver = webdriver.Chrome(options=option)


Anaurl = "https://www.cookieserve.com"
driver.get(Anaurl)
time.sleep(2)

url_kısım = driver.find_element_by_class_name("form-control").send_keys(sorgu)
buton = driver.find_element_by_id("scan_cookie").click()
time.sleep(5)

tablo = driver.find_element_by_css_selector("#CookieTable")

for row in tablo.find_elements_by_css_selector('tbody'):
    print("\n")
    print(colored("                                           Cookie Bot 0.4         ","red",attrs=['bold']))
    for cell in row.find_elements_by_tag_name('tr'):
        print (100*"-")
        print("\n")
        liste = ["Cookie Name","Description","Duration","Type"]
        i = 0
        while i<4:
            for sutun in cell.find_elements_by_tag_name('td'):
                print(colored(liste[i],"red"),":",sutun.text)
                i += 1
#Özet kısmı eklenecek toplam şu kadar  bulunud gdpr ve kvkk uygunluk durumu gibi
# rapor olarak word e kaydedilecek
# Quit kısmı eklenecek

time.sleep(10)
driver.close()