import werkzeug
from flask_restplus import reqparse

image_detection = reqparse.RequestParser()
image_detection.add_argument('image',
                         type=werkzeug.datastructures.FileStorage,
                         location='files',
                         required=True,
                         help='JPEG file')