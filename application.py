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

    i = 1
    while i > 0:
        response = requests.get(url).json()

        currPrice = response['market_data']['current_price'][cfg.currency]
        

        if lastPrice > currPrice:
            show_not("DOGECOIN",'Price decreased by ' + str(lastPrice - currPrice) + ' to ' + str(currPrice) + '. Your current value : ' + str(cfg.owned_coins * currPrice))
        elif currPrice > lastPrice:
            show_not("DOGECOIN",'Price increased by ' + str(currPrice - lastPrice) + ' to ' + str(currPrice) + '. Your current value : ' + str(cfg.owned_coins * currPrice))
        else:
            print('same')

        print(currPrice)
        print(lastPrice)
        lastPrice = currPrice
        time.sleep(30)

        
checkPrice(lastPrice)
