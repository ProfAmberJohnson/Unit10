# Amber Johnson
# CSC256.0002 FA21
import requests
import pytest

url_ddg = "https://api.duckduckgo.com"


@pytest.mark.parametrize("president", ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Buren", "Harrison",
                                       "Tyler", "Polk", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Hayes",
                                       "Garfield", "Arthur", "Cleveland", "McKinley", "Roosevelt", "Taft", "Harding",
                                       "Coolidge", "Hoover", "Truman", "Eisenhower", "Kennedy", "Nixon", "Ford",
                                       "Carter", "Reagan", "Bush", "Clinton", "Obama", "Trump", "Biden"])
def test_presidents(president):
    resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json&pretty=1")
    rsp_data = resp.json()
    topics_list = []
    for topic in rsp_data["RelatedTopics"]:
        topics_list.append(topic["FirstURL"])
    if any(president in string for string in topics_list):
        assert True
    else:
        assert False


