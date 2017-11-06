import logging

from flask_restplus import Resource
from flask import jsonify
from ml_as_a_service.api.restplus import api
from ml_as_a_service.api.detectors import parsers
from ml_as_a_service.api.detectors.models import Classification
from ml_as_a_service.api.detectors.serializers import classification

log = logging.getLogger(__name__)
ns = api.namespace('detectors/little_men', description='Operations related to blog categories')


@ns.route('/')
class LittleManDetection(Resource):

    @api.response(200, 'Successfully analysed image for little men.')
    @api.response(500, 'There was an error trying to analyse little men.')
    @api.expect(parsers.image_detection)
    @api.marshal_with(classification)
    def post(self):
        args = parsers.image_detection.parse_args()

        if args['image'].mimetype != 'image/jpeg':
            return None, 500

        jpeg_image = args['image']

        model = Classification(1, 10, 10, 20, 40)
        return model, 200