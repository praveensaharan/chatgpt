from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import os
import openai
from config import API_KEY, MONGO_URI

openai.api_key = os.getenv(API_KEY)




app = Flask(__name__)

app.config["MONGO_URI"] = MONGO_URI
mongo =PyMongo(app)

@app.route('/')
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html",myChats=myChats)

@app.route("/api",methods=["GET","POST"])
def qa():
    if request.method=="POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question":question})
        if chat:
            data = {"question":question,"answer": f"{chat['answer']}"}
            return jsonify(data)
        else:
            
            # response = openai.Completion.create(
            #     model="text-davinci-003",
            #     prompt=question,
            #     temperature=1,
            #     max_tokens=256,
            #     top_p=1,
            #     frequency_penalty=0,
            #     presence_penalty=0
            #     )
            data ={"question":question,"answer":"Sorry I have no response"}
            # mongo.db.chats.insert_one({"question":question,"answer":response["choices"][0]["text"]})
            return jsonify(data)
    data ={"answer":"Thank you! I'm just a machine learning model designed to respond to questions and generate text based answer"}
    return jsonify(data)

app.run(debug=True)