import json
def TextMessage(message,contactno):
    import requests

    url = "https://www.fast2sms.com/dev/bulk"

    querystring = {"authorization": "IQRhfs7vrXVmWCZP2LMnlN8yHAizbexoqSt3d4YBKaOkwJEpTcrb4GVwfNs6gBmWPA0uEovKdkY9yXLh",
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