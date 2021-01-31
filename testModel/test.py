#using the model saved from hard disk 
import pickle 
#import sklearn from tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
# load the model from disk
#filename = 'DTModel.pkl'
filename = 'RFModel.pkl'
loaded_model = pickle.load(open(filename, 'rb'))
P =[[9,31,51,205.25]]
print(loaded_model.predict(P))
P2 =[[2,5.8,17,36]]
print(loaded_model.predict(P2))
P3 = [[90.3,85.2,34.7,45.8]]
print(loaded_model.predict(P3))