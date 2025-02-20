from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,FieldList,RadioField,IntegerField,EmailField,SelectField,DateField
from wtforms import validators,EmailField
from wtforms import Form, StringField, DateField, RadioField, validators


class UserForm(Form):
    matricula=StringField('Matricula',[validators.DataRequired(message='El campo es requerido'),
    validators.length(min=3,max=10, message='El campo debe temer entre 3 y 10 caracteres')
                                       ])
    nombre=StringField('Nombre',[validators.DataRequired(message='El campo es requerido')])
    apellido=StringField('Apellido',[validators.DataRequired(message='El campo es requerido')])
    email=EmailField('email',[validators.Email(message="Ingrese un correo valido")])
    
"""
Codigo para practica del zodiaco
"""

class UserForm(Form):
    nombre = StringField('Nombre', [validators.DataRequired(message='El campo es requerido')])
    apellidoMa = StringField('Apellido Materno', [validators.DataRequired(message='El campo es requerido')])
    apellidoPa = StringField('Apellido Paterno', [validators.DataRequired(message='El campo es requerido')])
    fechaNacimiento = DateField('Fecha de Nacimiento', format='%Y-%m-%d', validators=[validators.DataRequired(message='El campo es requerido')])
    sexo = RadioField('Sexo', choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], validators=[validators.DataRequired(message='El campo es requerido')])