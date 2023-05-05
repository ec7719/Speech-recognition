import csv
import speech_recognition as sr
import pyttsx3 
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
    r = sr.Recognizer()
    engine = pyttsx3.init()

    search_type = None
    search_term = None
    
    data = request.get_json()
    speech_to_text = data['speech_to_text']
    if 'faculty' in speech_to_text.lower():
        search_type = 'Faculty Name'
    elif 'roomno' in speech_to_text.lower():
        search_type = 'ROOM NO'
    else:
        return jsonify({'message': 'Invalid search type. Please try again.'})
    
    search_term = data['search_term']
    
    if search_type and search_term:
        with open('NWC Name board1.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row[search_type] == search_term:
                    # Return the search result as a JSON response
                    result = {'name': row['Name'], 'room_no': row['ROOM NO']}
                    return jsonify(result)

    return jsonify({'message': 'No match found for the search term.'})

if __name__ == '__main__':
  app.run()