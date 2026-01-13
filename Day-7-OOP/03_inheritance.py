class Server:
    def start(self):
        print("Starting server")

class WebServer(Server):
    def deploy_app(self):
        print("Deploying web application")

ws = WebServer()
ws.start()
ws.deploy_app()
print(isinstance(ws, WebServer))  # True