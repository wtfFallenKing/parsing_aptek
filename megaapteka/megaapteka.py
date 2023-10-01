from bs4 import BeautifulSoup
import requests
import csv



def letmeshowyou(urlString):
  url = urlString
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'lxml')

  price   = 'Нет в наличии'
  manCnt  = ''
  medName = ''

  #elif soup.find('span', class_='moneyprice__roubles') == None:

    #price = 'Нет в наличии'
    #print('Нет в наличии')
  findingallelements = soup.find_all('div', class_='tovar-info')

  if findingallelements != None:
    for element in findingallelements:

      medName = element.find('a').get_text()
      print(medName)

      if element.find('div', class_='tovar-info-text') != None:
      
        manCnt = element.find('div', class_='tovar-info-text')

      findPrice = element.find('div', class_='tovar-info-price')

      if findPrice != None:
        if findPrice.find('div', class_='tovar-info-price-text'):
          price = (findPrice.find('div', class_='tovar-info-price-text').get_text())
          
      if findPrice.find('span', class_='thisText'):
        print((findPrice.find('span', class_='thisText')).get_text())
        price = (findPrice.find('span', class_='thisText').get_text())


      productName    = medName
      productCountry = manCnt.get_text()
      productStore   = 'megapteka.ru'
      productPrice   = price


      outString = productName + ';'+ productPrice + ';' + productCountry + ';' + productStore + ';' + urlString


      with open('out.txt', 'a', encoding="utf-8") as file:
      
        file.writelines(''.join(outString))
        file.writelines('\n')
    

def bsXMLparser():

  file = open("products-sitemap-perm.xml", "r", encoding='utf-8')
  content = file.read()
  soup = BeautifulSoup(content,'xml')
  titles = soup.find_all('loc')
  least = len(titles)
  print(least)

  for title in titles:
    least-=1
    print(least)
    letmeshowyou(title.get_text())

    
bsXMLparser()