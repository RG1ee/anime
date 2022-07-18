from pprint import pprint
import requests
# import json

# a = requests.get('https://api.jikan.moe/v4/anime/')
# json_data = json.loads(a.text)

# # pprint(json_data)

# Here we define our query as a multi-line string
query = '''
query ($id: Int) { # Define which variables will be used in the query (id)
  Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
    id
    title {
      romaji
      english
      native
    }
  }
}
'''

# Define our query variables and values that will be used in the query request
variables = {
    'id': 15125
}

url = 'https://graphql.anilist.co'

# Make the HTTP Api request
response = requests.post(url, json={'query': query, 'variables': variables})
pprint(response['response'])