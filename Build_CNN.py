import numpy as np
X = X.to_numpy().reshape(X.shape[0], X.shape[1], 1)
Y = Y.to_numpy()
##############################
import keras
from keras.models import Sequential
from keras.callbacks import EarlyStopping
from keras.layers import Dense, Dropout,Flatten,Conv1D, MaxPool1D
from sklearn.model_selection import KFold
from keras.layers.normalization import BatchNormalization
from keras.optimizers import Adam

model = Sequential()
model.add(Conv1D(32, 2, activation='relu', input_shape = X[0].shape))
model.add(BatchNormalization())
# model.add(MaxPool1D(2))
model.add(Dropout(0.2))

model.add(Conv1D(64, 2, activation='relu'))
model.add(BatchNormalization())
# model.add(MaxPool1D(2))
model.add(Dropout(0.5))

model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(1, activation='sigmoid'))

callbacks_list = [ 
    keras.callbacks.EarlyStopping( 
        monitor = 'val_accuracy', 
        patience = 10, 
    ),
    keras.callbacks.ModelCheckpoint( 
        filepath='model', 
        monitor = 'val_accuracy',
        save_best_only = True 
    ),
]
# --- training
model.compile(optimizer=Adam(lr=0.0001), loss = 'binary_crossentropy', metrics=['accuracy'])
history = model.fit(
    X, Y, 
    epochs = 50, 
    batch_size = 500, 
    validation_split = 0.30,
    callbacks = callbacks_list,
    verbose = False
)
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
