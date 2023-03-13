from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AgenteForm(FlaskForm):
    nombre = StringField("nombre", validators=[DataRequired()])
    apellido = StringField("apellido")
    email = StringField("email", validators=[DataRequired()])
    send = SubmitField("send")
