# https://datascience.stackexchange.com/questions/34209/xgboost-quantifying-feature-importances
from xgboost import plot_importance

ax = plot_importance(xgb_model, max_num_features = 15,importance_type='weight')
fig = ax.figure
fig.patch.set_facecolor('xkcd:white')
plt.show()

feature_importance = xgb_model.get_booster().get_fscore()
df_feature = pd.DataFrame(pd.Series(feature_importance, index = feature_importance.keys()),columns = ['cnt'])
df_feature = df_feature.sort_values(by = 'cnt', ascending = False)
feature_3 = list (df_feature[df_feature['cnt'] > 3].index)
