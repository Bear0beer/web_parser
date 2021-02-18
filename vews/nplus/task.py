import requests
import re
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.find(id="main").find("a").get("href")

    return data


def get_text(html):
    soup = BeautifulSoup(html, "lxml")
    article = soup.find("section", id="main")
    title = article.find("article").find("h1").text
    demo_body = article.find("div", class_="body js-mediator-article")
    img = demo_body.find("img").get("src")
    txt = re.compile(r'\w+=\s*')
    body = txt.sub("", demo_body.text)

    return {"title": title, "img": img, "body": body}


def main(url):
    html = get_html(url)
    data = get_data(html)
    html = get_html(url + data)
    text = get_text(html)

    text["link"] = url + data

    return text