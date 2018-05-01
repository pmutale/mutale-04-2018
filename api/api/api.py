import logging
import json
import requests

from django.conf import settings
from requests import RequestException

logger = logging.getLogger('__name__')

LOGGING_LEVELS = {
    'INFO': logger.info,
    'WARNING': logger.warning,
    'ERROR': logger.error,
    'EXCEPTION': logger.exception
}


class MutaleAPI(object):
    HTTP_GET = 'GET'
    HTTP_POST = 'POST'
    HTTP_PUT = 'PUT'
    HTTP_DELETE = 'DELETE'

    def _get(self, resource, params=None, key='data'):
        """
        Perform a HTTP GET request on the ESB API
        :param resource:
           :param params:
           :return: deserialized JSON string as python object
           """
        result = self.api_call(resource, params, self.HTTP_GET)
        if 'result' not in result:
            error_message = 'No result entry found in esb response'
            logger.exception(error_message)
            raise APIError(error_message, resource, params)
        return result[key]

    def api_call(self, action, params, method=HTTP_GET):
        """
        Generic endpoint for making all Bookingstreet requests.
        Checks for HTTP 200 status code of response, throws error otherwise.
        :param method: HTTP Request Method
        :param action: api endpoint (e.g. bookingstreet/get_preferences)
        :param params: dict of args to pass along
        :return: deserialized JSON string as python object
        """
        url = action
        if settings.DEBUG:
            logger.info("Calling {0} method on ESB: {1}".format(method, url))
        try:
            if method == self.HTTP_GET:
                response = requests.get(url, params=params)
            # elif method == self.HTTP_POST:
            #     response = requests.post(url, json=params)
            # elif method == self.HTTP_DELETE:
            #     response = requests.delete(url)
            # elif method == self.HTTP_PUT:
            #     response = requests.put(url, json=params)
            else:
                raise APIError(
                    'Unknown HTTP method: {method}, url: {url}'.format(
                        method=method, url=url))
        except RequestException as e:
            logger.exception(e.message)
            raise APIError('RequestException: {message}'.format(
                message=e.message))

        if settings.DEBUG:  # for performance reasons
            logger.info("URL: {0}".format(url))
            logger.info("Response code: {0}".format(response.status_code))
        # json_response = self.detect_response_error(response, url, params)
        j_response = json.loads(response.content, url, params)
        return j_response


class APIError(Exception):
    """
    Custom exception type to distinguish errors arising fromout ESB
    """

    def __init__(self, message, code=0, title='', *args):
        self.message = message
        self.code = code
        self.title = title
        super(APIError, self).__init__(message, code, title, *args)

    def __str__(self):
        return self.message
