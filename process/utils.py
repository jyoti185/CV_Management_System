import json
def TextMessage(message,contactno):
    import requests

    url = "https://www.fast2sms.com/dev/bulk"

    querystring = {"authorization": "",
                   "sender_id": "FSTSMS",
                   "message": message,
                   "language": "english",
                   "route": "p",
                   "numbers": contactno}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    json_data=(response.text)
    d1=json.loads(json_data)
    return d1['return']