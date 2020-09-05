
import json
import tensorflow as tf
import numpy as np
import random
from flask import Flask,request

app=Flask(__name__)

model=tf.keras.models.load_model("model.h5")

feature_model=tf.keras.models.Model(model.inputs,
                                   [layer.output for layer in model.layers])

_,(x_test,_)=tf.keras.datasets.mnist.load_data()
x_test=x_test/255.

def get_prediction():
    index=np.random.choice(x_test.shape[0])
    image=x_test[index,:,:]
    image_arr=np.reshape(image,(1,784))
    return image       #feature_model.predict(image_arr),

@app.route('/',methods=['get','post'])
def index():
    if request.method=='post':
        image=get_prediction()  #preds,
        final_preds=[p.tolist() for  p in preds]
        return json.dumps({'image':image})
    return "welcome to the model server"
@app.route("/hello")
def hello():
    return "hello ,this is second route" 

if __name__=='__main__':
    app.run()
