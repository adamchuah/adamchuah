# from discord_hooks import Webhook


# url = open("https://discordapp.com/api/webhooks/333843063069868032/DLW5Ekzp4-GcAi7VSY11urQOI2o9bOko8iQej_Udh4vIAGvtZ_3eOxD54Xca2z5zdsAO").read()

# msg = Webhook(url,msg="Hello there! I'm a webhook \U0001f62e")

# msg.post()
from discord_hooks import Webhook

url = 'https://discordapp.com/api/webhooks/458305610035888128/iSYSr2jiIk45lmJLSZ7HRjvt3QIvbdYH_q2DQz0hy9Sdz5MIIeS9WXZD-5jst5LrIad-'

msg = Webhook(url,msg="Hello there! I'm a webhook \U0001f62e")

msg.post()
