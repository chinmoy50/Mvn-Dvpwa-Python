import sys
import logging

from flask import request, Flask

from aiohttp.web import run_app

from sqli.app import init as init_app

log = logging.getLogger(__name__)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    app = init_app(sys.argv[1:])

    host = app['config']['app']['host']
    port = app['config']['app']['port']
    log.info(f'App is listening at http://{host}:{port}')
    run_app(app, host=host, port=port)




app = Flask(__name__)

@app.route("/greet")
def greet():
    name = request.args.get("name", "")
    return f"<h1>Hello {name}</h1>"  # BUG: reflected XSS
