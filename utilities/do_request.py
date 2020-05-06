import requests
from requests.auth import HTTPBasicAuth
class DoRequest:
    basic_auth = ('username', 'password')
    def get_expect_200(self, url, page_number):
        query = {'page': page_number}
        headers = {"User-Agent": "secret agent 0.07"}
        response =requests.get(url, params=query, headers=headers )
        assert response.status_code == 200, "Response code expected is 200 but found: " + str(response.status_code)
        return response.json()

    def get_with_authentication(self, url, page_number):
        query = {'page': page_number}
        headers = {"User-Agent": "secret agent 0.07"}
        return requests.get(url, params=query, headers=headers, auth=self.basic_auth ).json()

    def post_expect_201(self, url, payload):
        response = requests.post(url, data=payload)
        assert response.status_code == 201, "Response code expected is 201 but found: "+ str(response.status_code)
        return response.json()

    def delete_expect_204(self, url, user_id):
        response = requests.delete(url+ "/"+ str(user_id))
        assert response.status_code == 204, "Response code expected is 204 but found: "+ str(response.status_code)
        return response

