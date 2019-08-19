import os
from flask import Flask, request
from tslearn.neighbors import KNeighborsTimeSeriesClassifier, KNeighborsTimeSeries
import pickle
import pandas as pd
app = Flask(__name__)

port = int(os.environ.get('PORT', 3000))
@app.route('/',methods = ['POST', 'GET'])
def hello():
	if request.method=='POST':

		#reading the test-file object from request
		if request.files['file'].filename == '':
			return 'No selected file'
		else:
			file = request.files['file']
			test_data = pd.read_csv(file)

			#loading the trained-model
			filename = 'knn_model.sav'
			loaded_model = pickle.load(open(filename, 'rb'))

			#predicting the output
			predicted_labels = loaded_model.predict(test_data[['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','x11','x12']].values)
		
			result = []
			for i in predicted_labels:
				if(i==1):
					result.append("Non-grape")
				else:
					result.append("Grape")
			return str(result)
	else:
		return "Time-series classfier API"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)