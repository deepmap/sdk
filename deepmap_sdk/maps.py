""" Create request params for maps API. """

import urllib.parse


def list_maps(server_url):
    """ Returns a url for listing maps.

    Args:
        server_url: String of base URL of the API.
    """

    url = urllib.parse.urljoin(server_url, '/api/maps/v1/maps')
    return url


def download_distribution(map_id, server_url, map_format=None, version=None):
    """ Returns a url for downloading a map distribution.

    Args:
        map_id: Id of the map whose distribution is being downloaded.
        server_url: String of base URL of the API.
        map_format: Format of the map distribution to download.
        version: Version of the map to download.
    """

    url = urllib.parse.urljoin(server_url,
                               '/api/maps/v1/{}/distribution'.format(map_id))

    query = {}
    if map_format:
        query['format'] = map_format
    if version:
        query['version'] = version

    url_sections = list(urllib.parse.urlparse(url))
    url_sections[4] = urllib.parse.urlencode(query)
    url = urllib.parse.urlunparse(url_sections)
    return url
