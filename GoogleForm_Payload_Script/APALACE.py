import time
import random
import requests
#from faker import Faker
#fake = Faker()
res  = requests.session()

def main(limit):
	for i in range(1, limit):
		url = "https://docs.google.com/forms/d/e/1FAIpQLSez2O2qbqNjXi9EhdymvJFodx11L6cYq1mexT4Cb499WBf_Cw/formResponse" # Request URL

		head = {
				"Referer" : "https://docs.google.com/forms/d/e/1FAIpQLSez2O2qbqNjXi9EhdymvJFodx11L6cYq1mexT4Cb499WBf_Cw/viewform?fbzx=-7772949085126631000"
				}

		r = requests.get(url)

		# user preference

		# sizes   = ["4", "4.5", "5", "5.5", "6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "11.5", "12", "12.5", "13", "13.5", "14"]
		# sex     = ["Male", "Female"]
		# email   = (fake.first_name() + "." + fake.last_name())
		# prefix  = "accessdenied.io"
		# name    = fake.first_name() + fake.last_name()
		# gender  = random.choice(sex)
		# insta   = ("@whereiskeef" + str(random.randint(000, 999)))
		# country = "Australia"
		# state   = "Victoria"
		# city    = "Truganina"
		# size    = random.choice(sizes)
		# emailAd = (email + (str(random.randint(000, 999))) + "@" + prefix)

		emailAd = "mrdeafline@gmail.com"
		print("EMAIL as : %s", emailAd)
		name = "Chuah Weng"
		print("NAME as : %s", name)
		sizes = "UK 9"
		print("Size as : %s", sizes)


		payload = {
				"emailAddress": emailAd,
				"entry.1126176335": name,
				"entry.1082670759": sizes,
				#"entry.797910400": gender,
				# "entry.1663711564": insta,
				# "entry.925071326": country,
				# "entry.77039044": state,
				# "entry.902286662": city,
				"fvv": "1",
				"draftResponse": '[null,null,"-7772949085126631829"]',
				"pageHistory": "0",
				"fbzx": "-7772949085126631829",
				}

		print("Payload is complete \n", payload)
		print("Payload complete")
		print("i = ", i)

		res.post(url, data = payload, headers = head)
		if r.status_code == 200:
			print("[SUCCESS] " + emailAd + " has been successfully entered")
		else:
			print("[ERROR] Something wrong")


if __name__ == "__main__":
	main(2)

