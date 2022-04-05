import requests
from bs4 import BeautifulSoup

def scrape_weather():
    print("[오늘의날씨]")
    url ="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8"
    res = requests.get(url)
    #res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    
    cast = soup.find("p", attrs={"class":"summary"}).get_text()
    
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().replace("현재 온도","")#현재온도

    lowest_temp = soup.find("span", attrs={"class":"lowest"}).get_text() #최저 온도

    highest_temp = soup.find("span", attrs={"class":"highest"}).get_text() #최고 온도

    #오전 오후 강수 확률
    weather_inner = soup.findAll("span",attrs={"class":"weather_inner"})
    #weather_inner2 = soup.find("span",attrs={"class":"weather_inner"}).get_text()
    #미세먼저 초미세먼지
    dust = soup.findAll("span",attrs={"class":"txt"})

    #출력
    print(cast)
    print("현재 온도{}({} / {})".format(curr_temp,lowest_temp,highest_temp))
    print("오전{} / 오후{}".format(weather_inner[0].get_text().replace("오전",""),weather_inner[1].get_text().replace("오후","")))
    print("미세먼지 {} / 초미세먼지 {}".format(dust[0].get_text(), dust[1].get_text()))
scrape_weather()