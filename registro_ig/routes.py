from registro_ig import app


@app.route("/")
def index():
    return "Flask con js"
