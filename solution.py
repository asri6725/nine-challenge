from flask import Flask, jsonify, json
from flask import request
from werkzeug.exceptions import HTTPException

  
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
    

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "response": "Could not decode request: JSON parsing failed"
    })
    response.content_type = "application/json"
    return response
app.run(host='0.0.0.0', port= 80) 
