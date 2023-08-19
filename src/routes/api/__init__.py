from flask import Blueprint

from routes.api.v1 import v1

urlpatterns = [
    ("/v1", v1),
]

api = Blueprint("api", __name__)
for path, blueprint in urlpatterns:
    api.register_blueprint(blueprint, url_prefix=path)

__all__ = ["api"]
