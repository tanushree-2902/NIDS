# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime 
# import os.path
# import os

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Todo(db.Model):
#     sno = db.Column(db.Integer, primary_key = True)
#     title = db.Column(db.String(200), nullable = False)
#     desc = db.Column(db.String(500), nullable = False)
#     date_created = db.Column(db.DateTime, default= datetime.utcnow)

#     def __repr__(self) -> str:
#         return f"{self.sno} - {self.title}"
    
# with app.app_context():
#     db.create_all()

# if not os.path.exists(("/"+str(db.engine.url).strip("sqlite:///todo.db"))):
#     db.create_all()
# else:
#     print("database already exists")



# @app.route('/')
# def hello_world():
#     return render_template('index.html')
    

# @app.route('/products')
# def products():
#     return 'this is products page'

# if __name__ == "__main__":
#     app.run(debug=True, port =8000)


# # def create_app():
# #     app = Flask(__name__)

# #     with app.app_context():
# #         init_db()

# #     return app

# from flask import Flask, request, jsonify, render_template
# import pickle
# from pickle import load
# import numpy as np
# from sklearn import preprocessing
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()

# app = Flask(__name__)

# try:
#     # Attempt to load the model
#     model = pickle.load(open('classifier (1).pkl', 'rb'))
#     print("Model loaded successfully.")
# except Exception as e:
#     print("Failed to load model:", e)
#     model = None

# @app.route("/")
# def home():
#      return render_template("index.html")
 

# @app.route('/app_predict', methods=['POST'])
# def app_predict():
#  # Load the model
# #  model = pickle.load(open('classifier (1).pkl', 'rb'))
#  # Load the scaler
# #  scaler = load(open('scaler.pkl', 'rb'))
 
#  # Read the query parameters as an numpy array, and reshape it, so it's
#  # readable for the scaler and the model.
#  feature_list = request.form.to_dict()
#  feature_list = list(feature_list.values())
#  feature_list = list(map(int,feature_list()))
#  new_attack = np.array([request.args.get('srcip', type=float) ,
#                         request.args.get('sport', type=float) ,
#                         request.args.get('dstip', type=float),
#                         request.args.get('dsport', type=float) ,
#                         request.args.get('proto', type=float) ,
#                         request.args.get('state', type=float),
#                         request.args.get('dur', type=float),
#                         request.args.get('sbytes', type=float),
#                         request.args.get('dbytes', type=float),
#                         request.args.get('sttl', type=float),
#                         request.args.get('dttl', type=float),
#                         request.args.get('sloss ', type=float),
#                         request.args.get('dloss ', type=float),
#                         request.args.get('service', type=float),
#                         request.args.get('sload', type=float),
#                         request.args.get('dloss ', type=float),
#                         request.args.get('spkts', type=float),
#                         request.args.get('dpkts ', type=float),
#                         request.args.get('swin ', type=float),
#                         request.args.get('dwin ', type=float),
#                         request.args.get('stcpb ', type=float),
#                         request.args.get('dtcpb ', type=float),
#                         request.args.get('smeansz', type=float),
#                         request.args.get('dmeansz', type=float),
#                         request.args.get('trans_depth ', type=float),
#                         request.args.get('res_bdy_len', type=float),
#                         request.args.get('sjit', type=float),
#                         request.args.get('djit', type=float),
#                         request.args.get('stime', type=float),
#                         request.args.get('ltime', type=float),
#                         request.args.get('sintpkt', type=float),
#                         request.args.get('dintpkt', type=float),
#                         request.args.get('tcprtt', type=float),
#                         request.args.get('synack', type=float),
#                         request.args.get('ackdat', type=float),
#                         request.args.get('is_sm_ips_ports', type=float),
#                         request.args.get('ct_state_ttl', type=float),
#                         request.args.get('ct_flw_http_mthd ', type=float),
#                         request.args.get('is_ftp_login  ', type=float),
#                         request.args.get('ct_ftp_cmd', type=float),
#                         request.args.get('ct_srv_src', type=float),
#                         request.args.get('ct_srv_dst ', type=float),
#                         request.args.get(' ct_dst_ltm  ', type=float),
#                         request.args.get('ct_src_ltm ', type=float),
#                         request.args.get('ct_src_dport_ltm', type=float),
#                         request.args.get('ct_dst_sport_ltm', type=float),
#                         request.args.get('ct_dst_src_ltm ', type=float),
#                         request.args.get('attack_cat ', type=float),
#                        ]).reshape(1, -1)
     
# # Scale the new wine data, and predict if its good (1) or bad (0)
# #  new_attack_scaled = scaler.transform(new_attack)
#  prediction = model.predict(new_attack)
#  output = int(prediction[0])
#  if output == 1:
#    text = "attacked"
#  else:
#    text = "Not Attacked"

# # Return the prediction in a python list
# #  return prediction.tolist()
   
#  return render_template('index.html', prediction_text = 'The system is {}'.format(text))

# if __name__ == '__main__':
#  app.run(debug=True, port=5000)

from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

try:
    # Attempt to load the model
    model = pickle.load(open('ClassifierV1.pkl', 'rb'))
    print("Model loaded successfully.")
except Exception as e:
    print("Failed to load model:", e)
    model = None

@app.route('/api/predict', methods=['POST'])
def predict():
    global model
    if model is None:
        return jsonify({'error': 'Model not loaded.'}),  500
    
    # Get data from the POST request.
    data = request.get_json(force=True)
    
    # Make prediction using the loaded model
    prediction = model.predict([data['feature_vector']])
    
    # Return the prediction
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)