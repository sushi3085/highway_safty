import os
from flask import Flask

app = Flask(__name__)

@app.route('/<answer>')
def homepage(answer):
    return f'<h2>Hello {answer}!</h2>'

from flask import request
from flask import jsonify

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

@app.route("/test")
def test():
    from dotenv import load_dotenv

    load_dotenv()
    import os
    import MySQLdb

    connection = MySQLdb.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USERNAME"),
        passwd=os.getenv("PASSWORD"),
        db=os.getenv("DATABASE"),
        ssl_mode="VERIFY_IDENTITY",
        ssl={
            "ca": "/etc/ssl/cert.pem"
        }
    )
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS USER")
    cursor.execute("CREATE TABLE USERS("
                   "IP CHAR(20) NOT NULL"
                   "ACCOUNT CHAR(20) NOT NULL"
                   "PASSWORD CHAR(20) NOT NULL);"
    )
    cursor.execute("Desc Employee;")
    connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))