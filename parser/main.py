from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import csv
import asyncio

import csv

ua = UserAgent()
HEADERS = {'accept': '*/*', 'user-agent': ua.firefox}

URL = "https://www.thisiswhyimbroke.com/"


async def get_page(url):
    return requests.get(url, headers=HEADERS, timeout=5).text if requests.get(url) != 200 else print(
        f"Ошибка, Статус код: {requests.get(url).status_code}")


async def pars_mangalib(page):
    all_info = []
    # with open("index.html", "w", encoding="utf-8") as index:
    #     index.write(page)
    with open("index.html", "r", encoding="utf-8") as index:
        text = index.read()
        new_page = BeautifulSoup(text, "lxml")
        hot_media = new_page.find_all(class_="hot-media-item")
        for item in hot_media:
            item_a = item.find_all("a")[1]
            manga_name = item_a.get_text()
            manga_href = item_a.get("href")
            all_info.append((manga_name, manga_href))
    return all_info


async def record_csv(info):
    with open("example.csv", "w", newline="") as file:
        for i in info:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(i)


async def parser():
    page = await get_page(URL)
    info = await pars_mangalib(page)
    return info


if __name__ == "__main__":
    print(get_page(URL))
