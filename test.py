from flask import Flask, request
app = Flask(__name__)

@app.route('/hello')
def hello():
    a = "Вы не ввели длину стороны куба"
    if "a" in request.args:
        if request.args['a']!="" and int(request.args['a'])>0:
            b=int(request.args['a'])
            b = b**3
            a = "Объем куба - {}!".format(b)

    return """
    <html>
        <body>
        <div style="">
            <p style="text-align:center; font-size: 120%; font-family: monospace; color: #cd66cc">{}</p>

            <form action='/hello' method='GET'>
               <p style="text-align:center; font-size: 120%; font-family: monospace; color: #cd66cc"; margin: 20px 150px > Длина стороны куба (a): <input type="number" style="margin: 30px 120px" name="a" /><br>
                <input type="submit" style="margin: 30px 120px; width: 300px;height: 100px; background-color:#fd6bdc"" value="Рассчитать" /></p>
        </div>
            </form>
        </body>
    </html>
    """.format(a)

app.run(debug=True, port=8080)