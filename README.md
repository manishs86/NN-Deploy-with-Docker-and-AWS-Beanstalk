# Neural Network Deploy with Docker and AWS Beanstalk
How to deploy a voice sentiment prediction model with docker, flask, keras and AWS.

[How the app will look like](/docs/1.jpg?raw=true): 

This is an example of deploying a multi-class classification keras model with Docker, Flask and AWS elastic beanstalk. It will cover basically the main project structure: Docker, Flask and recorder, since for AWS side you need to check their steps (for creating a new application and docker environment + and after just archive/compress the project folder contents and upload on beanstalk). Data sets used, transforms(mfccs/librosa) and keras model built(CNN1 & CNN2): hopefully will come soon on one of my blogs.

<p>
    <img src="/docs/2.png" width="220" height="240" />
</p>

I have uploaded above the whole project so you can give it a try/run and change where you find appropiate for your own project:

- *application.py*: the flask application
- *commons*: all the background functions needed to transform the wav data requested from users and predict
- *requirements*: libraries needed for docker image building
- *Dockerfile*: contains all the commands to assemble an image, reads also from requirements.txt.
- *my_sentimental_model.h5*: saved keras model to be used
- *labels.pkl*: a pickle with the labels used for reasigning labels to prediction results
- *static/style.css*: the style sheet for html
- *static/scripts/js's*: javascripts needed for voice recorder
- *templates/index.html*: the page that will host the recorder and the prediction result
- *uploads/*: where the wav's will be saved for further processing

Hope this example helps with your future voice sentiment deploys.

Good luck,

Daniel
