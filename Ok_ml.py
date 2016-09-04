import numpy as np;
import pandas as pd;

from sklearn import tree;
from sklearn import linear_model
from sklearn import svm;

train_data = pd.read_csv('data.csv');

#cleaning
train_data['result'][train_data['result']=='ok']=1;
train_data['result'][train_data['result']=='not_ok']=0;
train_data['result'][train_data['result']=='hello']=2;

train_data['hand_type'][train_data['hand_type']=='Left hand']=0;
train_data['hand_type'][train_data['hand_type']=='Right hand']=1;
#print train_data;

target = train_data['result'];
target = np.array(target).astype(int);#set datatype for the array
features = train_data[['hand_type','thumb_direction_x','thumb_direction_y','index_direction_x','index_direction_y','middle_direction_x','middle_direction_y','ring_direction_x','ring_direction_y','pinky_direction_x','pinky_direction_y']].values;

#clf = tree.DecisionTreeClassifier(max_depth = 10, min_samples_split = 5, random_state = 1);
#print train_data.describe();
#my_tree = my_tree.fit(features,target);
#clf = linear_model.LogisticRegression() #initialize regressor
clf = svm.SVC(probability=True);

#clf.fit(features, target) #fit training data
clf.fit(features, target);
'''test1 = pd.read_csv('ok.csv');
test2 = pd.read_csv('not_ok.csv');
test3 = pd.read_csv('hello.csv');

test1['hand_type'][test1['hand_type']=='Left hand']=0;
test1['hand_type'][test1['hand_type']=='Right hand']=1;

test2['hand_type'][test2['hand_type']=='Left hand']=0;
test2['hand_type'][test2['hand_type']=='Right hand']=1;

test3['hand_type'][test3['hand_type']=='Left hand']=0;
test3['hand_type'][test3['hand_type']=='Right hand']=1;

test_features_1 = test1[['hand_type','thumb_direction_x','thumb_direction_y','index_direction_x','index_direction_y','middle_direction_x','middle_direction_y','ring_direction_x','ring_direction_y','pinky_direction_x','pinky_direction_y']].values;
test_features_2 = test2[['hand_type','thumb_direction_x','thumb_direction_y','index_direction_x','index_direction_y','middle_direction_x','middle_direction_y','ring_direction_x','ring_direction_y','pinky_direction_x','pinky_direction_y']].values;
test_features_3 = test3[['hand_type','thumb_direction_x','thumb_direction_y','index_direction_x','index_direction_y','middle_direction_x','middle_direction_y','ring_direction_x','ring_direction_y','pinky_direction_x','pinky_direction_y']].values;


prediction1 = clf.predict(test_features_1);
prediction2 = clf.predict(test_features_2);
prediction3 = clf.predict(test_features_3);
my_solution_1 = pd.DataFrame(prediction1, columns = ['result']);
my_solution_2 = pd.DataFrame(prediction2, columns = ['result']);
my_solution_3 = pd.DataFrame(prediction3, columns = ['result']);
my_solution_1.to_csv("my_solution_one.csv", index_label = ["id"]);
my_solution_2.to_csv("my_solution_two.csv", index_label = ["id"]);
my_solution_3.to_csv("my_solution_three.csv", index_label = ["id"]);
print my_solution_1;
#print(my_tree.feature_importances_);
#print(my_tree.score(features,target));
#print train_data.describe();
'''
