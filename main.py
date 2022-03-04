import requests
import config
import datetime
import smtplib
import json

# Determine what season year we are in
todays_date = datetime.date.today().strftime("%Y-%m-%d")
if datetime.date.today().strftime("%m") < "9":
    season_year = int(datetime.date.today().strftime("%Y")) - 1
else:
    season_year = datetime.date.today().strftime("%Y")

# Pull data from the config file
headers = {
    'x-rapidapi-host': config.api_host,
    'x-rapidapi-key': config.api_key
    }
email_sender = config.email_sender
email_sender_pw = config.email_sender_pw
email_receiver = config.email_receiver

# Fixtures endpoint and query setup
fixtures_url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
fixtures_querystring = {"date":"2022-03-06","league":"39","season":season_year}
#prod: fixtures_querystring = {"date":todays_date,"league":"39","season":year}

def send_email(message_text):
    message_text = "\n" + message_text
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(email_sender, email_sender_pw)
        server.sendmail(email_sender, email_receiver, message_text)         
        print("Successfully sent email")
        server.quit()
    except:
        print("Error: unable to send email")

def main():
    response = requests.request("GET", fixtures_url, headers=headers, params=fixtures_querystring)

    send_email(response.text)

if __name__ == "__main__":
    main()

'''"id":39,"name":"Premier League"'''
'''"league":{"id":2,"name":"UEFA Champions League","type":"Cup"'''
'''2021-01-29'''