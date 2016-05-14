from base import BaseTestAPI
import requests


class TestDeleteIssue(BaseTestAPI):
    
    def setUp(self):
        super().setUp()
        self.url = self.base_url + '/issue/'
    
    def test_delete_issue(self):
        issue_id = self.create_issue()
        
        url = self.url + issue_id
        r = requests.delete(url, cookies=self.cookies)
        r = requests.get(url, cookies=self.cookies)
        
        self.assertEqual(r.status_code, 404)
        
    def test_delete_unexistent_issue(self):
        issue_id = "ZZZ"
        
        url = self.url + issue_id
        r = requests.delete(url, cookies=self.cookies)

        self.assertEqual(r.status_code, 404)