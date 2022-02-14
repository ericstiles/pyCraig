from bs4 import Tag

result = {'class': ['result-row']}
banner = {'class': ['ban', 'nearby']}

def get_search_query(url: str, search_path: str, query: str) -> str:
    """

    :param search_path:
    :param url:
    :param query:
    :return:
    """
    return f"{url}{search_path}{query.replace(' ', '+')}"


def tag_filter(tag: Tag) -> bool:
    """

    :param tag:
    :return:
    """
    return is_nearby_banner(tag) or is_result_item(tag)


def is_result_item(tag: Tag) -> bool:
    """

    :param tag:
    :return:
    """
    return tag.name == 'li' and tag.has_attr('class') and len(list(set(tag['class']) & set(result['class']))) > 0


def is_nearby_banner(tag: Tag) -> bool:
    """

    :param tag:
    :return:
    """
    return tag.name == 'h4' and tag.has_attr('class') and 'ban' in tag['class'] and 'nearby' in tag['class']


def get_tag_name(tag: Tag) -> str:
    """

    :param tag:
    :return:
    """
    return tag.name


def reduce_page_results(results_list: list) -> list:
    """

    :param results_list:
    :return:
    """
    return_list = []
    for tag in results_list:
        if tag.name == 'h4':
            break
        return_list.append(tag)
    return return_list
