from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = models.db
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = models.Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = models.Hero.query.get(id)
    if hero:
        return jsonify(hero.to_dict_with_powers())
    else:
        return jsonify({'error': 'Hero not found'}), 404

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = models.Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = models.Power.query.get(id)
    if power:
        return jsonify(power.to_dict())
    else:
        return jsonify({'error': 'Power not found'}), 404

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = models.Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404
    data = request.get_json()
    if 'description' not in data:
        return jsonify({'errors': ['Description is required']}), 400
    try:
        power.description = data['description']
        db.session.commit()
        return jsonify(power.to_dict())
    except ValueError as e:
        db.session.rollback()
        return jsonify({'errors': [str(e)]}), 400

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    try:
        hero_power = models.HeroPower(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id']
        )
        db.session.add(hero_power)
        db.session.commit()
        response = hero_power.to_dict_with_power()
        response['hero'] = hero_power.hero.to_dict()
        return jsonify(response), 201
    except (KeyError, ValueError) as e:
        db.session.rollback()
        return jsonify({'errors': [str(e)]}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'errors': ['Invalid hero_id or power_id']}), 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)
