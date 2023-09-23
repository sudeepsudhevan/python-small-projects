from flask import Flask

app = Flask(__name__)

print(__name__)


def make_bold(function):
    def wrapper_function():
        value = function()
        return f'<b>{value}</b>'
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        # return "<em>" + function() + "</em>"
        return f'<em>{function()}</em>'
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        value = function()
        return f'<u>{value}</u>'
    return wrapper_function


@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>this is something </p>'
            '<div style="width:100%;height:0;padding-bottom:63%;position:relative;">'
            '<iframe src="https://giphy.com/embed/3VYPZv5zVPg9ylvIrG" width="100%" height="100%" '
            'style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>'
            )


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello is this {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
