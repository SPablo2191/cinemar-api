from flask import Blueprint,jsonify,request
from resources.home import get_db
from database.models.Descuento import Descuento
discounts = Blueprint('discounts',__name__)
table = 'Descuento'
@discounts.route('/discounts', methods=['GET'])
def get_discounts():
    rows = get_db().select(table)
    return jsonify(get_array_json(rows))

@discounts.route('/discounts/days', methods=['GET'])
def get_discount_day():
    day = normalize(request.args.get('day'))
    rows = get_db().select(table,'*',f"where dia like '{day}'")
    return jsonify(get_array_json(rows)[0])


@discounts.route('/discounts', methods=['POST'])
def add_discounts():
    data = dict(request.get_json())
    print(data)
    newDiscount = Descuento(data['dia'],porcentaje=data['porcentaje'],descripcion=data['descripcion'])
    newTupleDiscount = newDiscount.__iter__(newDiscount.dia,newDiscount.porcentaje,newDiscount.descripcion,newDiscount.estado)
    get_db().insert(newDiscount,[newTupleDiscount])
    aux = get_db().select(table)
    return jsonify(aux),200


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def get_array_json(rows):
    discounts = []
    for row in rows:
        discount = Descuento(row[1],row[2],row[3],bool(row[4]),row[0]).__dict__
        discounts.append(discount)
    return discounts