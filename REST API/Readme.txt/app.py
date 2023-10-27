from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory storage for book records (you should use a database in a real application)
books = []

@app.route('/api/books', methods=['GET', 'POST'])
def manage_books():
    if request.method == 'GET':
        return jsonify(books)
    elif request.method == 'POST':
        data = request.get_json()
        if data:
            books.append(data)
            return jsonify({'message': 'Book added successfully'}), 201
        else:
            return jsonify({'error': 'Invalid data'}), 400

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
