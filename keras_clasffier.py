
import numpy as np 
import matplotlib.pyplot as plt

from sklearn.model_selection import *
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

import keras 
from keras import models
from keras.layers import Dense, Dropout
from keras.utils import to_categorical

X = df.drop('labels',1)
Y = df['labels']
Train_X,Test_X,Train_Y,Test_Y = train_test_split(X, Y, test_size = 0.1, random_state = 13)

X = np.array(X,dtype = 'f')

LE = LabelEncoder()
LE.fit(Y)
encoded_label = LE.transform(Y)
Y = to_categorical(encoded_label, dtype='float16')
################################################
n_samples, n_features = X.shape
n_samples, n_targets = Y.shape

# --- neural network configuration
model = models.Sequential()
model.add(Dense(128, activation='relu', input_shape=(n_features,)))
model.add(Dropout(0.5))
model.add(Dense(256, activation='sigmoid'))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(n_targets, activation='softmax'))

# --- load model from previous training as initial weights : TEST PURPOSE
#model.load_weights('model_ap_master.hd5')

callbacks_list = [ 
    keras.callbacks.EarlyStopping( 
        monitor='val_accuracy', 
        patience = 50, 
    ),
    keras.callbacks.ModelCheckpoint( 
        filepath='sulwhasoo', 
        monitor='val_accuracy',
        save_best_only=True 
    ),
#     keras.callbacks.TensorBoard(
#         log_dir='TensorBoard', 
#         histogram_freq=1, 
#         #embeddings_freq=1, 
#     )    
]


# --- training
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(
    X, Y, 
    epochs = 500, 
    batch_size=3000, 
    validation_split=0.20,
    callbacks = callbacks_list,
    verbose = False
)

# from keras.utils import plot_model
# plot_model(model, show_shapes=True, to_file='model_ap_master.png')

# --- plot 
loss = history.history['loss']
val_loss = history.history['val_loss']
acc = history.history['acc']
val_acc = history.history['val_acc']

epochs = range(1, len(loss) + 1)

plt.figure(figsize = (13,5))
plt.subplot(1,2,1)
plt.plot(epochs, loss, 'r', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.subplot(1,2,2)
plt.plot(epochs, acc, 'r', label='accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Accuracy and Validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()
plt.close()

def deep_sub(model,test):
    predicted = model.predict(np.array(test))
    sub = pd.DataFrame({'label': predicted.argmax(1)})
    sub['label'] = sub['label'].apply(lambda x: 'Y' if x == 1 else 'N')
    sub.to_csv('Submission.csv', index = False)
    print (sub['label'].value_counts())
