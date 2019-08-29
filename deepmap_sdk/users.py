""" Create requests params for users API. """

import urllib.parse
import sys


def list_users(server_url):
    """ Returns a url for listing users.

    Args:
        server_url: String of base URL of the API.
    """

    url = urllib.parse.urljoin(server_url, '/api/users/v1/users')
    return url


def invite_user(email, admin, server_url):
    """ Returns url and payload for inviting a user.

    Args:
        email: String of new user's email.
        admin: String taking value 'True' if new user should be an admin.
        server_url: String of base URL of the API.
    """

    url = urllib.parse.urljoin(server_url, '/api/users/v1/invite')
    payload = {'email': email}
    if admin == 'True':
        payload['admin'] = True
    else:
        payload['admin'] = False

    return url, payload


def get_user(user_id, server_url):
    """ Returns a url for getting the user's information. """

    url = urllib.parse.urljoin(server_url,
                               '/api/users/v1/users/{}'.format(user_id))
    return url


def edit_user(user_id, email, admin, server_url):
    """ Returns a url for editing the user and a payload, the user's info
    to change to.

    Args:
        user_id: String of user's id.
        email: String of email to change to, or empty string if no change.
        admin: String of 'True' or 'False' represnting new admin status,
               or empty string if no change.
        server_url: String of base URL of the API.
    """

    url = urllib.parse.urljoin(server_url,
                               '/api/users/v1/users/{}'.format(user_id))

    if not email and not admin:
        sys.exit('Nothing to be changed.')
    else:
        payload = {}
        if email:
            payload['email'] = email
        if admin:
            if admin == 'True':
                payload['admin'] = True
            elif admin == 'False':
                payload['admin'] = False
    return url, payload


def delete_user(user_id, server_url):
    """ Returns a url for deleting the user.

    Args:
        server_url: String of base URL of the API.
    """

    url = urllib.parse.urljoin(server_url,
                               '/api/users/v1/users/{}'.format(user_id))
    return url
