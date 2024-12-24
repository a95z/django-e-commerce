import urllib
from django.shortcuts import redirect


def redirect_with_params(url, **kwargs):
    response = redirect(url)

    if kwargs:
        query_string = urllib.parse.urlencode(kwargs)
        response["Location"] += "?" + query_string

    return response


def make_breadcrumbs(full_path: str) -> list[str]:
    """Generates breadcrumb paths from a full URL path."""

    segments = [segment for segment in full_path.split("/") if segment]

    return [
        {
            "label": segments[i].split("?")[0],
            "href": f"/{'/'.join(segments[:i + 1])}",
        }
        for i in range(len(segments))
    ]
