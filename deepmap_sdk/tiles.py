""" Create requests params for tiles API. """

import urllib.parse


def list_feature_tiles(map_id, server_url):
    """ Returns a url for listing a specific map's feature_tiles.

    Args:
        map_id: The id of the map.
    """

    url = urllib.parse.urljoin(server_url,
                               "/api/maps/v1/{}/feature_tiles".format(map_id))
    return url


def download_feature_tile(tile_id, server_url):
    """ Returns a url for downloading a specific feature tile.

    Args:
        tile_id: The id of the tile to download.
    """

    url = urllib.parse.urljoin(
        server_url, "/api/tiles/v1/feature_tiles/{}".format(tile_id))
    return url
