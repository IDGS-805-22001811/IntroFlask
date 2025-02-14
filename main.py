from flask import Flask, render_template, request
import forms

app=Flask(__name__)

@app.route("/")
def index():
    titulo="IDGS805"
    lista=["Pedro,Juan,Mario"]
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route("/alumnos",methods=["GET","POST"])
def alumnos():
    mat=''
    nom=''
    ape=''
    email=''
    alumno_clase=forms.UserForm(request.form)
    if request.method=="POST":
        mat=alumno_clase.matricula.data
        ape=alumno_clase.apellido.data
        nom=alumno_clase.nombre.data
        email=alumno_clase.email.data
    print('Nombre: {}'.format(nom))
    return render_template("alumnos.html",form=alumno_clase)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")


@app.route("/Hola")
def hola():
    return "<h1>Hola mundooo</h1>"


@app.route("/user/<string:user>")
def user(user):
    return f"hola,{user}"

@app.route("/numero/<int:n>")
def numero(n):
    return f"El numeri es: {n}"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"El usuario es: {username} con id: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"La suma es: {n1+n2}"

@app.route("/default/")
@app.route("/default/<string:tem>")
def func1(tem='Juan'):
    return f"Hola, {tem}"

@app.route("/form1")
def form1():
    return '''
            <form>
            <label for="nombre">Nombre:</label>
            </form>
    
           '''

@app.route("/OperasBas", methods=["GET", "POST"])
def operas():
    resultado = None
    n1 = None
    n2 = None
    operacion = None

    if request.method == "POST":
        n1 = int(request.form.get("n1"))
        n2 = int(request.form.get("n2"))
        operacion = request.form.get("operacion")

        if operacion == "suma":
            resultado = n1 + n2
        elif operacion == "resta":
            resultado = n1 - n2
        elif operacion == "multiplicacion":
            resultado = n1 * n2
        elif operacion == "division":
            if n2 != 0:
                resultado = n1 / n2
            else:
                resultado = "Error: No se puede dividir por cero."

    return render_template("OperasBas.html", resultado=resultado, n1=n1, n2=n2, operacion=operacion)

"""
@app.route("/resultado", methods=["GET", "POST"])
def resul():
    if request.method == "POST":
        num1 = int(request.form.get("n1"))
        num2 = int(request.form.get("n2"))
        operacion = request.form.get("operacion")

        if operacion == "suma":
            resultado = num1 + num2
            operacion_texto = "suma"
        elif operacion == "resta":
            resultado = num1 - num2
            operacion_texto = "resta"
        elif operacion == "multiplicacion":
            resultado = num1 * num2
            operacion_texto = "multiplicación"
        elif operacion == "division":
            if num2 != 0:
                resultado = num1 / num2
                operacion_texto = "división"
            else:
                return "Error: No se puede dividir por cero."
        else:
            return "Error: Operación no válida."

        return "La {} de {} y {} es {}".format(operacion_texto, num1, num2, resultado)
"""
class Cine:
    def __init__(self):
        self.registros = []

    def calcular_descuento(self, boletos_comprados):
        if boletos_comprados > 7:
            return 0.15
        elif 3 <= boletos_comprados <= 5:
            return 0.10
        else:
            return 0

    def calcular_total(self, boletos_comprados, tarjeta):
        precio = 12.000
        descuento = self.calcular_descuento(boletos_comprados)
        sin_descuento = boletos_comprados * precio
        con_descuento = sin_descuento * descuento
        total = sin_descuento - con_descuento
        if tarjeta == 'si':
            total = sin_descuento - (total * 0.10)
        return total

cine_instancia = Cine()

@app.route("/cinepolis", methods=["GET", "POST"])
def cine():
    pago = None
    error = None
    nombre = None
    compradores = None
    tarjeta = None
    boletos = None

    if request.method == "POST":
        nombre = request.form.get("nombre")
        compradores = request.form.get("compradores")
        boletos = request.form.get("boletos")
        tarjeta = request.form.get("tarjeta")

        if not nombre or not compradores or not boletos or not tarjeta:
            error = "Todos los campos son obligatorios."
        else:
                compradores = int(compradores)
                boletos = int(boletos)
                max_boletos = compradores * 7

                if boletos > max_boletos:
                    error = "Has excedido el límite permitido de boletos. Máximo permitido: {}.".format(max_boletos)
                else:
                    total = cine_instancia.calcular_total(boletos, tarjeta)
                    pago = total
    
    return render_template("cinepolis.html", pago=pago, error=error, nombre=nombre, compradores=compradores, tarjeta=tarjeta, boletos=boletos)


if __name__=="__main__":
    app.run(debug=True,port=3000)