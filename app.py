import csv
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/search', methods=['POST'])
def search():
    # r = sr.Recognizer()
    # engine = pyttsx3.init()

    search_type = None
    search_term = None
    
    data = request.get_json()
    print(data)
    sType = data['type']
    if 'faculty' in sType.lower():
        search_type = 'Faculty Name'
    elif 'roomno' in sType.lower():
        search_type = 'ROOM NO'
    else:
        return jsonify({'message': 'Invalid search type. Please try again.'})
    
    search_term = data['data']
    print("Search term is: ", search_term)
    if search_type and search_term:
        with open('NWC Name board1.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                row[search_type] = row[search_type].lower().replace(" ","")
            csv_file.seek(0)
            resList = []
            for row in csv_reader:
                if search_term in "".join("".join(row[search_type].split(".")).split(" ")).lower():
                    print(row)
                    resList.append(row)
            if len(resList) > 0:
                print(resList)
                return jsonify(resList)

    return jsonify({'message': 'No match found for the search term.'})

if __name__ == '__main__':
  app.run()
