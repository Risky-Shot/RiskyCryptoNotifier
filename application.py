from win10toast import ToastNotifier
import time
import requests
import config as cfg

def show_not(title, text):
    toaster = ToastNotifier()
    toaster.show_toast(title,
     text,
     icon_path="custom.ico",
     duration=120)

lastPrice = 0.0

def checkPrice(lastPrice) :
    url = "https://api.coingecko.com/api/v3/coins/"+ cfg.coin +"?localization=false&tickers=false&market_data=true&community_data=false&developer_data=true&sparkline=false"

    while True:
        response = requests.get(url).json()

        currPrice = response['market_data']['current_price'][cfg.currency]


        if lastPrice > currPrice:
            show_not(response['name'],'Price DECREASED by ' + str(round(lastPrice - currPrice, 2)) + ' to ' + str(round(currPrice,2)) + '. Your current value : ' + str(round(cfg.owned_coins * currPrice, 2)))
        elif currPrice > lastPrice:
            show_not(response['name'],'Price INCREASED by ' + str(round(currPrice - lastPrice, 2)) + ' to ' + str(round(currPrice, 2)) + '. Your current value : ' + str(round(cfg.owned_coins * currPrice, 2)))
        else:
            print('NO CHANGE IN PRICE')

        currTime = time.localtime()
        currTime = time.asctime(currTime)
        print(currTime)
        print('Current Price : ' + str(round(currPrice, 2)))

        lastPrice = currPrice
        time.sleep(30)

        
checkPrice(lastPrice)

