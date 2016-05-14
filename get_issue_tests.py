import unittest
import requests
import xmltodict

from base import BaseTestAPI


class TestGetIssueCase(BaseTestAPI):
    '''
    TestCase containing tests for obtaining issues from Youtrack
    '''
    
    def setUp(self):
        super().setUp()
        self.url = self.base_url + '/issue/'
        self.issue = 'API-1'
    
    def test_get_issue(self):
        url = self.url + self.issue
        r = requests.get(url, cookies=self.cookies)
        
        self.assertEqual(r.status_code, 200, r.text)
        response_dict = xmltodict.parse(r.text)
        self.assertEqual(response_dict['issue']['@id'], self.issue)
        
        
    def test_get_nonexisted_issue(self):
        url = self.url + "ZZZ"
        r = requests.get(url, cookies=self.cookies)
        
        self.assertEqual(r.status_code, 404, r.text)