from flask import Flask, request, redirect
import urllib.parse
from flask_cors import CORS, cross_origin

# declare app
application = Flask(__name__)
CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'


# serve main page
@application.route("/")
@cross_origin()
def index():
    requestParametes = request.args.to_dict()
    set(k.lower() for k in requestParametes)
    print(requestParametes)
    if "xredirecturl" not in requestParametes:
        requestParametes["xredirecturl"] = "https://www.cardknoxdeeplinktest.com/results"
    if "xkey" not in requestParametes:
        requestParametes["xkey"] = "artemisdev12345"
    newLink = "dck://app.cardknox.com/transaction?" + urllib.parse.urlencode(requestParametes, doseq=True)
    print(newLink)
    return redirect(newLink, code=302)

# parameters to run with
if __name__ == "__main__":
    application.run(debug=False)