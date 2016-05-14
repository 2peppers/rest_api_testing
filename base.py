import unittest
import requests
import xmltodict
from yaml import load


class BaseTestAPI(unittest.TestCase):
    '''Base class for all test cases'''
    
    def setUp(self):
        self.settings = load(open('settings.yaml', 'r').read())
        self.base_url = self.settings['base_url']
        self.project = 'JJ'
        
        params = {
            'login': self.settings['credentials']['login'],
            'password': self.settings['credentials']['password'],
        }
        
        url = self.base_url + '/user/login'
        r = requests.post(url, data=params)
        self.cookies = r.cookies
        print ("Login status:", r.status_code)
            
    def create_issue(self):
        '''
        Create issue which we can later delete etc
        '''
        
        url = self.base_url + '/issue/'
        params = {
            'project': self.project,
            'summary': 'test issue by robots',
            'description': 'Hello World Yo!'
        }
        r = requests.put(url, data=params, cookies=self.cookies)
        location = r.headers['Location']
        issue_id = location.split('/')[-1]
        
        return issue_id

