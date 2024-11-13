import tls_client
from flask import Flask, request

app = Flask(__name__)

@app.route("/mailtest")
def mailtest():
  s = tls_client.Session(
    client_identifier="chrome120",
    random_tls_extension_order=True
  )
  mail = request.args.get("addr")
  s.headers = {
  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "sec-fetch-site": "none",
  "accept-encoding": "gzip, deflate, br",
  "sec-fetch-mode": "navigate",
  "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1",
  "accept-language": "ja",
  "referer": "https://www.google.com/",
  "sec-fetch-dest": "document"
  }
  r = s.get("https://support.discord.com/hc/en-us/requests/new")
  print(r.status_code)
  form_id = r.text.split("https://support.discord.com/hc/en-us/requests/new?ticket_form_id=")[1].split('"')[0]
  print(form_id)
  csrf = s.get("https://support.discord.com/hc/api/internal/csrf_token.json").json()["current_session"]["csrf_token"]
  print(csrf)
  s.headers["x-csrf-token"] = csrf
  r = s.post("https://support.discord.com/hc/en-us/requests",  data={
  "utf8": "%E2%9C%93",
  "request[ticket_form_id]": form_id,
  "request[anonymous_requester_email]": mail,
  "request[custom_fields][360011846391]": "us_support_general",
  "request[subject]": "A bot is nuking server",
  "request[description]": "761562078095867916 user id",
  "request[description_mimetype]": "text/plain",
  "authenticity_token": csrf
  })
  print(r.status_code)
  return "ok"

app.run()
