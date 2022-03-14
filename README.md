# Soccer-Automated-Alerts
Automated alerts and emails for soccer data

<h2>How does it work?</h2>
The program uses a RapidAPI endpoint (https://api-football-v1.p.rapidapi.com/v3/fixture) to get fixtures for the current day. It then converts the JSON repsonse into a readable HTML table, and sends that to the desired email via Gmail. Currently the program only retrieves Premier League games.

<h2>Example config.py</h2>

```python
api_host = "api-football-v1.p.rapidapi.com"
api_key = "your_key_here"
sender = "your_sender_email@gmail.com"
sender_creds = "your_sender_password"
receiver = "your_receiver_email@example.com"
```
