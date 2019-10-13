from flask_blog import app

if __name__ == '__main__':
    app.run(debug=False)
    app.run(port=5000, host='192.168.0.14')