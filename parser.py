import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, features = "html.parser")
    div = soup.find('div', class_ = 'module-kurs_nbrb')
    tr = div.find_all('tr')
#    print(type(tr))
    result = {"data": [], "1 USD": [], "1 EUR": [], "100 RUB": []}
    print(tr[0])
    """ tags = div.find_all('td')
    if tags.text != "":
            result = result + tags.text + "\t"
            print(tags.text) """
    print(result)


"""     today_data =
    tomorrow_data = tr[2]
    today_USD = tr[7]
    tomorrow_USD = tr[8]
    print(today_data, tr[2], tr[7], tr[8]) """

def main():
    parse(get_html('https://select.by/kurs/'))

if __name__ == '__main__':
    main()