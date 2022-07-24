import requests
from bs4 import BeautifulSoup


def solar_price(state):
    page = requests.get('https://www.marketwatch.com/picks/guides/home-improvement/solar-panel-costs/')

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())

    prices = []

    rows = soup.find_all('td', class_='comparison-normal')
    for i in rows:
        prices.append(i.text)

    for i in range(len(prices)):
        if prices[i].upper() == state.upper():
            p = prices[i+1][1::]
            return float(p) * 909


def hydro_price(state):
    return 0.12 * 909


def wind_price(state):
    return 0.015 * 909
