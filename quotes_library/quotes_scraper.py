from bs4 import BeautifulSoup
import requests
import random

popular_choice = ['motivational', 'life', 'positive', 'friendship', 'success', 'happiness', 'love','strength'\
                  ,'fathersday','mothersday']


def get_quotes_by_topic(type, number_of_quotes=1):
    url = "http://www.brainyquote.com/quotes/topics/" + type
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []
    for quote in soup.find_all('a', {'title': 'view quote'}):
        quotes.append(quote.contents[0])
    random.shuffle(quotes)
    result = quotes[:number_of_quotes]
    return result


def get_random_quote():
    result = get_quotes(popular_choice[random.randint(0, len(popular_choice) - 1)])
    return result


def get_quotes_by_author(authorname, number_of_quotes=1):
    authorname=authorname.replace("." ," ").lower().split()
    authorname="_".join(authorname)
    url = "https://www.brainyquote.com/authors/" + authorname
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []
    for quote in soup.find_all('a', {'title': 'view quote'}):
        quotes.append(quote.contents[0])
    random.shuffle(quotes)
    result = quotes[:number_of_quotes]
    return result


def get_quotes_of_the_day(number_of_quotes=1):
    url = "https://www.brainyquote.com/quote_of_the_day"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []
    for quote in soup.find_all('a', {'title': 'view quote'}):
        quotes.append(quote.contents[0])
    random.shuffle(quotes)
    result = quotes[:number_of_quotes]
    return result


def get_quotes_by_profession(profession, number_of_quotes=1):
    profession=profession.lower()
    profession=profession+ "_quotes"
    url = "https://www.brainyquote.com/profession/" + profession
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []
    for quote in soup.find_all('a', {'title': 'view quote'}):
        quotes.append(quote.contents[0])
    random.shuffle(quotes)
    result = quotes[:number_of_quotes]
    return result

#todo: add top 100 quotes scraping function
