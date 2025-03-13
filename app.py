from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import json
import csv

app = Flask(__name__)
DB_PATH = "database/usuarios.db"
TXT_PATH = "datos/datos.txt"
JSON_PATH = "datos/datos.json"
CSV_PATH = "datos/datos.csv"


# Crear la base de datos y la tabla si no existen
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


init_db()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/formulario')
def formulario():
    return render_template('formulario.html')


@app.route('/guardar', methods=['POST'])
def guardar_datos():
    nombre = request.form['nombre']

    # Guardar en TXT
    with open(TXT_PATH, 'a') as txt_file:
        txt_file.write(nombre + '\n')

    # Guardar en JSON
    try:
        with open(JSON_PATH, 'r') as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append({"nombre": nombre})
    with open(JSON_PATH, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    # Guardar en CSV
    with open(CSV_PATH, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([nombre])

    # Guardar en SQLite
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre) VALUES (?)", (nombre,))
    conn.commit()
    conn.close()

    return render_template('resultado.html', mensaje="Datos guardados correctamente.")


@app.route('/usuarios')
def listar_usuarios():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return jsonify(usuarios)


if __name__ == '__main__':
    app.run(debug=True)
