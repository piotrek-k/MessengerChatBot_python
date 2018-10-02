# MessengerChatBot
Example of Facebook Messenger Bot based on 
[official tutorial](https://developers.facebook.com/docs/messenger-platform/getting-started/quick-start)
 but written in Python

## Tasks:

[*] [Facebook app setup](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup)

[*] [How webhook (API in Python from this repo) should be done and tested](https://developers.facebook.com/docs/messenger-platform/getting-started/webhook-setup)

[*] [Images, postbacks](https://developers.facebook.com/docs/messenger-platform/getting-started/quick-start)

[*] Automatic tests

## Usage
Flask setup:
```
export FLASK_APP=hello.py
flask run
```
(`set` instead of `export` on Windows)

Tests:
```
pytest
```
It also requires to create `secrets.py` where Facebook token will be stored.
`secrets.py` is not pushed to git repo since it contains sensitive infomation.

`PAGE_ACCESS_TOKEN` global variable for FB Page token.

## Data

Here is what is sent to `\webhook` (POST), when someone writes a message to Facebook Page:
```
{
   'id':'[number]',
   'time':1538421274715,
   'messaging':[
      {
         'sender':{
            'id':'[number]'
         },
         'recipient':{
            'id':'[number]'
         },
         'timestamp':1538421274284,
         'message':{
            'mid':'[string]',
            'seq':855684,
            'text':'[typed text]'
         }
      }
   ]
}
```

Running `flask run` will create local server. Use ngrok (in `tools` folder) to expose it to internet.
Then configure it in `Webhooks` subpage (developers.facebook.com/apps/appid/webhooks/)