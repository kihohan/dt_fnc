from sklearn.model_selection import *
from sklearn.metrics import *
import lightgbm as lgb
from sklearn.externals import joblib

X = df_train.drop('fr_yn',1)
Y = df_train[['fr_yn']]

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    skf = StratifiedKFold(n_splits = 10, shuffle = True,random_state = 13)
    i = 1
    for train_index,test_index in skf.split(X,Y):
        print('{} of KFold {}'.format(i, skf.n_splits))
        xtr,xvl = X.iloc[train_index],X.iloc[test_index]
        ytr,yvl = Y.iloc[train_index],Y.iloc[test_index]

        lgb_model = lgb.LGBMClassifier(objective='binary', boosting_type='gbdt',learning_rate = 0.15,
                                       n_estimators = 60,
                                       max_bin = 225, metric='auc', num_leaves = 17,default = 'is_unbalance',
                                       random_state = 13,tree_method='gpu_exact')
        lgb_model.fit(xtr,ytr,
                    eval_set=[(xvl,yvl)],
                    verbose = False,
                    early_stopping_rounds = 1000)
        y_pred = lgb_model.predict(Test_X)
        predicted = [round(value) for value in y_pred]
        predicted = lgb_model.predict(val_X)
        print ('val_set - accuaracy: {0}'.format(accuracy_score(val_Y,predicted)))
        print ('val_set - precision: {0}'.format(precision_score(val_Y,predicted)))
        print ('val_set - recall: {0}'.format(recall_score(val_Y,predicted)))
        print ('val_set - fl: {0}'.format(f1_score(val_Y,predicted)))
        # joblib.dump(model,f'{score}_model.pkl')
        i += 1
