from flask import Flask
from flask import jsonify

app = Flask(__name__)

users = [
    {
        "id" : "taebinjjang",
        "pw" : "taebin0831"
    },
    {
        "id" : "habinjjang",
        "pw" : "habin0220"
    }
]

@app.route('/view/<id>')
def view(id):
    for user in users:
        if user["id"] == id:
            return jsonify(user)


@app.route('/signup/<id>/<pw>')
def signup(id,pw):
    for user in users:
        if user["id"] == id:
            return "already id"
        users.append(
            {
                "id" : id,
                "pw" : pw
            }
        )


if __name__ == '__main__':
    app.run()
