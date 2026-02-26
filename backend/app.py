from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="biblioteca",
    user="admin",
    password="admin"
)

@app.route('/libros', methods=['GET'])
def obtener_libros():
    cur = conn.cursor()
    cur.execute("SELECT * FROM libros;")
    libros = cur.fetchall()
    cur.close()
    return jsonify(libros)

@app.route('/buscar', methods=['GET'])
def buscar_por_autor():
    autor = request.args.get('autor')
    cur = conn.cursor()
    cur.execute("SELECT * FROM libros WHERE autor = %s;", (autor,))
    resultados = cur.fetchall()
    cur.close()
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)