from application import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
from flask import send_file

@app.route('/download-db')
def download_db():
    return send_file('flicket.db', as_attachment=True)
