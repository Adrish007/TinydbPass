import flask
from flask import request
from tinydb import TinyDB,Query
db = TinyDB('db.json')

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        App = request.form["App"]
        user = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        db.insert({"App":App,"username":user,"email":email,"password":password})
    resp = db.all()
    parameter = request.args.get("name")
    if not parameter:
        return {"response": resp}
    query = Query()
    resp2 = db.search(query.App==parameter)
    return {"response":resp2}

@app.route('/delete', methods=['GET'])
def handle_delete():
   parameter = request.args.get("name")
   query = Query()
   Remove = db.remove(query.App==parameter)
   if db.search(query.App==parameter) ==[] :
       return "Not Found"
   else:
     return "Delete Successful"


if __name__=="__main__":
  app.run(debug=True)