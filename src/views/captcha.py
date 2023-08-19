from http import HTTPStatus

from flask import jsonify, request, views
from marshmallow import ValidationError

from schemas import BreakerSchema
from utils.preprocess import pre_process_image, get_text_from_clear_image_numeric


class BreakerView(views.MethodView):
    """Breaker View"""

    schema_class = BreakerSchema

    def post(self, *args, **kwargs):
        schema = self.schema_class()
        try:
            validated_data = schema.load(request.files)
        except ValidationError as e:
            return jsonify(e.messages), HTTPStatus.BAD_REQUEST
        value = get_text_from_clear_image_numeric(pre_process_image(validated_data["image"]))
        # valuee = get_text_from_clear_image_six(pre_process_image(validated_data("image")))
        return jsonify(schema.dump({"text": value})), HTTPStatus.CREATED
