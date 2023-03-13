from database import db as database
from flask import Flask, render_template, url_for, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, instance_relative_config=True)
from sqlalchemy.dialects import registry
from models import Agente
from forms import AgenteForm
from werkzeug.utils import redirect


# config db
DATABASE = 'test_db'
USERNAME = 'postgres'
PASSWORD = 'DILEN23536asd'
HOST = '127.0.0.1'

# FLASK_APP="SapFlask/app.py"

FULL_URL=f'postgresql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}'
# CONFIG FLASK-WTF
app.config['SECRET_KEY']="ASDOIJAOSIDJ"
app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



database.init_app(app)
migrate = Migrate()
migrate.init_app(app, database)






@app.route('/')
@app.route('/index') 
@app.route('/index.html')
def start():
    # listado de personas
    # p = Agente.query.all()
    p = Agente.query.order_by('id')
    totalp = Agente.query.count()
    app.logger.debug(f"agentes {p}")
    # es una tupla no un diccionario
    return render_template('index.html', p=p, totalp=totalp)


@app.route('/ver/<int:id>')
def ver_detalle(id):
    # listado de personas
    aget = Agente.query.get_or_404(id)
    app.logger.debug(f"agentes {aget}")
    # es una tupla no un diccionario
    return render_template('agente_detalle.html', aget=aget)


# flask-wtf para trabajar los formularios
@app.route('/agregar', methods=["GET", "POST"])
def agregar_agente():
    newAgent = Agente()
    form = AgenteForm(obj = Agente())
    if request.method == "POST":
        if form.validate_on_submit():
            form.populate_obj(newAgent)
            app.logger.debug(f"isertado {newAgent}")
            # agregar un nuevo registro
            database.session.add()
            database.session.commit()
            return redirect(url_for("start"))
    return render_template('agregar_agente.html', form=form)


@app.route('/editar/<int:id>', methods=["GET", "POST"])
def editar_agente(id):
    editAgent = Agente.query.get_or_404(id)
    form = AgenteForm(obj = editAgent())
    if request.method == "POST":
        if form.validate_on_submit():
            form.populate_obj(editAgent)
            app.logger.debug(f"editado: {editAgent}")
            # guardar el registro
            database.session.commit()
            return redirect(url_for("start"))
    return render_template('editar_agente.html', form=form)


@app.route('/eliminar/<int:id>')
def eliminar_agente(id):
    deleteAgent = Agente.query.get_or_404(id)
    app.logger.debug(f"editado: {deleteAgent}")
    database.session.delete()
    database.session.commit()
    return redirect(url_for("start"))