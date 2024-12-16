from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="templates", static_folder='static')

# Path to the folder containing Python files
PROBLEMS_FOLDERS = {'Leetcode':'./Leetcode/','CodeForce': './CodeForce/'}


@app.route('/')
def index():
    folders = {}
    for name, folder in PROBLEMS_FOLDERS.items():
        items = []
        for root, dirs, files in os.walk(folder):
            for d in dirs:
                items.append({'type': 'folder', 'name': d, 'path': os.path.join(root, d)})
            for file in files:
                items.append({'type': 'file', 'name': file, 'path': os.path.join(root, file)})
        folders[name] = items

    return render_template('index.html', folders=folders)


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


