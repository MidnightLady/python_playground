from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="templates", static_folder='static')

# Path to the folder containing Python files
PROBLEMS_FOLDER = './problems/'


@app.route('/')
def index():
    items = []

    for root, dirs, files in os.walk(PROBLEMS_FOLDER):
        for dir in dirs:
            items.append({'type': 'folder', 'name': dir, 'path': os.path.join(root, dir)})
        for file in files:
            items.append({'type': 'file', 'name': file, 'path': os.path.join(root, file)})

    return render_template('index.html', items=items)


@app.route('/item/<path:item_path>')
def show_item(item_path):
    # Get the content of the selected Python file
    file_path = os.path.join(item_path)

    with open(file_path, 'r') as file:
        code = file.read()

    # Just return the raw code to highlight.js (no need for parsing)
    return render_template('item_content.html', filename=item_path, code=code)


if __name__ == '__main__':
    app.run(debug=True)


