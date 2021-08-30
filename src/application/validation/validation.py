from enum import IntEnum


class Pages(IntEnum):
    URL_ONE = 1


def validate(url: str):
    page_list = {"www.brmangas.com":  1}

    for x in page_list:
        if x in url:
            return Pages(page_list[x])

    return None
