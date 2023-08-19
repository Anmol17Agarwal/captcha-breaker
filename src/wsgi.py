from flask import Flask

from routes import urlpatterns
from utils import ma
import settings


def get_wsgi_application():
    app = Flask(__name__)
    app.config.update(
        DEBUG=settings.DEBUG,
    )
    ma.init_app(ma)
    for path, blueprint in urlpatterns:
        app.register_blueprint(blueprint, url_prefix=path)
    return app


application = get_wsgi_application()

if __name__ == "__main__":
    application.run()
