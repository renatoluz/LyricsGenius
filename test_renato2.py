import requests
import urllib2

# Format a request URI for the Genius API
search_term = 'Andy Shauf'
_URL_API = "https://api.genius.com/"
_URL_SEARCH = "search?q="
querystring = _URL_API + _URL_SEARCH + urllib2.quote(search_term)
request = urllib2.Request(querystring)
request.add_header("Authorization", "Bearer " + client_access_token)
request.add_header("User-Agent", "")

response = urllib2.urlopen(request, timeout=3)
json_obj = response.json()
