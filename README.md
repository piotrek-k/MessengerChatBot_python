# MessengerChatBot

## Tasks:

[*] [Facebook app setup](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup)

[*] [How webhook (API in Python from this repo) should be done and tested](https://developers.facebook.com/docs/messenger-platform/getting-started/webhook-setup)

[*] [Images, postbacks](https://developers.facebook.com/docs/messenger-platform/getting-started/quick-start)

[ ] Automatic tests

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