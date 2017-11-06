from flask_restplus import fields
from ml_as_a_service.api.restplus import api

classification = api.model('Classification', {
    'type': fields.String(readOnly=True, description='The type of item classified'),
    'x1': fields.Float(required=True, description='x1 position'),
    'y1': fields.Float(required=True, description='y1 position'),
    'width': fields.Float(required=True, description='width'),
    'height': fields.Float(required=True, description='height'),
})
