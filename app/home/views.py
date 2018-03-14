from .import home


@home.route("/")
def index():
    return "<h1 style='color:red'>home</h1>"
