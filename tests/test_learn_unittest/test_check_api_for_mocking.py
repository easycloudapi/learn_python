import os
import sys
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

root_dir = os.getcwd()
sys.path.append(root_dir)

from learn_unittest.check_api_for_mocking import _get_only_joke
from learn_unittest.check_api_for_mocking import _call_api_randomjoke


class TestGetOnlyJoke(unittest.TestCase):
    @patch('learn_unittest.check_api_for_mocking._call_api_randomjoke')
    def test_get_only_joke_call_once(self, mock_call_api_randomjoke):
        mock_call_api_randomjoke.return_value = {"setup": "difference of Senseless and Nonsense", 
                                                 "punchline": "both have no sense"}
        expected_result = ("difference of Senseless and Nonsense" +
                           ", " +
                           "both have no sense")
        actual_result = _get_only_joke()

        self.assertEqual(expected_result, actual_result)


    @patch('learn_unittest.check_api_for_mocking._call_api_randomjoke')
    def test_get_only_joke_call_key_error(self, mock_call_api_randomjoke):
        mock_call_api_randomjoke.return_value = {"wrong_setup": "difference of Senseless and Nonsense", 
                                                 "wrong_punchline": "both have no sense"}
        
        self.assertRaises(KeyError, _get_only_joke)


    def test_get_only_joke_call_type_error(self):       
        self.assertRaises(TypeError, _get_only_joke, "joke_name")


class TestCallApiRandomJoke(unittest.TestCase):
    @patch('learn_unittest.check_api_for_mocking.requests')
    def test_call_api_randomjoke_calls_once(self, mock_request):

        expected_result = {'type': 'general', 
                           'setup': 'How does the moon cut his hair?', 
                           'punchline': 'Eclipse it.', 
                           'id': 137}
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_result
        mock_request.get.return_value = mock_response
        
        actual_result = _call_api_randomjoke()

        self.assertEqual(expected_result, actual_result)


    @patch('learn_unittest.check_api_for_mocking.requests')
    def test_call_api_randomjoke_exception_400(self, mock_request):
        
        mock_request.status_code = 400

        self.assertRaises(Exception, _call_api_randomjoke)
        


if __name__ == "__main__":
    unittest.main()
