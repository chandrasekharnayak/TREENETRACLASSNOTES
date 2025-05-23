import pytest
import json


@pytest.mark.usefixtures("browser_per_class")
class TestFacebookClass:

    def test_feed_count(self,browser_per_class):
        # fetch UL list help of find elements
        #count then length of list, and store expecetd feed count variable
        #evaluate with test_data , call the json data and count
    
    with open('test_data/test_json_data.json','r') as test_data:
        data = json.loads(test_data)
        actual_feeds_count = data['facebook_feeds_count']
        assert expected_feed_count == actual_feeds_count
        
    def test_feeds_all_names(self,browser_per_class):

        