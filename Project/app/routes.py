from app import app

@app.route('/')
@app.route('/all')
def all():
    return "My website: "

