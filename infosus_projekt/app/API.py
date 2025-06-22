from flask import Blueprint, request, jsonify, render_template, redirect
from pony.orm import db_session, select
from baza import IzvjesceKvara
from datetime import datetime
from pony.orm import count

kvar_blueprint = Blueprint('kvarovi', __name__)

@kvar_blueprint.route('/')
@db_session
def index():
    status_filter = request.args.get('status')
    datum_od = request.args.get('od')
    datum_do = request.args.get('do')

    kvarovi = select(k for k in IzvjesceKvara)

    if status_filter:
        kvarovi = kvarovi.filter(lambda k: k.status == status_filter)

    if datum_od:
        datum_od = datetime.strptime(datum_od, "%Y-%m-%d")
        kvarovi = kvarovi.filter(lambda k: k.datum_prijave >= datum_od)

    if datum_do:
        datum_do = datetime.strptime(datum_do, "%Y-%m-%d")
        kvarovi = kvarovi.filter(lambda k: k.datum_prijave <= datum_do)

    return render_template("index.html", kvarovi=kvarovi[:])

@kvar_blueprint.route('/add', methods=['POST'])
@db_session
def add_kvar():
    data = request.form
    IzvjesceKvara(
        title=data['title'],
        opis=data['opis'],
        category=data['category'],
        status='prijavljen',
        prioritet=data['prioritet']
    )
    return redirect('/')

@kvar_blueprint.route('/api/kvarovi')
@db_session
def api_kvarovi():
    kvarovi = select(k for k in IzvjesceKvara)[:]
    return jsonify([k.to_dict() for k in kvarovi])

@kvar_blueprint.route('/api/stats')
@db_session
def stats():
    podaci = select((k.status, count(k)) for k in IzvjesceKvara)[:]
    return jsonify([[status, broj] for status, broj in podaci])
    
@kvar_blueprint.route('/update/<int:kvar_id>', methods=['POST'])
@db_session
def update_kvar(kvar_id):
    novi_status = request.form.get('status')
    kvar = IzvjesceKvara.get(id=kvar_id)
    if kvar:
        kvar.status = novi_status
        return redirect('/')
    return "Kvar nije pronađen", 404
