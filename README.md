py-pushover
===========

Python wrapper for sending Pushover messages


Usage example
-------------
    import pushover
    resp = pushover.send(token=MY_API_TOKEN,
                         user=MY_USER_TOKEN,
                         message="Oh hi there")
    if resp['status'] == 1:
        print "hey, it worked!"

You will need
----------------
* to install the wondrous [Requests](https://github.com/kennethreitz/requests) library. This will be set up as a proper dependency once I package this up.
* to create an [application](https://pushover.net/apps) on Pushover's site to obtain the API token necessary for sending messages.
* a user token to send messages to.

Usage details
-------------
`send()` takes arguments as described in the [Pushover API docs](https://pushover.net/api). `token`, `user`, and `message` are required, the rest are optional. The only difference is that we will, if you prefer it, accept a value of `True` for the `priority` option.

`send()` will return a dictionary constructed from the JSON response provided by the API call. We add a key called `http_status` which contains the HTTP status code from our request. Normal usage will product a dictionary like `{'http_status': 200, 'status': 1}`. In the event of failure, the dictionary should contain information useful to determining the issue.

See example/push.py for a simple example of a script that sends a notification from the commandline.