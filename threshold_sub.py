def threshold_sub(model,test,threshold):
    predicted = model.predict_proba(test)
    threshold = threshold
    classes = predicted[:,1]
    classes[classes >= threshold] = 1
    classes[classes < threshold] = 0
    predicted = classes
    sub = pd.DataFrame({'aaaa': predicted})
    sub['fr_yn'] = sub['fr_yn'].apply(lambda x: 'Y' if x == 1 else 'N')
    sub.to_csv('Submission.csv', index = False)
    print (sub['aaaaa'].value_counts())
###################################
threshold_sub(xgb_model,df_test,0.7)
