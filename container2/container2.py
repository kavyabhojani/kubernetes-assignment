import os
import csv
from flask import Flask, request, jsonify

app = Flask(__name__)
PV_DIR = "/kavya_PV_dir/"

@app.route('/sum', methods=['POST'])
def sum_product():
    data = request.get_json()
    file_name = data.get("file")
    product = data.get("product")

    if not file_name:
        return jsonify({"file": None, "error": "Input file not in CSV format."})

    if not file_name.endswith('.csv'):
        return jsonify({"file": file_name, "error": "Input file not in CSV format."})

    file_path = os.path.join(PV_DIR, file_name)
    try:
        total = 0
        is_empty = True
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                is_empty = False
                if len(row) != 2:
                    return jsonify({"file": file_name, "error": "Input file not in CSV format."})
                if row[0].strip() == product:
                    total += int(row[1].strip())

        if is_empty:
            return jsonify({"file": file_name, "error": "Input file not in CSV format."})

        if total == 0:
            return jsonify({"file": file_name, "error": "Input file not in CSV format."})

        return jsonify({"file": file_name, "sum": total})
    except FileNotFoundError:
        return jsonify({"file": file_name, "error": "File not found."})
    except Exception as e:
        return jsonify({"file": file_name, "error": str(e)})

if __name__ == '__main__':
    app.json.sort_keys = False
    app.run(host='0.0.0.0', port=5001)
