# MessengerChatBot

## Links:

[Facebook app setup](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup)

[How webhook (API in Python from this repo) should be done and tested](https://developers.facebook.com/docs/messenger-platform/getting-started/webhook-setup)

## Data

Here is what is sent to `\webhook` (POST), when someone writes a message to Facebook Page:
```
{
   'id':'1710586375891589',
   'time':1538421274715,
   'messaging':[
      {
         'sender':{
            'id':'1219457681420837'
         },
         'recipient':{
            'id':'1710586375891589'
         },
         'timestamp':1538421274284,
         'message':{
            'mid':'FPMMa04XLIErFjR-6919Jva_nUgD6jp0M100ndezMdU_M11lMACCU7iIF8_0l02SVahVhL7D5nseDN7_n68f4A',
            'seq':855684,
            'text':'************""""'
         }
      }
   ]
}
```

Running `flask run` will create local server. Use ngrok (in `tools` folder) to expose it to internet.
Then configure it in `Webhooks` subpage (developers.facebook.com/apps/appid/webhooks/)