# Unsupervised Feature Learning with Autoencoder
# Author: Qi Liu
# Date: 2017-09-18
# Reference: https://blog.keras.io/building-autoencoders-in-keras.html

from keras.layers import Input, Dense, LSTM, RepeatVector
from keras.models import Model
from keras import regularizers
from keras.models import Sequential
import numpy as np
from keras.layers.core import Dropout
import pandas as pd
from sklearn import preprocessing
import time
from keras.models import load_model

from keras.layers import advanced_activations

train_new = 1
good = 1
iters = 4

# this is the size of our encoded representations
input_dim = 1

'''
inputs = Input(shape=(1, input_dim))
encoded = LSTM(latent_dim)(inputs)

decoded = RepeatVector(1)(encoded)
decoded = LSTM(input_dim, return_sequences=True)(decoded)

autoencoder = Model(inputs, decoded)
encoder = Model(inputs, encoded)
'''
select_only_last_state = 0
hidden_dim = 1
window_length = 1

autoencoder = Sequential()
if select_only_last_state:
    autoencoder.add(LSTM(hidden_dim, input_shape=(window_length, input_dim), return_sequences=False))
    autoencoder.add(RepeatVector(window_length))
else:
    autoencoder.add(LSTM(hidden_dim, input_shape=(window_length, input_dim), return_sequences=True, activation = 'linear'))
    #act = advanced_activations.PReLU(init='zero', weights=None)
    #autoencoder.add(act)
    #autoencoder.add(Dropout(p=0.15))
    autoencoder.add(LSTM(1, return_sequences=True, activation='linear'))

'''
# Sparsity coding
# add a Dense layer with a L1 activity regularizer
encoded = Dense(encoding_dim, activation='relu',
                activity_regularizer=regularizers.l1(10e-5))(input_img)
decoded = Dense(784, activation='sigmoid')(encoded)

autoencoder = Model(input_img, decoded)
'''

'''
# Simplest
# "encoded" is the encoded representation of the input
encoded = Dense(encoding_dim, activation='relu')(input_img)
# "decoded" is the lossy reconstruction of the input
decoded = Dense(784, activation='sigmoid')(encoded)

# this model maps an input to its reconstruction
autoencoder = Model(input_img, decoded)
'''
#adadelta
autoencoder.compile(optimizer='rmsprop', loss='mean_squared_error')# loss='mean_squared_error'

# read excel data

if good == 1:
    df = pd.read_excel('E:/myprojects/pv_detection/data/model_fault_0912/data1802_0920_normal.xlsx')
    modelFile = 'E:/myprojects/pv_detection/data/model_fault_0912/goodModel_linear.h5'
    x_train = df.iloc[0:8000,0:2].as_matrix()
    x_test = df.iloc[8000:,0:2].as_matrix()
else:
    df = pd.read_excel('E:/myprojects/pv_detection/data/model_fault_0912/data1802_0920_bad.xlsx')
    modelFile = 'E:/myprojects/pv_detection/data/model_fault_0912/goodModel_linear.h5'
    x_train = df.iloc[0:35000,0:2].as_matrix()
    x_test = df.iloc[35000:,0:2].as_matrix()
    
#x_train = preprocessing.scale(x_train)
#x_test = preprocessing.scale(x_test)

x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

x_train_x = x_train[:,0]
x_test_x = x_test[:,0]

x_train_x = preprocessing.scale(x_train_x)
x_test_x = preprocessing.scale(x_test_x)

x_train_y = x_train[:,1]
x_test_y = x_test[:,1]

x_train_ex = np.expand_dims(x_train_x, axis=1)
x_test_ex = np.expand_dims(x_test_x, axis=1)

x_train_xex = np.expand_dims(x_train_ex, axis=1)
x_test_xex = np.expand_dims(x_test_ex, axis=1)

x_train_yex = np.expand_dims(x_train_y, axis=1)
x_test_yex = np.expand_dims(x_test_y, axis=1)

x_train_yex = np.expand_dims(x_train_yex, axis=1)
x_test_yex = np.expand_dims(x_test_yex, axis=1)

print(x_train_yex.shape)
print(x_test_yex.shape)

start = time.time()

if train_new == 1:
    autoencoder.fit(x_train_xex, x_train_yex,
                    epochs=iters,
                    batch_size=10,
                    shuffle=True,
                    validation_data=(x_test_xex, x_test_yex))
                    
    
    autoencoder.save(modelFile)
else:
    autoencoder = load_model(modelFile)
 
'''
for idx,layer in enumerate(autoencoder.layers):
    weights = layer.get_weights()
    print('Layer: ', idx, 'Weights:', weights)
    '''
                               
decoded_imgs = autoencoder.predict(x_train_xex)

end = time.time()
runtime = end - start
msg = "AutoEncoder Single-Processing Took {time} seconds to complete"
print(msg.format(time=runtime))                

print(decoded_imgs.shape)


import matplotlib.pyplot as plt

n = 2  # how many digits we will display
plt.figure(figsize=(20, 4))

#ax = plt.subplot(1,2,1)
plt.plot(x_train[:,1],color='blue',label='Test Abnormal Data')
plt.plot(decoded_imgs[:,:,0],color='red',label='Test Expected Data')

plt.xlabel('Time (min)')
plt.ylabel('Current (A)')
plt.title('Modeling with LSTM')

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.07),fancybox=True, shadow=True, ncol=5)

'''
ax = plt.subplot(1,2,2)
plt.plot(x_test[:,1],color='blue')
plt.plot(decoded_imgs[:,:,1],color='red')


ax = plt.subplot(2,2,3)
plt.plot(x_test[:,2],color='blue')
plt.plot(decoded_imgs[:,:,2],color='red')

ax = plt.subplot(2,2,4)
plt.plot(x_test[:,3],color='blue')
plt.plot(decoded_imgs[:,:,3],color='red')
'''

plt.show()


'''
from keras.datasets import mnist
import numpy as np
(x_train, _), (x_test, _) = mnist.load_data()

x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

print(x_train.shape)
print(x_test.shape)

autoencoder.fit(x_train, x_train,
                epochs=50,
                batch_size=256,
                shuffle=True,
                validation_data=(x_test, x_test))
                
# encode and decode some digits
# note that we take them from the *test* set
encoded_imgs = encoder.predict(x_test)
decoded_imgs = decoder.predict(encoded_imgs)
'''

# use Matplotlib (don't ask)
'''
import matplotlib.pyplot as plt

n = 10  # how many digits we will display
plt.figure(figsize=(20, 4))
for i in range(n):
    # display original
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(x_test[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # display reconstruction
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_imgs[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()
'''