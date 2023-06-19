from flask import Flask, request, render_template, jsonify
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
        requestParametes["xRedirectURL"] = "https://bbpos.cardknox.link/results"
    else:
        requestParametes["xRedirectURL"] = requestParametes["xredirecturl"]
        del requestParametes["xredirecturl"]
    if "xkey" in requestParametes:
        requestParametes["xKey"] = requestParametes["xkey"]
        del requestParametes["xkey"]
    if "xamount" in requestParametes:
        requestParametes["xAmount"] = requestParametes["xamount"]
        del requestParametes["xamount"]
    if "xcommand" in requestParametes:
        requestParametes["xCommand"] = requestParametes["xcommand"]
        del requestParametes["xcommand"]
    newLink = "dck://app.cardknox.com/transaction?" + \
        urllib.parse.urlencode(requestParametes, doseq=True)
    if request.method == "POST":
        return jsonify(redirect=newLink)
    return render_template("index.html", newLink=newLink)


@application.route("/results", methods=["POST", "GET"])
def results():
    resultJson = request.args.to_dict()
    return render_template("results.html", data=resultJson)


# parameters to run with
if __name__ == "__main__":
    application.run(debug=False)
