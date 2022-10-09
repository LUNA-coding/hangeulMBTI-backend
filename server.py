from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
from pytz import timezone


app = Flask(__name__)
CORS(app)

cred = credentials.Certificate('firebase-adminkey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://hangeul-mbti-default-rtdb.asia-southeast1.firebasedatabase.app' 
})



@app.route("/")
def hello():
	return "본 API는 GET 형식 요청을 받지 않습니다."

@app.route('/', methods=['POST'])
def main():
    nowTime = datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')
    
    requestData = request.json
    phoneNum = requestData['phoneNum']

    ref = db.reference('phoneNumList')
    ref.update({nowTime: phoneNum})

    
    return jsonify({"phoneNum": phoneNum}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)