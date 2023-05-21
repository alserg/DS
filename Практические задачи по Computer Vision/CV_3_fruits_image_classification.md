## Обучите свёрточную сеть для классификации фруктов по изображению

**Добейтесь того, чтобы значение accuracy на тестовой выборке было не меньше 90%.**

*Чистый код обучения: [CV_3_fruits_image_classification.py](data/CV_3_fruits_image_classification.py)*

---

**Имеем данные:**

![](data/fruits_image_classification_image1.jpg)

**Код:**


```python
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
```

## Результаты обучения

**Вывод:** обучили модель с точностью 99.21%.

**Лог:**

```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 150, 150, 16)      448       
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 150, 150, 32)      12832     
_________________________________________________________________
average_pooling2d (AveragePo (None, 75, 75, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 75, 75, 20)        5780      
_________________________________________________________________
average_pooling2d_1 (Average (None, 38, 38, 20)        0         
_________________________________________________________________
flatten (Flatten)            (None, 28880)             0         
_________________________________________________________________
dense (Dense)                (None, 1406)              40606686  
_________________________________________________________________
dense_1 (Dense)              (None, 351)               493857    
_________________________________________________________________
dense_2 (Dense)              (None, 12)                4224      
=================================================================
Total params: 41,123,827
Trainable params: 41,123,827
Non-trainable params: 0
_________________________________________________________________


<class 'tensorflow.python.keras.engine.sequential.Sequential'>
Train for 732 steps, validate for 488 steps
Epoch 1/20
732/732 - 268s - loss: 0.8446 - acc: 0.7034 - val_loss: 0.4207 - val_acc: 0.8387
Epoch 2/20
732/732 - 270s - loss: 0.2761 - acc: 0.9048 - val_loss: 0.2294 - val_acc: 0.9184
Epoch 3/20
732/732 - 273s - loss: 0.2029 - acc: 0.9316 - val_loss: 0.1418 - val_acc: 0.9503
Epoch 4/20
732/732 - 277s - loss: 0.1590 - acc: 0.9443 - val_loss: 0.2561 - val_acc: 0.9027
Epoch 5/20
732/732 - 281s - loss: 0.1302 - acc: 0.9551 - val_loss: 0.0953 - val_acc: 0.9649
Epoch 6/20
732/732 - 274s - loss: 0.1165 - acc: 0.9602 - val_loss: 0.1128 - val_acc: 0.9600
Epoch 7/20
732/732 - 277s - loss: 0.0973 - acc: 0.9658 - val_loss: 0.0772 - val_acc: 0.9735
Epoch 8/20
732/732 - 282s - loss: 0.0872 - acc: 0.9705 - val_loss: 0.1116 - val_acc: 0.9601
Epoch 9/20
732/732 - 265s - loss: 0.0800 - acc: 0.9719 - val_loss: 0.0844 - val_acc: 0.9690
Epoch 10/20
732/732 - 262s - loss: 0.0697 - acc: 0.9756 - val_loss: 0.0785 - val_acc: 0.9710
Epoch 11/20
732/732 - 275s - loss: 0.0624 - acc: 0.9782 - val_loss: 0.0517 - val_acc: 0.9837
Epoch 12/20
732/732 - 265s - loss: 0.0541 - acc: 0.9817 - val_loss: 0.0467 - val_acc: 0.9842
Epoch 13/20
732/732 - 273s - loss: 0.0524 - acc: 0.9821 - val_loss: 0.0703 - val_acc: 0.9764
Epoch 14/20
732/732 - 254s - loss: 0.0514 - acc: 0.9824 - val_loss: 0.0492 - val_acc: 0.9815
Epoch 15/20
732/732 - 255s - loss: 0.0416 - acc: 0.9853 - val_loss: 0.0411 - val_acc: 0.9868
Epoch 16/20
732/732 - 260s - loss: 0.0380 - acc: 0.9871 - val_loss: 0.0445 - val_acc: 0.9840
Epoch 17/20
732/732 - 266s - loss: 0.0413 - acc: 0.9870 - val_loss: 0.0352 - val_acc: 0.9882
Epoch 18/20
732/732 - 266s - loss: 0.0353 - acc: 0.9881 - val_loss: 0.0504 - val_acc: 0.9830
Epoch 19/20
732/732 - 266s - loss: 0.0309 - acc: 0.9899 - val_loss: 0.0290 - val_acc: 0.9899
Epoch 20/20
732/732 - 267s - loss: 0.0372 - acc: 0.9875 - val_loss: 0.0223 - val_acc: 0.9921
488/488 - 41s - loss: 0.0223 - acc: 0.9921
```
