#All using Embed code for python

from discord_hooks import Webhook

#url = open('https://discordapp.com/api/webhooks/458305610035888128/iSYSr2jiIk45lmJLSZ7HRjvt3QIvbdYH_q2DQz0hy9Sdz5MIIeS9WXZD-5jst5LrIad-').read()
url = 'https://discordapp.com/api/webhooks/458305610035888128/iSYSr2jiIk45lmJLSZ7HRjvt3QIvbdYH_q2DQz0hy9Sdz5MIIeS9WXZD-5jst5LrIad-'
embed = Webhook(url, color=0x00FF00, msg='Push status : Successful')
# 'text' = make it different font
# __text__ = make it underline
# **text** = make it bold
# *text* = make it italic
# ~~text~~ = make it crossline
#U0001f603 is emoji

#Refer to example if wanted to change

embed.set_author(name='Adidas',icon='https://i.imgur.com/rdm3W9t.png', url='https://www.adidas.com.au/ultraboost-parley-ltd-shoes/BB7076.html?pr=home_rr&slot=2') #Name of the brand?
embed.set_title(title='Ultraboost Parley LTD', url='https://www.adidas.com.au/ultraboost-parley-ltd-shoes/BB7076.html?pr=home_rr&slot=2') #Name of the shoe?
#embed.set_desc("this description supports [named links](https://discordapp.com) as well. ```\nyes, even code blocks```")
embed.add_field(name="SKU Number / Content : ", value="BB7076",inline=False) #SKU?
embed.add_field(name="Size: ", value="Put Size here", url="https://www.google.com/" ,inline=False) # Put add to cart links?
##embed.add_field(name="Field 3 🙄", value="Jokes, dont do that.",inline=False)
##embed.add_field(name="Field 4 🙄", value="these last two")
##embed.add_field(name="Field 5 🙄", value="are inline fields")
embed.set_thumbnail('https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcTNIgkTa9sYVSpxMvtEsQRzS9wcsRw5vBiVi-aTXALpQDMwOwzUkzKO3xrg5kwdVLGzqxlYtuU&usqp=CAc')
##embed.set_image('https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcTNIgkTa9sYVSpxMvtEsQRzS9wcsRw5vBiVi-aTXALpQDMwOwzUkzKO3xrg5kwdVLGzqxlYtuU&usqp=CAc')
embed.set_footer(text='Time Stamp : ',ts=True)

embed.post()




