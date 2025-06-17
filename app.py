from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__, template_folder='../html_templates', static_folder='../static_assets')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/preorder', methods=['POST'])
def preorder():
    name = request.form['name']
    email = request.form['email']
    cap = request.form['cap']

    data_path = os.path.join(os.path.dirname(__file__), 'data/orders.csv')
    with open(data_path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, email, cap])

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
