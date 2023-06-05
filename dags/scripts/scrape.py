import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.olx.pl/oferty/q-"


def extract_text(result, page):
    return [result.append(data.text.strip()) for data in page]


def extract_from_href(result, page):
    return [result.append(data.get("href")) for data in page]


def scrape_from_olx(item: str = "iphone", pages: int = 1) -> pd.DataFrame:
    result_links, result_names, result_prices, result_state = [], [], [], []

    for page in range(pages):
        URL = f"{BASE_URL}{item}/?page={page}"
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        offer_links = soup.find_all("a", {"class": "css-rc5s2u"})
        extract_from_href(result_links, offer_links)

        offer_names = soup.find_all("h6", attrs={"class": "css-16v5mdi er34gjf0"})
        extract_text(result_names, offer_names)

        offer_prices = soup.find_all("p", attrs={"class": "css-10b0gli er34gjf0"})
        extract_text(result_prices, offer_prices)

        used_prices = soup.find_all("span", attrs={"class": "css-3lkihg"})
        extract_text(result_state, used_prices)

    df = pd.DataFrame(
        {
            "name": result_names,
            "price": result_prices,
            "link": result_links,
            "state": result_state,
        }
    )

    return df
