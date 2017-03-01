from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello Flask"


@app.route("/test/<search_query>")
def search(search_query):
    return search_query


@app.route("/integer/<int:value>")
def int_type(value):
    value = value + 1
    print(value)
    return str(value)


@app.route("/float/<float:value>")
def flaot_type(value):
    value = value + 1
    print(value)
    return str(value)


@app.route("/name/<name>")
def index(name):
    if name.lower() == "accion":
        return "Hello, {}".format(name), 200
    else:
        return "Not found", 404


if __name__ == "__main__":
    app.run()
