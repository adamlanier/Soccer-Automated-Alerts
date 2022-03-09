import requests, config, datetime, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from json2html import *

def get_season():
    """
    Determine what soccer season we're in. Pre-August is the previous year's season.
    """
    if datetime.date.today().strftime("%m") < "9":
        return int(datetime.date.today().strftime("%Y")) - 1
    return datetime.date.today().strftime("%Y")

def convert_json_to_html(json_input):
    html = json2html.convert(json = json_input, clubbing = "off")
    return html

def send_email(sender, sender_creds, receiver, subject, message_text):

    # Setup the message headers
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver

    print(message_text)
    # Convert the json response to a HTML table we can read
    html = convert_json_to_html(message_text)

    # Attach the line returns and the html body
    plain_text = MIMEText("\n\n", "plain")
    html_body = MIMEText(html, "html")
    message.attach(plain_text)
    message.attach(html_body)

    # Log into the gmail server and send the message
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender, sender_creds)
        server.sendmail(sender, receiver, message.as_string())         
        print("Successfully sent email")
        server.quit()
    except:
        print("Error: unable to send email")

def main():
    # Pull data from the config file
    headers = {
        'x-rapidapi-host': config.api_host,
        'x-rapidapi-key': config.api_key
        }
    sender = config.sender
    sender_creds = config.sender_creds
    receiver = config.receiver

    # Other variable setup
    todays_date = datetime.date.today().strftime("%Y-%m-%d")
    season_year = get_season()
    subject = f"Soccer Email - {todays_date}"

    # Fixtures endpoint and query setup
    fixtures_url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    fixtures_querystring = {"date":"2022-03-12","league":"39","season":season_year}

    # Create request from Rapid API and pass it to our email function
    message = requests.request("GET", fixtures_url, headers=headers, params=fixtures_querystring)
    send_email(sender, sender_creds, receiver, subject, message.text)

if __name__ == "__main__":
    main()
