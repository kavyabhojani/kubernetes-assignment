from flask import Flask, request, jsonify
import os

app = Flask(__name__)
PV_DIR = "/kavya_PV_dir/"

@app.route('/store-file', methods=['POST'])
def store_file():
    data = request.get_json()
    file_name = data.get("file")
    content = data.get("data")
    
    if not file_name:
        return jsonify({"file": None, "error": "Invalid JSON input."})

    file_path = os.path.join(PV_DIR, file_name)
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return jsonify({"file": file_name, "message": "Success."})
    except Exception as e:
        return jsonify({"file": file_name, "error": str(e)})

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    file_name = data.get("file")
    product = data.get("product")

    if not file_name:
        return jsonify({"file": None, "error": "Invalid JSON input."})

    file_path = os.path.join(PV_DIR, file_name)
    try:
        total = 0
        with open(file_path, 'r') as file:
            for line in file.readlines():
                prod, amount = line.split(',')
                if prod.strip() == product:
                    total += int(amount.strip())
        return jsonify({"file": file_name, "sum": total})
    except FileNotFoundError:
        return jsonify({"file": file_name, "error": "File not found."})
    except Exception as e:
        return jsonify({"file": file_name, "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
