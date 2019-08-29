""" Tests for the Deepmap Client class. """
from deepmap_sdk.deepmap_sdk_example import DeepmapClient


def test_client_functions_as_admin(admin_token, server):
    """ Tests all functions implemented by the client as an admin user. """

    assert server is not None

    test_client = DeepmapClient(admin_token, server)

    print(test_client.is_exp())
    print(test_client.get_exp())

    num_users = len(test_client.list_users())
    assert num_users == 2 or num_users > 2

    invited = test_client.invite_user('fake@deepmap.ai')
    assert invited['email'] == 'fake@deepmap.ai'
    assert not invited['admin']

    test_client.edit_user(invited['id'], 'fake2@deepmap.ai', 'True')
    updated = test_client.get_user(invited['id'])
    assert updated['email'] == 'fake2@deepmap.ai'
    assert updated['admin']

    test_client.edit_user(invited['id'], email='fake3@deepmap.ai')
    updated = test_client.get_user(invited['id'])
    assert updated['email'] == 'fake3@deepmap.ai'
    assert updated['admin']

    test_client.edit_user(invited['id'], admin='False')
    updated = test_client.get_user(invited['id'])
    assert updated['email'] == 'fake3@deepmap.ai'
    assert not updated['admin']

    test_client.delete_user(invited['id'])

    assert len(test_client.list_users()) == num_users


def test_client_functions_as_user(admin_token, reg_token, server):
    """ Tests all functions implemented by the client as a regular user. """

    assert server is not None

    # Invite a new user to be subject of tests
    test_client = DeepmapClient(admin_token, server)
    invited = test_client.invite_user('fake@deepmap.ai')

    num_users = len(test_client.list_users())
    assert num_users == 3 or num_users > 3

    # Log in as regular user
    assert len(test_client.list_users()) == num_users
    test_client = DeepmapClient(reg_token, server)

    test_client.edit_user(invited['id'], 'fake2@deepmap.ai', 'True')
    updated = test_client.get_user(invited['id'])
    assert updated['email'] == invited['email']
    assert updated['admin'] == invited['admin']

    test_client.delete_user(invited['id'])
    # Check that the number of users hasn't changed
    assert num_users == len(test_client.list_users())

    test_client.invite_user('fake2@deepmap.ai')
    assert num_users == len(test_client.list_users())

    # Store number of existing tokens
    tokens = test_client.list_api_tokens()
    if tokens:
        num_api_tokens = len(tokens)
    else:
        num_api_tokens = 0

    # Generate an API token
    api_token_response = test_client.create_api_token("test description")
    assert 'id' in api_token_response
    assert 'api_token' in api_token_response
    api_token_id = api_token_response['id']
    api_token_val = api_token_response['api_token']
    print(api_token_response)

    # List API tokens test
    assert len(test_client.list_api_tokens()) - 1 == num_api_tokens

    # Use API token to get a JWT, simply checks to see that the session token exists,
    # because unit testing already checks that a returned JWT is valid
    api_session_token_response = test_client.create_api_session(api_token_val)
    assert 'token' in api_session_token_response

    # Delete API token
    test_client.delete_api_token(api_token_id)
    tokens_after_delete = test_client.list_api_tokens()
    if tokens_after_delete:
        assert len(tokens_after_delete) == num_api_tokens

    # Store number of existing tokens
    tokens = test_client.list_vehicle_tokens()
    if tokens:
        num_vehicle_tokens = len(tokens)
    else:
        num_vehicle_tokens = 0

    # Generate a vehicle token
    vehicle_token_response = test_client.create_vehicle_token(
        "test vehicle id", "test description")
    assert 'id' in vehicle_token_response
    assert 'vehicle_token' in vehicle_token_response
    vehicle_token_id = vehicle_token_response['id']
    vehicle_token_val = vehicle_token_response['vehicle_token']
    print(vehicle_token_response)

    # List vehicle API tokens test
    assert len(test_client.list_vehicle_tokens()) - 1 == num_vehicle_tokens

    # Use vehicle token to get a JWT, simply checks to see that the session token exists,
    # because unit testing already checks that a returned JWT is valid
    vehicle_session_token_response = test_client.create_vehicle_session(
        vehicle_token_val)
    assert 'token' in vehicle_session_token_response

    # Delete vehicle token
    test_client.delete_vehicle_token(vehicle_token_id)
    tokens_after_delete = test_client.list_vehicle_tokens()
    if tokens_after_delete:
        assert len(tokens_after_delete) == num_vehicle_tokens

    # Cleanup
    test_client = DeepmapClient(admin_token, server)

    test_client.delete_user(invited['id'])
    assert (num_users - 1) == len(test_client.list_users())
