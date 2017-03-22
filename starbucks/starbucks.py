from flask import Flask
from flask import render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("test.html")

language = {
    "Ko" : {
        "americano" : "아메라카노",
        "latte" : "라떼",
        "javachip" : "자바칩",
        "chcobanana" : "초코바나나"
    },
    "Us" : {
        "americano" : "americano",
        "latte" : "latte",
        "javachip" : "javachip",
        "chcobanana" : "chcobanana"
    }
}




def search():
    r = requests.get("http://naver.com")
    soup = BeautifulSoup(r.text,"html.parser")

    keyword = [

    ]

    datas = soup.find(id="realtimeKeywords").ol.find_all('li')
    for data in datas:
        keyword.append(
            data.a.find("span", {"class": "ell"}).string
        )
    return keyword


@app.route('/<name>')
def hello_name(name):
    return render_template("test.html",name=name)

@app.route('/welcome/<country>')
def welcome(country):
    keywords = search()
    return render_template("welcome.html",language=language,country=country,keywords=keywords)


if __name__ == '__main__':
    app.run()
