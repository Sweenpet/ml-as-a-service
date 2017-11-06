import logging

from flask_restplus import Api
from ml_as_a_service import settings

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Image Detection API', description='A restful api for various image detection')

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500

