from flask import Blueprint

from views.captcha import BreakerView

captcha = Blueprint("captcha", __name__)
captcha.add_url_rule("/breaker", view_func=BreakerView.as_view("breaker"))
