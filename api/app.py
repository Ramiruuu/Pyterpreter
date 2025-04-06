from flask import Flask, request, jsonify, render_template
import sys
from io import StringIO

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.json['code']
    
    # Redirect stdout to capture output
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    
    try:
        exec(code)
        output = redirected_output.getvalue()
        success = True
    except Exception as e:
        output = str(e)
        success = False
    
    # Restore stdout
    sys.stdout = old_stdout
    
    return jsonify({
        'output': output,
        'success': success
    })

if __name__ == '__main__':
    app.run(debug=True)