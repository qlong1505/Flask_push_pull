from flask import Flask, request
api = Flask(__name__)

global ENG_VIET_DICT
ENG_VIET_DICT = {}


@api.route("/")
def hello():
    return "Hello World!"


@api.route("/push")
def Push():
    global ENG_VIET_DICT
    ENG_VIET_DICT["Hello"] = "Xin Chao"
    enWord = request.args.get('en')
    viWord = request.args.get('vi')
    if (enWord == None) or (viWord == None):
        return "No new word"
    else:
        ENG_VIET_DICT[enWord] = viWord
        return "Added word: " + enWord + ":" + viWord


@api.route("/pull")
def Pull():
    global ENG_VIET_DICT
    return ENG_VIET_DICT


if __name__ == "__main__":
    api.run(host='0.0.0.0', port=8123, debug=False)
