from __future__ import unicode_literals
import requests

PUSHOVER_API_URL = 'https://api.pushover.net/1/messages.json'


def send(token, user, message, **kwargs):
    """Send a Pushover notification.

    Returns a dictionary created from the API's json response, plus a 'http_status'
    key with the HTTP status code returned. A normal successful message would have
    'http_status' == 200 and 'status' == 1.

    Required parameters:
        token: the Pushover api token for your application.
        user: the Pushover user token which will receive the message.
        message: the message to be sent.

    Optional parameters:
        device: send to a specific device identifier, rather than all.
        title: a title for the message; if omitted, your app's name is sent.
        url: a supplementary url to show with the message.
        url_title: a title for the supplementary url.
        priority: set to 1 or True to send as high priority.
        timestamp: Unix timestamp for your message, rather than the current time.
    """
    try:
        if kwargs['priority'] == True:
            kwargs['priority'] = 1
    except KeyError:
        pass

    kwargs['token'] = token
    kwargs['user'] = user
    kwargs['message'] = message

    r = requests.post(PUSHOVER_API_URL, params=kwargs)
    ret_json = r.json
    ret_json['http_status'] = r.status_code
    return ret_json
