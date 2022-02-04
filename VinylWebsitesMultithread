import datetime
from bs4 import BeautifulSoup
import requests
import threading



def main():
    #arrayOfWebsites =
    begin_time = datetime.datetime.now()
    #rollinRec()
    threadCount = 0
    if(threadCount < 2):
        try:
           t1 = threading.Thread(target=merchBar)
           t2 = threading.Thread(target=victrola)
           threadCount += 2
           t1.start()
           t2.start()
           t1.join()
           t2.join()
           
        except:
           print("Error: unable to start thread")

    print(datetime.datetime.now() - begin_time)

def rollinRec():
    htmlText = requests.get('https://rollinrecs.com/this-weeks-restocks/').text
    soup = BeautifulSoup(htmlText, 'lxml')
    productGrid = soup.find('div', class_ = 'product-grid grid-container')
    productList = productGrid.find_all('h2', class_ = 'product-grid-item-name')
    productListPrice = productGrid.find_all('div', class_ = 'price')
    if (len(productList) == len(productListPrice)):      
        for i in range(0, len(productList)):
            artistInfo = (productList[i].text).strip()
            price = (productListPrice[i].text).strip()
            count = 0
            artistInfo = artistInfo.split('-')
            for info in artistInfo:
                if count == 0:
                    print("Artist: " + info.strip())
                else:
                    print("Vinyl: " + info.strip())
                count += 1
            print("Price: " + price, end = "\n")
            print()
    
def merchBar():
    htmlText = requests.get('https://www.merchbar.com/search?idx=Merch_created_desc&dFR%5Btags%5D%5B0%5D=vinyl&dFR%5Bgenre%5D%5B0%5D=R%26B%2FHiphop&dFR%5Bstatus_name%5D%5B0%5D=AVAILABLE&cpt=Ivaly%20Erpbeqf&p=1').text
    soup = BeautifulSoup(htmlText, 'lxml')
    productList = soup.find_all('div', class_ = 'SearchInterface_merchTileContainer__by__3 px-2 col-md-4 col-6')
    for product in productList:
        productArtist = product.find('div', class_ = 'MerchTile_brandName__2Ljvm')
        productName = product.find('div', class_ = 'MerchTile_title__3Y_tD')
        print("Artist: " + productArtist.text)
        print("Vinyl: " + productName.text)
        productPrice = product.find('div', class_ = 'MerchTile_priceContainer__2BSVH')
        productPrice = (productPrice.text).split(' ')
        if (len(productPrice)) == 2:
            print("Price: " + productPrice[1])
        elif (len(productPrice)) == 1:
            print("Price: " + productPrice[0])
        print()


def victrola():
    htmlText = requests.get('https://victrola.com/collections/genre-rap-hip-hop').text
    soup = BeautifulSoup(htmlText, 'lxml')
    productList = soup.find(id = 'bc-sf-filter-products')
    productList2 = productList.find_all('div', class_ = 'product-card__content')
    for product in productList2:
        productInfo = product.find('h3', class_ = 'h6').text
        productPrice = product.find('p',class_ = 'bc-sf-filter-product-item-price').text.strip()
        productInfo = productInfo.split(': ')
        count = 0
        for info in productInfo:
            if count == 0:
                print("Artist: " + productInfo[0])
            if count == 1:
                print("Vinyl: " + productInfo[1])
            count += 1
        print("Price: " + productPrice)
        print()




main()

