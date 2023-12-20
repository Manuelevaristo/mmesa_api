from mmesa import app
from flask import render_template
from mmesa.models import Client, Equipament


@app.route('/')
def page_home():
    return render_template("home.html")


@app.route('/clientes')
def page_clientes():
    clientLists = Client.query.all()

    return render_template("clientes.html", cliente=clientLists)


@app.route('/equipamentos')
def page_equipamentos():
    equipamentList = Equipament.query.all()

    return render_template("equipamentos.html", equipamento=equipamentList)
