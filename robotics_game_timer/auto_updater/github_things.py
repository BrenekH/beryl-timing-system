import os
from gql_py import Gql

gql = Gql(api='https://api.github.com/graphql')

class Repository:
	def __init__(self, owner, repo_name, api_key):
		self.owner = owner
		self.repo_name = repo_name
		self.api_key = api_key

		self.headers = {"Authorization": f"bearer {self.api_key}"}

	def get_latest_tag(self):
		# This string is super ugly, but I don't care
		query_string = '''
query {
  repository(owner:"''' + self.owner + '''", name:"''' + self.repo_name + '''") {
    releases(last: 1) {
      nodes {
        tagName
      }
    }
  }
}
'''
		response = gql.send(query=query_string, headers=self.headers)
		if response.errors == None and response.ok:
			return (True, response.data['repository']['releases']['nodes'][0]['tagName'])
		else:
			return (False, None)

	def get_resource_from_latest_release(self, resource_name, target_path):
		return "Not Implemented"