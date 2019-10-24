import io
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import flask
from flask import request
import requests
from keras.preprocessing import image
model=None


app = flask.Flask(__name__)



def load():
    global model
    model = load_model(filepath='nsfw.h5')
    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

load()




@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the
    data = {"success":"Unknown"}

    if flask.request.method == "POST":
        if flask.request.form.values():
            url=[x for x in request.form.values()]
            url=url[0]
            BASE = 'https://render-tron.appspot.com/screenshot/'
            path = 'target.jpg'
            response = requests.get(BASE + url, stream=True)
            if response.status_code != 200:
                status="url render failed"
            if response.status_code == 200:
                with open(path, 'wb') as file:
                    for chunk in response:
                        file.write(chunk)
            test_image = image.load_img('target.jpg', target_size = (64, 64)) 
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis = 0)
            result = model.predict(test_image)
            categories=['safe','not safe - contains Adult content']
            status=categories[int(result[0][0])]
            data['URL_response']=response.status_code
            if response.status_code != 200:
                status="url render failed"
            data["status"] = status


    return flask.jsonify(data)


@app.route("/", methods=["POST", "GET"])
def home():
    data = {"status":" Unknown"}

    if request.method == "GET":
        return """
        <!doctype html>
        <title>Website NSFW Classification</title>
        <h1>URL NSFW Classification</h1>
        <h3>CNN model trained on images to classify website by its UI</h3>
        <strong>Note:</strong> input should be given with protocol (http:// or https:// ) output will be in JSON format
        <form method=post enctype=multipart/form-data>
        <p><input type=text name=file>
            <input type=submit value=url image>
        </form>
        """


    if flask.request.method == "POST":
        if flask.request.form.values():
            url=[x for x in request.form.values()]
            url=url[0]
            BASE = 'https://render-tron.appspot.com/screenshot/'
            path = 'target.jpg'
            response = requests.get(BASE + url, stream=True)
            if response.status_code != 200:
                status="url render failed"
            if response.status_code == 200:
                with open(path, 'wb') as file:
                    for chunk in response:
                        file.write(chunk)
            test_image = image.load_img('target.jpg', target_size = (64, 64)) 
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis = 0)
            result = model.predict(test_image)
            categories=['safe','not safe - cointains adult content']
            status=categories[int(result[0][0])]
            data['URL_response']=response.status_code
            if response.status_code != 200:
                status="url render failed"
            data["status"] = status


    return flask.jsonify(data)


if __name__ == "__main__":
    print(
        (
            "Please wait while server loading.."
        )
    )

    load()
    app.run()
