from flask import Flask, jsonify
from flask import request
  
app = Flask(__name__)

def process(content):
	results = []
	
	for show in content['payload']:
		if 'country' in show: #Additional check as 1 of the sample JSON was of a different format
			if show['drm'] == True and show['episodeCount'] > 0:
				results.append({"image": show['image']['showImage'], "slug": show['slug'], "title": show['title']})
	
	return {"response": results}



  
@app.route('/', methods = ['POST'])
def postJsonHandler():
    if not request.is_json:
    	return jsonify({"response": "Could not decode request: JSON parsing failed"})
    content = request.get_json()
    return jsonify(process(content))
    
# This method is to just check if the site is live
@app.route('/hello', methods = ['GET'])
def index():
	return ''' <h2> Hello! This site parses json and returns stuff on the main page. </h2>  '''  
app.run(host='0.0.0.0', port= 80) 
