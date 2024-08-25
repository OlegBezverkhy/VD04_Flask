from flask import Flask
from datetime import datetime as dt

app = Flask(__name__)

@app.route("/")
def curent_time():
    return f'Текущая дата :   {dt.now().date():%d/%m/%Y}<br>Текщее время:  ' \
           f'{dt.now().time():%H:%M:%S}'

if __name__ == '__main__':
    app.run()

