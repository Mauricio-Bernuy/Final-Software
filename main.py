from tokenize import String
from flask import Flask, Response, request, jsonify
import setuptable 

def create_app():
    app = Flask(__name__)
    return app
    
app = create_app()

@app.route('/createtables', methods=['GET'])
def create():
    setuptable.createtable()
    return jsonify(
        msg="tables created"
    )

@app.route('/droptables', methods=['GET'])
def drop():
    setuptable.droptable()
    return jsonify(
        msg="tables dropped"
    )


@app.route('/message', methods=['POST'])
def msg():
    if request.method == 'POST':
        setuptable.addmessage(request.form['message'], request.form['topic'])
        # if fails catch by exception handler

    return Response(
        "ok",
        status=200,
    )

@app.route('/message/<topic>')
def listmessages(topic=None):
    topic = (topic)

    list = setuptable.getmessagesbytopic(topic)
    
    return jsonify(list)

@app.errorhandler(Exception)
def exception_handler(error):
    return Response(
        "fail",
        status=400,
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)