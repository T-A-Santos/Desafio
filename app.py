import tornado
from tornado import gen
from tornado.ioloop import IOLoop

# local imports
from servers import build_service
from settings import OWN_DB_INFO
from models import db


@gen.coroutine
def launch_service(host='localhost', port='9999'):
    # database setup
    current = IOLoop.current()
    app = build_service(
        service_management={}
        )
    current.run_sync(
        lambda: db.init_app(app, **OWN_DB_INFO)
    )

    http_server = tornado.httpserver.HTTPServer(app)
    # launch listener server
    http_server.listen(port)
    print(f'run service on port http://localhost:{port}')
    # launch services
    IOLoop.instance().start()


if __name__ == '__main__':
    launch_service()