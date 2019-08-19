# time-series-classifier-flaskapp

## Introduction
This is an implementation of Grape vs Non-grape time-series classifier.
It's basically a flask-app which exposes an API to use the classifier.
Check sample input-file(also train-test data) for the specified file-format(```dataset is in time-series-dataset.zip```)

### Prerequisites
You need to have trained-model saved in this app-directory.(There is already saved model present in the directory, you can train new model by looking at ```time-series-classifier.ipynb```)

### Deployment
```manifest.yml``` and ```environment.yml``` contains deployment configurations and dependencies. </br>
 
 To deploy application use : ```cf push```
 
### Testing thr API
To use this API make a POST call from rest-client with the input file.
The body of the post call should contain ```key: file``` and ```value:``` should be uploaded file.
URL will be the app's url only.(No specific paths)
