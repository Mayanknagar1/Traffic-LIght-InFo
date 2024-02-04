from flask import Flask,render_template,request,jsonify
from model import TrafficLight
from db import  db_init,db
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traffic_light.db'
app.config['SQLALCHEMY_TRAK_MODIFICATIONS']=False
db_init(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/traffic_lights', methods=['GET'])
def get_traffic_lights():
    lights = TrafficLight.query.all()
    light_list = [{'id': light.id, 'light_color_work': light.light_color_work, 'color': light.color, 'status': light.status} for light in lights]
    return jsonify(light_list)

@app.route('/api/traffic_lights/<int:light_id>', methods=['GET'])
def get_traffic_light(light_id):
    light = TrafficLight.query.get_or_404(light_id)
    return jsonify({'id': light.id, 'light_color_work': light.light_color_work, 'color': light.color, 'status': light.status})

@app.route('/api/traffic_lights', methods=['POST'])
def create_traffic_light():
    data = request.get_json()
    new_light= TrafficLight(light_color_work=data['light_color_work'], color=data['color'], status=data['status'])
    db.session.add(new_light)
    db.session.commit()
    return jsonify({'id': new_light.id, 'light_color_work': new_light.light_color_work, 'color': new_light.color, 'status': new_light.status}), 201

@app.route('/api/traffic_lights/<int:light_id>', methods=['PUT'])
def update_traffic_light(light_id):
    light = TrafficLight.query.get_or_404(light_id)
    data = request.get_json()
    light.light_color_work = data['light_color_work']
    light.color = data['color']
    light.status = data['status']
    db.session.commit()
    return jsonify({'id': light.id, 'light_color_work': light.light_color_work, 'color': light.color,'status':light.status}),205

@app.route('/api/traffic_lights/<int:light_id>', methods=['DELETE'])
def delete_traffic_light(light_id):
    light = TrafficLight.query.get_or_404(light_id)
    db.session.delete(light)
    db.session.commit()
    return jsonify({'message': 'Traffic light deleted successfully'})

if __name__ == "__main__":
    app.run(debug=True)