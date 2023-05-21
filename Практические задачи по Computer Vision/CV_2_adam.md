## Постройте и обучите свёрточную нейронную сеть используя LeNet и алгоритм Adam

**Используйте набор данных с одеждой (fashion_mnist).**

Градиентный спуск (SGD) — это не самый оптимальный алгоритм обучения нейронной сети. Если величина шага слишком маленькая, сеть будет обучаться долго, а если большая — может пропустить минимум. 

**Чтобы подбор шага был автоматическим, применим алгоритм Adam** (от англ. adaptive moment estimation, «адаптивность на основе оценки моментов»).<br/>Он подберет различные параметры для разных нейронов, что также ускорит обучение модели.

В LeNet заменим функцию активации с гиперболического тангенса на ReLU, а алгоритм обучения — с SGD на Adam.

*Чистый код обучения: [CV_2_adam.py](data/CV_2_adam.py)*


```python
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.layers import Dense,Conv2D,AvgPool2D,Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
import numpy as np


def load_train(path):
    features_train = np.load(path + 'train_features.npy')
    target_train = np.load(path + 'train_target.npy')
    features_train = features_train.reshape(-1, 28, 28, 1) / 255.0
    return features_train, target_train


def create_model(input_shape):
    optimizer = Adam()
    model = Sequential()
    
    model.add(Conv2D(filters=6, kernel_size=(5, 5), padding='same', activation='relu',
                 input_shape=(28, 28, 1)))

    model.add(AvgPool2D(pool_size=2, padding='same',strides=2))

    model.add(Conv2D(filters=16, kernel_size=(5, 5), activation='relu',
                     input_shape=(28, 28, 1),strides=1))

    model.add(AvgPool2D(pool_size=2, padding='same',strides=2))

    model.add(Flatten())
    
    model.add(Dense(256, input_shape=input_shape, activation='relu'))
    model.add(Dense(10, input_shape=input_shape, activation='softmax'))
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy',
                  metrics=['acc'])

    return model


def train_model(model, train_data, test_data, batch_size=32, epochs=5,
               steps_per_epoch=None, validation_steps=None):

    features_train, target_train = train_data
    features_test, target_test = test_data
    model.fit(features_train, target_train, 
              validation_data=(features_test, target_test),
              batch_size=batch_size, epochs=epochs,
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps,
              verbose=2, shuffle=True)

    return model 
```

## Результаты обучения

**Вывод:** обучили модель с точностью 89.6%.

**Лог:**

```
<class 'tensorflow.python.keras.engine.sequential.Sequential'>
Train on 60000 samples, validate on 10000 samples
Epoch 1/5
60000/60000 - 8s - loss: 0.5391 - acc: 0.8032 - val_loss: 0.4226 - val_acc: 0.8440
Epoch 2/5
60000/60000 - 6s - loss: 0.3702 - acc: 0.8656 - val_loss: 0.3667 - val_acc: 0.8696
Epoch 3/5
60000/60000 - 6s - loss: 0.3197 - acc: 0.8831 - val_loss: 0.3440 - val_acc: 0.8746
Epoch 4/5
60000/60000 - 6s - loss: 0.2864 - acc: 0.8948 - val_loss: 0.3073 - val_acc: 0.8917
Epoch 5/5
60000/60000 - 6s - loss: 0.2633 - acc: 0.9039 - val_loss: 0.2898 - val_acc: 0.8960
10000/10000 - 1s - loss: 0.2898 - acc: 0.8960
```
