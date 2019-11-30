from sklearn.model_selection import *
from sklearn.metrics import *
import matplotlib.pyplot as plt

import xgboost as xgb
from xgboost import plot_importance
import lightgbm as lgb
from sklearn.ensemble import VotingClassifier 

Train_X,Test_X,Train_Y,Test_Y = train_test_split(X, Y, test_size = 0.1, random_state = 13)

xgb_model = xgb.XGBClassifier(objective="binary:logistic", learning_rate = 0.15, max_depth = 5,
                             max_delta_step = 7, max_bin = 512, eval_metric = 'poisson-nloglik',
                             random_state = 13, tree_method = 'gpu_hist')
xgb_model.fit(Train_X, Train_Y,
            eval_set=[(Test_X, Test_Y)],
            verbose = False,
            early_stopping_rounds = 1000)
y_pred = xgb_model.predict(Test_X)
predicted = [round(value) for value in y_pred]
predicted = xgb_model.predict(val_X)
print ('val_set - precision: {0}'.format(precision_score(val_Y,predicted)))
print ('val_set - recall: {0}'.format(recall_score(val_Y,predicted)))
print ('val_set - fl: {0}'.format(f1_score(val_Y,predicted)))
print ('------------------------------------------')
lgb_model = lgb.LGBMClassifier(objective='binary', boosting_type='gbdt',learning_rate = 0.15, n_estimators = 60,
                               max_bin = 225, metric='auc', num_leaves = 17,default = 'is_unbalance',
                               random_state = 13, tree_method = 'gpu_hist')
lgb_model.fit(Train_X, Train_Y,
            eval_set=[(Test_X, Test_Y)],
            verbose = False,
            early_stopping_rounds = 1000)
y_pred = lgb_model.predict(Test_X)
predicted = [round(value) for value in y_pred]
predicted = lgb_model.predict(val_X)
print ('val_set - precision: {0}'.format(precision_score(val_Y,predicted)))
print ('val_set - recall: {0}'.format(recall_score(val_Y,predicted)))
print ('val_set - fl: {0}'.format(f1_score(val_Y,predicted)))
print ('------------------------------------------')
vo_model = VotingClassifier(estimators = [('XGB', xgb_model),('LGBM', lgb_model)],
                          voting = 'soft')
vo_model.fit(Train_X, Train_Y)
y_pred = vo_model.predict(Test_X)
predicted = [round(value) for value in y_pred]
print ('train_set - precision: {0}'.format(precision_score(Test_Y,predicted)))
print ('train_set - recall: {0}'.format(recall_score(Test_Y,predicted)))
print ('train_set - fl: {0}'.format(f1_score(Test_Y,predicted)))
print ('---------------------------------------------------------------')
predicted = vo_model.predict(val_X)
print ('val_set - precision: {0}'.format(precision_score(val_Y,predicted)))
print ('val_set - recall: {0}'.format(recall_score(val_Y,predicted)))
print ('val_set - fl: {0}'.format(f1_score(val_Y,predicted)))
print ('---------------------------------------------------------------')
ax = plot_importance(xgb_model, max_num_features = 15)
fig = ax.figure
fig.patch.set_facecolor('xkcd:white')
plt.show()
