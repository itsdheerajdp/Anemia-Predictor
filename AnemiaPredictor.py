

import pickle
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator


train_datagen = ImageDataGenerator( 
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
training_set = train_datagen.flow_from_directory(
        'dataset/training_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')




test_datagen = ImageDataGenerator(rescale=1./255)
test_set = test_datagen.flow_from_directory(
        'dataset/test_set',
        target_size=(64, 64),
        batch_size=32,#it means 32 images in a batch
        class_mode='binary')




cnn=tf.keras.models.Sequential()




cnn.add(tf.keras.layers.Conv2D(filters=32,kernel_size=3,activation='relu',input_shape=[64,64,3]))




cnn.add(tf.keras.layers.MaxPool2D(pool_size=(2,2),strides=2))




cnn.add(tf.keras.layers.Conv2D(filters=32,kernel_size=3,activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=(2,2),strides=2))



cnn.add(tf.keras.layers.Flatten())



cnn.add(tf.keras.layers.Dense(units=128,activation='relu'))



cnn.add(tf.keras.layers.Dense(units=1,activation='sigmoid'))



cnn.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])



cnn.fit(x=training_set,validation_data=test_set,epochs=30)





training_set.class_indices


pickle.dump(cnn, open("AnemiaPredictor.pkl","wb"))