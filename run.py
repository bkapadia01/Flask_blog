from flaskblog import create_app

application = app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    app.run(port=5000, host='192.168.0.14')