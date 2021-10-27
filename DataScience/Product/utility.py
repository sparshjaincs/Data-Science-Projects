import requests
import lxml
from bs4 import BeautifulSoup
import pandas as pd

def Product(category, page=1):
    url = f"https://www.amazon.in/s?k={category}&page={page}"
    HEADERS = ({'User-Agent':
               'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36',
                               'Accept-Language': 'en-US, en;q=0.5'})
    data = requests.get(url, headers = HEADERS)
    soup = BeautifulSoup(data.content, "lxml")
    db = pd.DataFrame(columns = ["Vendor","Title", "Link", "Image", "Rating","Price", "Actual_Price"])
    for i in soup.find_all("div", attrs = {"class":"s-asin"}):
        try:
            head = i.find("h2", attrs = {"class" : "s-line-clamp-2"})
            title = head.span.text
            link = "https://www.amazon.in"+head.a.get("href")
            image = i.find("img", attrs = {"class":"s-image"}).get("src")
            price = i.find("span", attrs = {"class": "a-price-whole"}).text
            a_price = i.find("span", attrs= {"class" : "a-offscreen"}).text[1:]
            rating = i.find("span", attrs = {"class":"a-icon-alt"}).text
            temp = pd.DataFrame([["Amazon",title,link,image, price,a_price, rating]], columns=["Vendor","Title","Link","Image","Price","Actual_Price","Rating"])
            db = db.append(temp, ignore_index= True)
        except:
            pass
    return db