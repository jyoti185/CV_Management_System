import json
def TextMessage(message,contactno):
    import requests

    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization": "TgA3oj8L9DPCYUBaVF2rkOuvXZcse0n6yS7qtfWmbh5l1MKiNJRb7eC3P4FalQ8TGN1XuxhyZK5zsJnH",
                   # "sender_id": "FastSM",
                   "message": message,
                   "language": "english",
                   "route": "q",
                   "numbers": contactno}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    json_data=(response.text)
    d1=json.loads(json_data)
    return d1['return']



