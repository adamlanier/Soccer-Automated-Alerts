import requests
import config
import datetime

#changeer
todays_date = datetime.date.today().strftime("%Y-%m-%d")
if datetime.date.today().strftime("%m") < "9":
    season_year = int(datetime.date.today().strftime("%Y")) - 1
else:
    season_year = datetime.date.today().strftime("%Y")

headers = {
    'x-rapidapi-host': config.api_host,
    'x-rapidapi-key': config.api_key
    }

# Fixtures endpoint setup
fixtures_url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
fixtures_querystring = {"date":"2022-03-06","league":"39","season":season_year}
#prod: fixtures_querystring = {"date":todays_date,"league":"39","season":year}

def main():
    response = requests.request("GET", fixtures_url, headers=headers, params=fixtures_querystring)

    print(response.text)


if __name__ == "__main__":
    main()


'''"id":39,"name":"Premier League"'''
'''"league":{"id":2,"name":"UEFA Champions League","type":"Cup"'''
'''2021-01-29'''