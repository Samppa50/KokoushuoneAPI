from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

reservations = []
id_counter = 1

@app.route('/reservations', methods=['POST'])
def create_reservation():
    global id_counter
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    required_fields = ['room', 'start_time', 'end_time', 'user']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400
    
    room = data['room']
    start_str = data['start_time']
    end_str = data['end_time']
    user = data['user']
    
    try:
        start_time = datetime.fromisoformat(start_str)
        end_time = datetime.fromisoformat(end_str)
    except ValueError:
        return jsonify({'error': 'Invalid datetime format. Use ISO format (e.g., 2023-10-01T10:00:00)'}), 400
    
    if start_time >= end_time:
        return jsonify({'error': 'Start time must be before end time'}), 400
    
    if start_time < datetime.now():
        return jsonify({'error': 'Cannot make reservations in the past'}), 400
    
    # Check for overlapping reservations
    for r in reservations:
        if r['room'] == room and r['start_time'] < end_time and r['end_time'] > start_time:
            return jsonify({'error': 'Reservation overlaps with an existing reservation'}), 400
    
    reservation = {
        'id': id_counter,
        'room': room,
        'start_time': start_time,
        'end_time': end_time,
        'user': user
    }
    reservations.append(reservation)
    id_counter += 1
    
    return jsonify({'id': reservation['id'], 'message': 'Reservation created successfully'}), 201


@app.route('/reservations', methods=['GET'])
def get_reservations():
    result = []

    if not reservations:
        return jsonify({'error': 'No reservations found'}), 404
    
    for r in reservations:
        result.append({
            'id': r['id'],
            'room': r['room'],
            'start_time': r['start_time'].isoformat(),
            'end_time': r['end_time'].isoformat(),
            'user': r['user']
        })
    return jsonify(result)


@app.route('/reservations/<room_name>', methods=['GET'])
def get_reservations_by_name(room_name):
    result = []
    for r in reservations:
        if r['room'] == room_name:
            result.append({
                'id': r['id'],
                'room': r['room'],
                'start_time': r['start_time'].isoformat(),
                'end_time': r['end_time'].isoformat(),
                'user': r['user']
            })
        else:
            return jsonify({'error': 'No reservations found for the specified room'}), 404
    return jsonify(result)


@app.route('/reservations/<int:id>', methods=['DELETE'])
def delete_reservation(id):
    global reservations
    for i, r in enumerate(reservations):
        if r['id'] == id:
            reservations.pop(i)
            return jsonify({'message': 'Reservation deleted successfully'}), 200
    return jsonify({'error': 'Reservation not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)