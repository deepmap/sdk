""" Python class to interact with the APIs. """

import sys
import json
import time
import jwt
from requests import Session
from deepmap_sdk import auth, users, tiles, maps


class DeepmapClient:
    """ Python Client for the Deepmap API. """

    def __init__(self, api_token, server_url='https://api.deepmap.com'):
        self.session = Session()
        url, payload, headers = auth.create_api_session(api_token, server_url)
        self.session.headers.update(headers)
        response = self.session.post(url, data=json.dumps(payload))

        if response.status_code != 200:
            sys.exit('Failed to login.')

        token = response.json()['token']
        headers['Authorization'] = 'Bearer ' + token

        self.session.headers.update(headers)

        decoded_token = jwt.decode(token, algorithms=["ES256"], verify=False)
        self.expiration = decoded_token['exp']

        self.server_url = server_url

    def is_exp(self):
        """ Returns True if token is expired, False otherwise. """
        return time.time() >= self.expiration

    def get_exp(self):
        """ Returns the Unix time since epoch expiration time. """
        return self.expiration

    def list_maps(self):
        """ Returns a dictionary of the list of maps. """
        url = maps.list_maps(self.server_url)
        response = self.session.get(url)
        return response.json()

    def list_feature_tiles(self, map_id):
        """ Returns a dictionary of feature tiles for map designated by map_id. """
        url = tiles.list_feature_tiles(map_id, self.server_url)
        response = self.session.get(url)
        return response.json()

    def list_users(self):
        """ Returns a dictionary of the list of maps. """
        url = users.list_users(self.server_url)
        response = self.session.get(url)
        return response.json()

    def download_feature_tile(self, tile_id):
        """ Downloads a feature tile designated by tile_id. Returns a binary string. """
        url = tiles.download_feature_tile(tile_id, self.server_url)
        response = self.session.get(url)
        if response.status_code == 200:
            return response.content
        return response.json()

    def get_user(self, user_id):
        """ Returns user information for user designated by user_id. """
        url = users.get_user(user_id, self.server_url)
        response = self.session.get(url)
        return response.json()

    def invite_user(self, email, admin=''):
        """ Invites new user to join.

        Args:
            email: email of the new user.
            admin: String, 'True' if new user is an admin. 'False' or '' otherwise.
        """
        url, payload = users.invite_user(email, admin, self.server_url)
        response = self.session.post(url, data=json.dumps(payload))

        if response.status_code != 200:
            print("Error. Could not invite user.")
            return {}
        return response.json()

    def edit_user(self, user_id, email='', admin=''):
        """ Edits an exisiting user's information.

        Args:
            email: email of the new user.
            admin: String, 'True' if user will be admin. 'False' or '' otherwise.
        """
        url, payload = users.edit_user(user_id, email, admin, self.server_url)
        response = self.session.post(url, data=json.dumps(payload))

        if response.status_code != 200:
            print("Error. Could not edit user.")
        else:
            print("User edited.")

    def delete_user(self, user_id):
        """ Deletes user designated by user_id. """
        url = users.delete_user(user_id, self.server_url)
        response = self.session.delete(url)

        if response.status_code != 200:
            print("Error. Could not invite user.")
        else:
            print("User deleted.")

    def create_api_token(self, description):
        """ Creates an API access token with the given description. """
        url, payload = auth.create_api_token(description, self.server_url)
        response = self.session.post(url, data=json.dumps(payload))
        return response.json()

    def create_vehicle_token(self, vehicle_id, description):
        """ Creates an vehicle access token with the given description and
            vehicle_id. """
        url, payload = auth.create_vehicle_token(vehicle_id, description,
                                                 self.server_url)
        response = self.session.post(url, data=json.dumps(payload))
        return response.json()

    def delete_api_token(self, token_id):
        """ Delete the API token with token_id as its id. """
        url = auth.delete_api_token(token_id, self.server_url)
        response = self.session.delete(url)

        if response.status_code != 200:
            print("Error. Could not delete API token.")
        else:
            print("API token deleted.")

    def delete_vehicle_token(self, token_id):
        """ Delete the vehicle token with token_id as its id. """
        url = auth.delete_vehicle_token(token_id, self.server_url)
        response = self.session.delete(url)

        if response.status_code != 200:
            print("Error. Could not delete vehicle token.")
        else:
            print("Vehicle token deleted.")

    def list_api_tokens(self):
        """ List all issued API tokens under the user's account. """
        url = auth.list_api_tokens(self.server_url)
        response = self.session.get(url)
        return response.json()

    def list_vehicle_tokens(self):
        """ List all issued vehicle tokens under the user's account. """
        url = auth.list_vehicle_tokens(self.server_url)
        response = self.session.get(url)
        return response.json()

    def create_api_session(self, api_token):
        """ Create an API session token (JWT) using a API access token. """
        url, payload, _ = auth.create_api_session(api_token, self.server_url)
        response = self.session.post(url, data=json.dumps(payload))
        return response.json()

    def create_vehicle_session(self, vehicle_token):
        """ Create a vehicle session token (JWT) using a API access token. """
        url, payload, _ = auth.create_vehicle_session(vehicle_token,
                                                      self.server_url)
        response = self.session.post(url, data=json.dumps(payload))
        return response.json()

    def __str__(self):
        return "url: {}\nexp: {}\n".format(self.server_url, self.expiration)
