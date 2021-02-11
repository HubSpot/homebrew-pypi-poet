from contextlib import closing
from hashlib import sha256

try:
    # Python 2.x
    from urllib2 import urlopen, urlparse, urlunparse
except ImportError:
    # Python 3.x
    from urllib.parse import urlparse, urlunparse
    from urllib.request import urlopen


_PARSED_URL_INDICES = {
    "scheme": 0,
    "netloc": 1,
    "path": 2,
    "params": 3,
    "query": 4,
    "fragment": 5,
}


def dash_to_studly(s):
    l = list(s)
    l[0] = l[0].upper()
    delims = "-_"
    for i, c in enumerate(l):
        if c in delims:
            if (i+1) < len(l):
                l[i+1] = l[i+1].upper()
    out = "".join(l)
    for d in delims:
        out = out.replace(d, "")
    return out


def extract_credentials_from_url(url):
    parsed_url = urlparse(url)
    url_without_credentials = transform_url(url, netloc=parsed_url.hostname)
    return url_without_credentials, parsed_url.username, parsed_url.password


def transform_url(url, **kwargs):
    url_parts = list(urlparse(url))

    for key, value in kwargs.items():
        try:
            index = _PARSED_URL_INDICES[key]
        except KeyError:
            continue

        url_parts[index] = value

    return urlunparse(tuple(url_parts))


def compute_sha256_sum(url):
    with closing(urlopen(url)) as file_:
        return sha256(file_.read()).hexdigest()
