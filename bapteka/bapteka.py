from bs4 import BeautifulSoup
import requests
def letmeshowyou(urlString):
    url = urlString
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    price = ''
    productCountry = ''
    productName = ''
    productStore = 'b-apteka.ru'
    productPrice = price
    try:
        if soup.find('div', class_='product-card-x__price') != None:
            div = soup.find('div', class_='product-card-x__price')
            priceFind = div.find('div', class_='price_new')
            priceFinal = priceFind.get_text();
            productPrice = priceFinal
            medName = soup.find('h1', itemprop='name')
            productName = medName.get_text()
            if soup.find('div', class_='product-card-x__provider').find('a') != None:
                Country = soup.find('div', class_='product-card-x__provider').find('a')
                CountryText = Country.get_text()
                productCountry = CountryText
            else:
                productCountry = 'Не указан'
            productStore = 'b-apteka.ru'
            outString = productName + ';' + productPrice + ';' + productCountry + ';' + productStore + ';' + urlString
            with open('out.txt', 'a', encoding="utf-8") as file:
                file.writelines(''.join(outString))
                file.writelines('\n')
    except:
        print("Ошибка на: " + urlString)
def bsXMLparser():
    file = open("sitemap-perm-0.xml", "r", encoding='utf-8')
    content = file.read()
    soup = BeautifulSoup(content, 'xml')
    titles = soup.find_all('loc')
    least = len(titles)
    print(least)
    for title in titles:
        least -= 1
        print(least)
        letmeshowyou(title.get_text())
bsXMLparser()