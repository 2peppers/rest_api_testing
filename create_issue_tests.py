from base import BaseTestAPI
import requests

class TestCreateIssue(BaseTestAPI):
    def test_create_issue(self):
        url = self.base_url + '/issue/'
        params = {
            'project': self.project,
            'summary': "New issue for testing!",
            'description': 'Cool mega issue<br>\nfor testing'
        }
        
        r = requests.put(url, data=params, cookies=self.cookies)
        issue_id = r.headers['Location'].split('/')[-1]
        
        self.assertEqual(r.status_code, 201)
        
        get_url = self.base_url + '/issue/' + issue_id
        r = requests.get(url, cookies=self.cookies)
        self.assertEqual(r.status_code, 200)