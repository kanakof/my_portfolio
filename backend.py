from flask import Flask, render_template, request, redirect, url_for
import code


app = Flask(__name__, static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/', methods=['GET'])
def process_GET_request():
    return render_template('page.html', title='personality', name="top page")

@app.route('/works-template.html', methods=['GET'])
def work_template1():
    return render_template('works-template.html', title='personality', name="top page")

@app.route('/works-template2.html', methods=['GET'])
def work_template2():
    return render_template('works-template2.html', title='personality', name="top page")

if __name__ == "__main__":
    app.run(debug=True, port=8000, threaded=True)
    print("Flask server has started")