from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
from conexion.conexion import obtener_conexion

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class Usuario(UserMixin):
    def __init__(self, id, nombre, email, password):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password


@login_manager.user_loader
def cargar_usuario(usuario_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_usuario, nombre, email, password FROM usuarios WHERE id_usuario = %s", (usuario_id,))
        usuario = cursor.fetchone()
    conexion.close()
    if usuario:
        return Usuario(*usuario)
    return None


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)",
                           (nombre, email, password))
            conexion.commit()
        conexion.close()
        flash('Registro exitoso, ahora puedes iniciar sesión', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id_usuario, nombre, email, password FROM usuarios WHERE email = %s", (email,))
            usuario = cursor.fetchone()
        conexion.close()

        if usuario and check_password_hash(usuario[3], password):
            user_obj = Usuario(*usuario)
            login_user(user_obj)
            return redirect(url_for('dashboard'))
        flash('Correo o contraseña incorrectos', 'danger')
    return render_template('login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return f'Bienvenido {current_user.nombre}, esta es tu área privada.'


@app.route('/logout')
def logout():
    logout_user()
    flash('Sesión cerrada', 'info')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
