from flask import Blueprint

from routes.api.v1.captcha import captcha

urlpatterns = [
    ("/captcha", captcha),
]

v1 = Blueprint("v1", __name__)
for path, blueprint in urlpatterns:
    v1.register_blueprint(blueprint, url_prefix=path)

__all__ = ["v1"]
