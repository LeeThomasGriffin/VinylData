import datetime
from bs4 import BeautifulSoup
import requests


def main():
    begin_time = datetime.datetime.now()
    
    #rollin rec website has been changed
    #rollinRec()
    
    merchBar()
    victrola()
    #print how long it takes to get infromation
    print(datetime.datetime.now() - begin_time)

def rollinRec():
     #get html of website
    htmlText = requests.get('https://rollinrecs.com/this-weeks-restocks/').text
    soup = BeautifulSoup(htmlText, 'lxml')
     #go to section where record infromation is stored
    productGrid = soup.find('div', class_ = 'product-grid grid-container')
    #create list of all found records and their prices
    productList = productGrid.find_all('h2', class_ = 'product-grid-item-name')
    productListPrice = productGrid.find_all('div', class_ = 'price')
    #make sure there is a record price for each record
    if (len(productList) == len(productListPrice)):  
        #for each record in record list
        for i in range(0, len(productList)):
            #get record information
            artistInfo = (productList[i].text).strip()
            price = (productListPrice[i].text).strip()
            count = 0
            artistInfo = artistInfo.split('-')
            #print info
            for info in artistInfo:
                if count == 0:
                    print("Artist: " + info.strip())
                else:
                    print("Vinyl: " + info.strip())
                count += 1
            print("Price: " + price, end = "\n")
            print()
    
def merchBar():
     #get html of website
    htmlText = requests.get('https://www.merchbar.com/search?idx=Merch_created_desc&dFR%5Btags%5D%5B0%5D=vinyl&dFR%5Bgenre%5D%5B0%5D=R%26B%2FHiphop&dFR%5Bstatus_name%5D%5B0%5D=AVAILABLE&cpt=Ivaly%20Erpbeqf&p=1').text
     #go to section where record infromation is stored
    soup = BeautifulSoup(htmlText, 'lxml')
     #create list of all found records
    productList = soup.find_all('div', class_ = 'SearchInterface_merchTileContainer__by__3 px-2 col-md-4 col-6')
    #for each record in record list
    for product in productList:
         #get record's name, artist
        productArtist = product.find('div', class_ = 'MerchTile_brandName__2Ljvm')
        productName = product.find('div', class_ = 'MerchTile_title__3Y_tD')
        #print artist and record name
        print("Artist: " + productArtist.text)
        print("Vinyl: " + productName.text)
        #get record price
        productPrice = product.find('div', class_ = 'MerchTile_priceContainer__2BSVH')
        productPrice = (productPrice.text).split(' ')
        #print price
        if (len(productPrice)) == 2:
            print("Price: " + productPrice[1])
        elif (len(productPrice)) == 1:
            print("Price: " + productPrice[0])
        print()


def victrola():
    #get html of website
    htmlText = requests.get('https://victrola.com/collections/genre-rap-hip-hop').text
    #go to section where record infromation is stored
    soup = BeautifulSoup(htmlText, 'lxml')
    productList = soup.find(id = 'bc-sf-filter-products')
    #create list of all found records
    productList2 = productList.find_all('div', class_ = 'product-card__content')
    #for each record in record list
    for product in productList2:
        #get record's name, artist and price
        productInfo = product.find('h3', class_ = 'h6').text
        productPrice = product.find('p',class_ = 'bc-sf-filter-product-item-price').text.strip()
        productInfo = productInfo.split(': ')
        count = 0
        #for infromation of each record, print
        for info in productInfo:
            if count == 0:
                print("Artist: " + productInfo[0])
            if count == 1:
                print("Vinyl: " + productInfo[1])
            count += 1
        print("Price: " + productPrice)
        print()




main()

