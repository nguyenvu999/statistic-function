from flask import Flask, request, jsonify
from flask_cors import CORS  # Import flask_cors
import statistics
from scipy import stats

app = Flask(__name__)

# Cấu hình CORS chỉ cho phép từ port 4200
CORS(app)

# Endpoint to calculate arithmetic mean
@app.route('/api/mean', methods=['POST'])
def mean():
    data = request.json
    try:
        result = statistics.mean(data['numbers'])
        return jsonify({'mean': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint to calculate floating-point mean
@app.route('/api/fmean', methods=['POST'])
def fmean():
    data = request.json
    try:
        result = statistics.fmean(data['numbers'])
        return jsonify({'fmean': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint to calculate geometric mean
@app.route('/api/geometric_mean', methods=['POST'])
def geometric_mean():
    data = request.json
    try:
        result = statistics.geometric_mean(data['numbers'])
        return jsonify({'geometric_mean': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint to calculate harmonic mean
@app.route('/api/harmonic_mean', methods=['POST'])
def harmonic_mean():
    data = request.json
    try:
        result = statistics.harmonic_mean(data['numbers'])
        return jsonify({'harmonic_mean': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint to calculate median
@app.route('/api/median', methods=['POST'])
def median():
    data = request.json
    try:
        result = statistics.median(data['numbers'])
        return jsonify({'median': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint to calculate low median
@app.route('/api/median_low', methods=['POST'])
def median_low():
    data = request.json
    try:
        result = statistics.median_low(data['numbers'])
        return jsonify({'median_low': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint to calculate high median
@app.route('/api/median_high', methods=['POST'])
def median_high():
    data = request.json
    try:
        result = statistics.median_high(data['numbers'])
        return jsonify({'median_high': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint to calculate mode
@app.route('/api/mode', methods=['POST'])
def mode():
    data = request.json
    try:
        result = statistics.mode(data['numbers'])
        return jsonify({'mode': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint to calculate variance
@app.route('/api/variance', methods=['POST'])
def variance():
    data = request.json
    try:
        result = statistics.variance(data['numbers'])
        return jsonify({'variance': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint to calculate standard deviation
@app.route('/api/stdev', methods=['POST'])
def stdev():
    data = request.json
    try:
        result = statistics.stdev(data['numbers'])
        return jsonify({'stdev': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint to perform linear regression
@app.route('/api/linear_regression', methods=['POST'])
def linear_regression():
    data = request.json
    try:
        x = data['x']
        y = data['y']
        if len(x) != len(y):
            raise ValueError("x and y must have the same length")
        
        # Sử dụng scipy để tính toán hồi quy tuyến tính
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        return jsonify({'slope': slope, 'intercept': intercept})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

