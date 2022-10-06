from app import create_app
import webview

app=create_app()

debug = True
port = 3000

if __name__ == '__main__':
    #app.run(debug=debug, port=port)
    #app.run()
    webview.create_window('Typless', app, width=800, height=480)
    webview.start()
