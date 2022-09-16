from app import create_app

app=create_app()

debug = True
port = 2000

if __name__ == '__main__':
    app.run(debug=debug, port=port)
    #app.run()
