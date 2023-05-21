## Обучите свёрточную сеть ResNet в Keras (классификация фруктов по фото)


Архитектура ResNet возникла, чтобы решить проблему затухающего градиента в очень глубоких сетях.

Название архитектуры — это сокращение от Residual Network. На русском языке его дословно переводят как «остаточная сеть», но обычно такие модели называют «резнет». 
Главная особенность ResNet заключается в использовании Shortcut Connections — дополнительные связи внутри сети, которые позволяют избежать проблемы затухающего градиента.

**Добейтесь того, чтобы значение accuracy на тестовой выборке было не меньше 99%.**

Чтобы код выполнялся быстрее, мы загрузили веса модели ResNet50 на сервер. Скачивать веса сервер не будет, если в аргументе weights указать такой путь к файлу:<br/>`/datasets/keras_models/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5`

*Чистый код обучения: [CV_4_resnet.py](data/CV_4_resnet.py)*

---

**Имеем данные:**

![](data/fruits_image_classification_image1.jpg)

**Код:**


```python
from tensorflow.keras.layers import Dense,GlobalAveragePooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
import numpy as np


def load_train(path):
    datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=90,
        width_shift_range=0.15,
        height_shift_range=0.15
    )
    train_datagen_flow = datagen.flow_from_directory(
        path,
        target_size=(150, 150),
        batch_size=16,
        class_mode='sparse',
        seed=12345
    )
    return train_datagen_flow


def create_model(input_shape):
    optimizer = Adam(learning_rate=0.0001)
    
    backbone = ResNet50(input_shape=input_shape,
                    weights='/datasets/keras_models/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5',
                    include_top=False) 
    
    
    model = Sequential()
    
    model.add(backbone)
    model.add(GlobalAveragePooling2D())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(12, activation='softmax'))
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy',
                  metrics=['acc'])
    print(model.summary())
    return model


def train_model(model, train_data, test_data, batch_size=None, epochs=1,
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

**Вывод:** обучили модель с точностью 99.17% в одну эпоху.

**Лог:**

```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
resnet50 (Model)             (None, 5, 5, 2048)        23587712  
_________________________________________________________________
global_average_pooling2d (Gl (None, 2048)              0         
_________________________________________________________________
dense (Dense)                (None, 256)               524544    
_________________________________________________________________
dense_1 (Dense)              (None, 12)                3084      
=================================================================
Total params: 24,115,340
Trainable params: 24,062,220
Non-trainable params: 53,120
_________________________________________________________________


<class 'tensorflow.python.keras.engine.sequential.Sequential'>
Train for 1463 steps, validate for 488 steps
1463/1463 - 272s - loss: 0.1228 - acc: 0.9622 - val_loss: 0.0234 - val_acc: 0.9917
488/488 - 40s - loss: 0.0234 - acc: 0.9917
```
