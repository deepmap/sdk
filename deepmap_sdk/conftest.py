""" Configures the pytest tests. """
import pytest


def pytest_addoption(parser):
    """ Adds command line args for tests. """
    parser.addoption("--admin_token",
                     action="store",
                     help="API token of an admin account.")
    parser.addoption("--reg_token",
                     action="store",
                     help="API token of a non-admin user.")
    parser.addoption("--server",
                     action="store",
                     help="Base URL of the API requested.")


@pytest.fixture
def admin_token(request):
    """ admin_token param. """
    return request.config.getoption("--admin_token")


@pytest.fixture
def reg_token(request):
    """ reg_token param. """
    return request.config.getoption("--reg_token")


@pytest.fixture
def server(request):
    """ server param. """
    return request.config.getoption("--server")
