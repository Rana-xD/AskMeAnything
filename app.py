from flask import Flask,jsonify,request,render_template
from wit import Wit
import json

app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/query',methods=['POST'])
def query():
    access_token = "PJUSBTGJ6VXSGG3HERAZEBT3NKKV7JSH"
    query = request.form['search']
    client = Wit(access_token)
    res = client.message(query)
    if(('song' in res['entities']) and ('code' in res['entities']) and ('singer' in res['entities'])):
        result = {"error": 1,"message":"I don't know"}
    elif (('song' in res['entities']) and ('code' in res['entities'])):
        result = searchTuneCode(res["entities"]["song"][0]["value"].lower())
    elif (('song' in res['entities']) and ('singer' in res['entities'])):
        result = searchTuneArtist(res["entities"]["song"][0]["value"].lower())
    else:
        result = {"error": 1,"message":"I don't know"}
    # if('singer' in res['entities']):
    #     return "mean"
    # else:
    #     return "ot mean"
    # i=0
    # for a in res["entities"]:
    #     i+=1
    # if(i<2):
    #     result = {"error": 1,"message":"I don't know"}
    # else:
    #     result = searchTuneCode(res["entities"]["song"][0]["value"].lower())
    return jsonify(result)

def searchTuneCode(title):
    if(title=="peakly"):
        result = {"error":0,"message":"189187","title":title}
    else:
        result = {"error":2,"message":"Calltune not found","title":title}
    return result

def searchTuneArtist(title):
    if(title=="peakly"):
        result = {"error":0,"message":"Tena","title":title}
    else:
        result = {"error":2,"message":"Singer not found","title": title}
    return result

if __name__ == "__main__":
    app.run(debug=True)