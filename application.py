from flask import Flask, request, render_template
import urllib.parse
from flask_cors import CORS, cross_origin

# declare app
application = Flask(__name__)
CORS(application)


# serve main page
@application.route("/", methods=["POST", "GET"])
@cross_origin()
def index():
    requestParametes = request.args.to_dict()
    requestParametes = {k.lower(): v for k, v in requestParametes.items()}
    print(requestParametes)
    if "xredirecturl" not in requestParametes:
        requestParametes["xRedirectURL"] = "https://bbpos.cardknox.com"
    else:
        requestParametes["xRedirectURL"] = requestParametes["xredirecturl"]
        del requestParametes["xredirecturl"]
    if "xkey" in requestParametes:
        requestParametes["xKey"] = requestParametes["xkey"]
        del requestParametes["xkey"]
    newLink = "dck://app.cardknox.com/transaction?" + \
        urllib.parse.urlencode(requestParametes, doseq=True)
    print(newLink)
    return render_template("index.html", newLink=newLink)


# parameters to run with
if __name__ == "__main__":
    application.run(debug=False)
