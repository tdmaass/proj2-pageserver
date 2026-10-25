from flask import Flask, send_from_directory
import config
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker demo!"

@app.route("/<path:filename>")
def respond(filename):

    root = os.path.realpath(DOCROOT)

    path = os.path.realpath(os.path.join(root, filename))
    print("Requested filename:", filename, flush=True)
    print("DOCROOT:", root, flush=True)
    print("Looking for:", path, flush=True)
    print("File exists:", os.path.isfile(path), flush=True)
    sameDir = (os.path.commonpath([root, path]) == root)

    if ("//" in filename) or ("~" in filename) or (".." in filename):
        return forbidden(None)
    
    if not sameDir:
        return forbidden(None)

    if not filename.endswith((".html", ".css")):
        return not_found(None)

    if not os.path.isfile(path):
        return not_found(None)

    return send_from_directory(DOCROOT, filename)
    

@app.errorhandler(403)
def forbidden(error):
    return send_from_directory(DOCROOT, "403.html"), 403

@app.errorhandler(404)
def not_found(error):
    return send_from_directory(DOCROOT, "404.html"), 404

def get_options():
    options = config.configuration()
    return options


def main():
    global DOCROOT
    options = get_options()
    assert options.DOCROOT, "Document root must be specified in " \
              + "configuration file credentials.ini or on command line"
    DOCROOT = options.DOCROOT
    

if __name__ == "__main__":
    main()
    app.run(debug=True, host='0.0.0.0')
