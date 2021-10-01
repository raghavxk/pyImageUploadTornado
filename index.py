import tornado.web
import tornado.ioloop

port = 8080

class uploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        files = self.request.files["imgFile"]
        for f in files:
            fh = open(f"img/{f.filename}", "wb")
            fh.write(f.body)
            fh.close()
        self.write(f"http://localhost:{port}/img/{f.filename}")


if(__name__ == '__main__'):
    app = tornado.web.Application([
        ("/", uploadHandler),
        ("/img/(.*)", tornado.web.StaticFileHandler, {"path": "img"})
    ])

    app.listen(port)
    print(f"listening on port {port} . server is up and runnning")

    tornado.ioloop.IOLoop.instance().start()


