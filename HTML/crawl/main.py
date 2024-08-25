import requests
from bs4 import BeautifulSoup

BOOK_PAGE = "ol.row col-xs-6.col-sm-4.col-md-3.col-lg-3"
URL = "https://books.toscrape.com/"
TITLE = "article.product_pod h3 a"
PRICE = "div.product_price p.price_color"

page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")

for counter,book in enumerate(soup.select(BOOK_PAGE), start = 1):
    book_title = book.select_one(TITLE).attrs = ["title"]
    book_price = book.select_one(PRICE).string
    print(book_price)