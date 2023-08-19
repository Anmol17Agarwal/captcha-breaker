from marshmallow import fields

from utils import ma


class BreakerSchema(ma.Schema):
    """Breaker Schema"""

    image = fields.Raw(metadata={"type": "string", "format": "binary"}, load_only=True)
    text = fields.Str(dump_only=True)
