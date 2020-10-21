from flask import Flask
from flask import request
  
app = Flask(__name__)

def process(content):
	print("The type of parsed JSON is: ", type(content['payload']))
	print("The type of individual show is: ", type(content['payload'][0]))
	results = []
	count = 0
	for show in content['payload']:
		if 'country' in show:
			if show['drm'] == True and show['episodeCount'] > 0:
				results.append({"image": show['image']['showImage'], "slug": show['slug'], "title": show['title']})
				#print("image: " , show['image']['showImage'], "; slug: ", show['slug'], "; title", show['title'])

	return {"response": results}



  
@app.route('/', methods = ['POST'])
def postJsonHandler():
    if not request.is_json:
    	return {"response": "Could not decode request: JSON parsing failed"}
    content = request.get_json()
    return process(content)
    

@app.route('/hello', methods = ['GET'])
def index():
	return ''' <h2> Hello! This site parses json and returns stuff on the main page. </h2>  '''  
app.run(host='127.0.0.1', port= 8090) # host='0.0.0.0', port= 443