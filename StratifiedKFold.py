from sklearn.model_selection import *
from sklearn.metrics import *
import xgboost as xgb
from sklearn.externals import joblib

X = df_train.drop('labels',1)
Y = df_train[['labels']]

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    skf = StratifiedKFold(n_splits = 10, shuffle = True,random_state = 13)
    i = 1
    for train_index,test_index in skf.split(X,Y):
        print('{} of KFold {}'.format(i, skf.n_splits))
        xtr,xvl = X.iloc[train_index],X.iloc[test_index]
        ytr,yvl = Y.iloc[train_index],Y.iloc[test_index]

        xgb_model = xgb.XGBClassifier(objective="binary:logistic", learning_rate = 0.15, max_depth = 5,
                                     max_delta_step = 7, max_bin = 512, eval_metric = 'poisson-nloglik',
                                     random_state = 13)
        xgb_model.fit(xtr, ytr,
                    eval_set=[(xvl, yvl)],
                    verbose = False,
                    early_stopping_rounds = 1000)
        y_pred = xgb_model.predict(Test_X)
        predicted = [round(value) for value in y_pred]
        predicted = xgb_model.predict(val_X)
        print ('val_set - precision: {0}'.format(precision_score(val_Y,predicted)))
        print ('val_set - recall: {0}'.format(recall_score(val_Y,predicted)))
        print ('val_set - fl: {0}'.format(f1_score(val_Y,predicted)))
        if f1_score(val_Y,predicted) > 0.521:
            joblib.dump(xgb_model,f'{f1_score(val_Y,predicted)}_model.pkl')
            print (f'---------------->save___{f1_score(val_Y,predicted)}_model.pkl')
        i += 1
