""" Create requests params for auth API. """

import urllib.parse


def create_api_session(api_token, server_url):
    """ Returns a url, payload, and headers for creating an API session token/JWT,
    which is required to access the rest of the API.

    Args:
        api_token: A valid API access token.
    """
    headers = {'Content-Type': 'application/json'}
    payload = {'api_token': api_token}
    url = urllib.parse.urljoin(server_url, "/api/auth/v1/token/api/session")
    return url, payload, headers


def reset_password_auth(email, server_url):
    """ Returns a url, payload, and headers for a password reset attempt. """

    headers = {'Content-Type': 'application/json'}
    payload = {'email': email}
    url = urllib.parse.urljoin(server_url, '/api/auth/v1/reset_password')
    return url, payload, headers


def create_api_token(description, server_url):
    """ Returns a url and payload for creating an API access token.

    Args:
        description: A user provided description for the API user.
    """
    payload = {'description': description}
    url = urllib.parse.urljoin(server_url, '/api/auth/v1/token/api')
    return url, payload


def create_vehicle_token(vehicle_id, description, server_url):
    """ Returns a url and payload for creating an vehicle access token.

    Args:
        vehicle_id: A user provided unique identifier for the vehicle.
        description: A user provided description for the vehicle.
    """
    payload = {'vehicle_id': vehicle_id, 'description': description}
    url = urllib.parse.urljoin(server_url, '/api/auth/v1/token/vehicle')
    return url, payload


def delete_api_token(token_id, server_url):
    """ Returns a url for deleting an API access token.

    Args:
        token_id: The id of the token to delete.
    """
    url = urllib.parse.urljoin(server_url,
                               "/api/auth/v1/token/api/{}".format(token_id))
    return url


def delete_vehicle_token(token_id, server_url):
    """ Returns a url and headers for deleting a vehicle access token.

    Args:
        token_id: The id of the token to delete.
    """
    url = urllib.parse.urljoin(
        server_url, "/api/auth/v1/token/vehicle/{}".format(token_id))
    return url


def list_api_tokens(server_url):
    """ Returns a url for listing issued API access tokens. """
    url = urllib.parse.urljoin(server_url, "/api/auth/v1/token/api")
    return url


def list_vehicle_tokens(server_url):
    """ Returns a url for listing issued vehicle access tokens. """
    url = urllib.parse.urljoin(server_url, "/api/auth/v1/token/vehicle")
    return url


def create_vehicle_session(vehicle_token, server_url):
    """ Returns a url, payload, and headers for creating a vehicle session token/JWT

    Args:
        vehicle_token: A valid vehicle access token.
    """
    headers = {'Content-Type': 'application/json'}
    payload = {'vehicle_token': vehicle_token}
    url = urllib.parse.urljoin(server_url,
                               "/api/auth/v1/token/vehicle/session")
    return url, payload, headers
