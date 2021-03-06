# Unsupervised Feature Learning with Autoencoder
# Author: Qi Liu
# Date: 2017-09-18
# Reference: https://blog.keras.io/building-autoencoders-in-keras.html

from keras.layers import Input, Dense
from keras.models import Model
from keras import regularizers
import numpy as np
import pandas as pd
from sklearn import preprocessing
import time
from keras.models import load_model

train_new = 1

# this is the size of our encoded representations
encoding_dim = 2  # 2 floats -> compression of factor 24.5, assuming the input is 784 floats
input_dim = 2
# this is our input placeholder
input_img = Input(shape=(input_dim,))

encoded = Dense(3, activation='relu')(input_img)
#encoded = Dense(5, activation='relu')(encoded)
#encoded = Dense(3, activation='relu')(encoded)

encoded = Dense(encoding_dim, activation='relu')(encoded)

decoded = Dense(3, activation='relu')(encoded)
#decoded = Dense(5, activation='relu')(decoded)
#decoded = Dense(8, activation='relu')(decoded)

decoded = Dense(input_dim, activation='sigmoid')(decoded)

autoencoder = Model(input_img, decoded)

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
autoencoder.compile(optimizer='adam', loss='mean_squared_error')# loss='mean_squared_error'

# read excel data
good = 1

if good ==1:
    df = pd.read_excel('E:/myprojects/pv_detection/data/model_fault_0912/data1802_0920_normal.xlsx')
    x_train = df.iloc[0:8000,0:2].as_matrix()
    x_test = df.iloc[8000:,0:2].as_matrix()
else:
    df = pd.read_excel('E:/myprojects/pv_detection/data/model_fault_0912/data1802_0920_bad.xlsx')
    x_train = df.iloc[0:35000,0:2].as_matrix()
    x_test = df.iloc[35000:,0:2].as_matrix()
    
x_train = preprocessing.scale(x_train)
x_test = preprocessing.scale(x_test)

x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

print(x_train.shape)
print(x_test.shape)

start = time.time()
modelFile = 'E:/myprojects/pv_detection/data/model_fault_0912/normalModel.h5'

if train_new == 1:
    autoencoder.fit(x_train, x_train,
                    epochs=50,
                    batch_size=10,
                    shuffle=True,
                    validation_data=(x_test, x_test))
                    
    
    autoencoder.save(modelFile)
else:
    autoencoder = load_model(modelFile)
 
for idx,layer in enumerate(autoencoder.layers):
    weights = layer.get_weights()
    print('Layer: ', idx, 'Weights:', weights)
                               
decoded_imgs = autoencoder.predict(x_test)

end = time.time()
runtime = end - start
msg = "AutoEncoder Single-Processing Took {time} seconds to complete"
print(msg.format(time=runtime))                

print(decoded_imgs.shape)


import matplotlib.pyplot as plt

n = 2  # how many digits we will display
plt.figure(figsize=(20, 4))

ax = plt.subplot(2,2,1)
plt.plot(x_test[:,0],color='blue')
plt.plot(decoded_imgs[:,0],color='red')

ax = plt.subplot(2,2,2)
plt.plot(x_test[:,1],color='blue')
plt.plot(decoded_imgs[:,1],color='red')
'''
ax = plt.subplot(2,2,3)
plt.plot(x_test[:,2],color='blue')
plt.plot(decoded_imgs[:,2],color='red')

ax = plt.subplot(2,2,4)
plt.plot(x_test[:,3],color='blue')
plt.plot(decoded_imgs[:,3],color='red')
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