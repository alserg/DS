from tensorflow.keras.layers import Dense,Conv2D,AvgPool2D,MaxPooling2D,Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np

def load_train(path):
    datagen = ImageDataGenerator(
        rescale=1./255,
		rotation_range=90,
		horizontal_flip=True
    )
    train_datagen_flow = datagen.flow_from_directory(
        path,
        target_size=(150, 150),
        batch_size=32,
        class_mode='sparse',
        seed=12345
    )
    return train_datagen_flow

def create_model(input_shape):
    
    optimizer = Adam(learning_rate=0.0001)
    model = Sequential()
    
    model.add(Conv2D(filters=16, kernel_size=(3, 3), padding='same', activation='relu',
                 input_shape=input_shape))
    
    model.add(Conv2D(filters=32, kernel_size=(5, 5), padding='same', activation='relu'))
    
    model.add(AvgPool2D(pool_size=2, padding='same',strides=2))
    
    model.add(Conv2D(filters=20, kernel_size=(3, 3), padding='same', activation='relu'))

    model.add(AvgPool2D(pool_size=2, padding='same',strides=2))
    
    model.add(Flatten())
    
    model.add(Dense(1406, input_shape=input_shape, activation='relu'))    
    model.add(Dense(351, input_shape=input_shape, activation='relu'))
    model.add(Dense(12, input_shape=input_shape, activation='softmax'))
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy',
                  metrics=['acc'])
    print(model.summary())
    return model


def train_model(model, train_data, test_data, batch_size=None, epochs=20,
               steps_per_epoch=None, validation_steps=None):
    model.fit(train_data, 
              validation_data=test_data,
              batch_size=batch_size, epochs=epochs,
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps,
              verbose=2)
    return model 