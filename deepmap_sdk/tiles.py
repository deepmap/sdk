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

def list_tiles_diff(map_id, server_url, z, map_format, before=None, after=None):
    """ Returns a url for fetching updated tiles.

    Args:
        map_id: Id of the map whose tiles is being check.
        server_url: String of base URL of the API.
        map_format: Format of the map to check tiles diff.
        z: The map level.
        before: The timestamp in milliseconds. The upper bound of the time range which
        targeted tile should belong to. If the field is set,
        it will only fetch tiles which version is older than or equal to the given timestamp.
        after: The timestamp in milliseconds. The lower bound of the time range which
        targeted tile should belong to. If the field is set, it will only fetch tiles
        which version is newer than or equal to the given timestamp.

    """

    url = urllib.parse.urljoin(server_url,
                               '/api/tiles/v2/{}/diff'.format(map_id))

    query = {}
    query['format'] = map_format
    query['z'] = z
    if before:
        query['before'] = before
    if after:
        query['after'] = after

    url_sections = list(urllib.parse.urlparse(url))
    url_sections[4] = urllib.parse.urlencode(query)
    url = urllib.parse.urlunparse(url_sections)
    return url

def search_tiles(map_id, server_url, z, lat1, lat2, lng1, lng2, map_format, before=None, after=None):
    """ Returns a url for fetching tiles in bbox.

    Args:
        map_id: Id of the map whose tiles is being search.
        server_url: String of base URL of the API.
        map_format: Format of the map to check tiles diff.
        z: The map level.
        lat1: The first latitude of the web mercator bounding box.
        lat2: The second latitude of the web mercator bounding box.
        lng1: The first longitude of the web mercator bounding box.
        lng2: The second longitude of the web mercator bounding box.
        before: The timestamp in milliseconds. The upper bound of the time range which
        targeted tile should belong to. If the field is set,
        it will only fetch tiles which version is older than or equal to the given timestamp.
        after: The timestamp in milliseconds. The lower bound of the time range which
        targeted tile should belong to. If the field is set, it will only fetch tiles
        which version is newer than or equal to the given timestamp.
    """

    url = urllib.parse.urljoin(server_url,
                               '/api/tiles/v2/{}/tiles/search/bbox'.format(map_id))

    query = {}
    query['format'] = map_format
    query['z'] = z
    query['lat1'] = lat1
    query['lat2'] = lat2
    query['lng1'] = lng1
    query['lng2'] = lng2
    if before:
        query['before'] = before
    if after:
        query['after'] = after

    url_sections = list(urllib.parse.urlparse(url))
    url_sections[4] = urllib.parse.urlencode(query)
    url = urllib.parse.urlunparse(url_sections)
    return url

def download_tile(map_id, server_url, z, x, y, map_format, before=None, after=None):
    """ Returns a url for downloading targeted tile by providing TileXYZ.

    Args:
        map_id: Id of the map whose tile is being downloaded.
        server_url: String of base URL of the API.
        map_format: Format of the map to check tiles diff.
        z: The map level.
        x: The x offset into the tile grid at the specified zoom level.
        Each level has 2^z x 2^z tiles, so level 0 is 1x1, level 10 is 1024x1024.
        Our '(0, 0)' map offset is at the top left of the map.
        y: The y offset into the tile grid at the specified zoom level.
        Each level has 2^z x 2^z tiles, so level 0 is 1x1, level 10 is 1024x1024.
        Our '(0, 0)' map offset is at the top left of the map.
        before: The timestamp in milliseconds. The upper bound of the time range which
        targeted tile should belong to. If the field is set,
        it will only fetch tiles which version is older than or equal to the given timestamp.
        after: The timestamp in milliseconds. The lower bound of the time range which
        targeted tile should belong to. If the field is set, it will only fetch tiles
        which version is newer than or equal to the given timestamp.
    """

    url = urllib.parse.urljoin(server_url,
                               '/api/tiles/v2/{}/tile'.format(map_id))

    query = {}
    query['format'] = map_format
    query['z'] = z
    query['x'] = x
    query['y'] = y
    if before:
        query['before'] = before
    if after:
        query['after'] = after

    url_sections = list(urllib.parse.urlparse(url))
    url_sections[4] = urllib.parse.urlencode(query)
    url = urllib.parse.urlunparse(url_sections)
    return url

def download_feature_tile(tile_id, server_url):
    """ Returns a url for downloading a specific feature tile.

    Args:
        tile_id: The id of the tile to download.
    """

    url = urllib.parse.urljoin(
        server_url, "/api/tiles/v1/feature_tiles/{}".format(tile_id))
    return url
