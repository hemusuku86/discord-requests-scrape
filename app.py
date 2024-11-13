import tls_client
from flask import Flask

app = Flask(__name__)

@app.route("/mailtest")
def mailtest():
  s = tls_client.Session(
    client_identifier="chrome120",
    random_tls_extension_order=True
  )

app.run()
