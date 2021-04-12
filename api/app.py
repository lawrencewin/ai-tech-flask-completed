import os
from flask import Flask, request, make_response, send_from_directory
import torch
import PIL
from model import Classifier, image_transform

app = Flask(__name__, static_folder="static")

# initialize model from path 
net = Classifier()
net.load_state_dict(torch.load("model.th", map_location=torch.device("cpu")))
net.eval() # IMPORTANT

# map of model outputs to ones we can understand
class_map = {
    0: "cat",
    1: "dog"
}

# outline routes

@app.route("/", methods=["GET"])
def hello_world(path):
    return "Hello World!"

@app.route("/classify", methods=["POST"])
def classify():
    output = "idk"
    probability = -1
    if "image" in request.files:
        f = request.files["image"]
        # open image and convert to tensor
        image = PIL.Image.open(f)
        as_tensor = image_transform(image)
        as_tensor = torch.unsqueeze(as_tensor, 0) # "batch" this
        # feed into our model and make prediction
        scores = net(as_tensor)
        pred = torch.argmax(scores, 1).item()
        probability = torch.softmax(scores, dim=1)[0][pred].item()
        output = class_map[pred] # maps from 0 / 1 to cat / dog
    return make_response({
        "type": output,
        "probability": probability
    })