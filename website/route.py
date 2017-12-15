from Flask import *
import site

app = Flask(__name__)

@app.route("/")
def launch_session:
    return site.new_session()

@app.route("/<session_id>")
def open_session():

    return site.home_page(bandeau,weapons,user)
