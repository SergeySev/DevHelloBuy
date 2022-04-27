import urllib.parse
import requests


token = "1800056577:AAF7OCGAUeqNSy985Omm_qF7fmfmmCwIaTQ"
url = "https://api.telegram.org/bot" + token
webAppUrl = "https://script.google.com/macros/s/AKfycbwV_JSgWMXn0O5OSXJplQFV2_RsVNBg2PIWIxlIbD1MTjsSHbI/exec"

URL_OKX = "https://www.okx.com/api/v5/market/index-tickers"
quoteCcy = "USDT"
instId = "-USDT"

okxApiBalance = "https://www.okx.com/api/v5/api/v5/account/balance"


def setWebhook():
    response = requests.get(url + "/setWebhook?url=" + webAppUrl).json()
    print("SetWebhook ", response)
    return response


def sendText(id, text):
    response = requests.get(url + "/sendMessage?chat_id=" + id + "&text=" + urllib.parse.quote(text)).json()
    print(response)
    return response


def price_okx_api(coin_name):
    params = {'quoteCcy': 'USDT', 'instId': str(coin_name + '-USDT').upper()}
    coin_price = requests.get(URL_OKX, params=params).json()
    if coin_price['code'] == '51001':
        return None
    return float(coin_price['data'][0]["idxPx"])


# def login(apiKey, passphrase, timestamp, secretKey):
#     temp = cCryptoGS.HmacSHA256(timestamp + 'GET' + '/users/self/verify', secretKey);
#     print(temp)
#     sign = cCryptoGS.enc.Base64.stringify(cCryptoGS.HmacSHA256(timestamp + 'GET' + '/users/self/verify', secretKey));
#
#     myHeaders = {
#         "apiKey": apiKey,
#         "passphrase": passphrase,
#         "timestamp": timestamp,
#         "sign": sign
#     }
#
#     myOptions = {
#         'method': 'GET',
#         'headers': myHeaders
#     }
#
#     response = UrlFetchApp.fetch(okxApiBalance, myOptions)
#     print(response)


# login("15de4839-7041-4be6-bc3b-084ff25a4077", "Headofsergo16$", dateString, "8586E6157E565D8A8F949FAB9A3890FE")

def doPost(e):
    cont = requests.get(e.postData.contents).json()
    coin_name = str(cont['message']["text"]).upper()
    id = cont["message"]["from"]["id"]

    answer = price_okx_api(coin_name)
    sendText(id, coin_name + " on OKX " + str(answer))






















