## Попробуйте решить задачу многоклассовой классификации на изображениях.

В вашем распоряжении такой датасет. Для агрегатора магазинов одежды нужно сделать классификатор на 10 классов. Каждый класс будет отвечать за определённую категорию товаров и отражён на сайте агрегатора:

Label	Description

0	T-shirt/top<br/>
1	Trouser<br/>
2	Pullover<br/>
3	Dress<br/>
4	Coat<br/>
5	Sandal<br/>
6	Shirt<br/>
7	Sneaker<br/>
8	Bag<br/>
9	Ankle boot

Вы будете работать с изображениями, потому что описания товаров могут содержать некорректную информацию, их может быть слишком много и причём на разных языках. 
На входе модель будет получать чёрно-белую фотографию товара.

*Чистый код обучения: [CV_1_manylayers.py](data/CV_1_manylayers.py)*


```python
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
import numpy as np


def load_train(path):
    features_train = np.load(path + 'train_features.npy')
    target_train = np.load(path + 'train_target.npy')
    features_train = features_train.reshape(features_train.shape[0], 28 * 28) / 255.
    return features_train, target_train


def create_model(input_shape):
    model = Sequential()
    model.add(Dense(1536, input_shape=input_shape, activation='relu'))
    model.add(Dense(784, input_shape=input_shape, activation='relu'))
    model.add(Dense(10, input_shape=input_shape, activation='softmax'))
    model.compile(optimizer='sgd', loss='sparse_categorical_crossentropy',
                  metrics=['acc'])

    return model


def train_model(model, train_data, test_data, batch_size=16, epochs=13,
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

**Вывод:** обучили модель с точностью 89%.

**Лог:**

```
<class 'tensorflow.python.keras.engine.sequential.Sequential'>
Train on 60000 samples, validate on 10000 samples
Epoch 1/13
60000/60000 - 13s - loss: 0.5727 - acc: 0.8070 - val_loss: 0.4577 - val_acc: 0.8411
Epoch 2/13
60000/60000 - 10s - loss: 0.4177 - acc: 0.8543 - val_loss: 0.4162 - val_acc: 0.8523
Epoch 3/13
60000/60000 - 10s - loss: 0.3761 - acc: 0.8675 - val_loss: 0.3897 - val_acc: 0.8625
Epoch 4/13
60000/60000 - 9s - loss: 0.3488 - acc: 0.8758 - val_loss: 0.3853 - val_acc: 0.8605
Epoch 5/13
60000/60000 - 11s - loss: 0.3276 - acc: 0.8834 - val_loss: 0.3866 - val_acc: 0.8601
Epoch 6/13
60000/60000 - 12s - loss: 0.3110 - acc: 0.8884 - val_loss: 0.3445 - val_acc: 0.8771
Epoch 7/13
60000/60000 - 10s - loss: 0.2962 - acc: 0.8923 - val_loss: 0.3797 - val_acc: 0.8599
Epoch 8/13
60000/60000 - 11s - loss: 0.2837 - acc: 0.8968 - val_loss: 0.3336 - val_acc: 0.8815
Epoch 9/13
60000/60000 - 11s - loss: 0.2729 - acc: 0.9006 - val_loss: 0.3384 - val_acc: 0.8761
Epoch 10/13
60000/60000 - 12s - loss: 0.2620 - acc: 0.9045 - val_loss: 0.3349 - val_acc: 0.8802
Epoch 11/13
60000/60000 - 10s - loss: 0.2525 - acc: 0.9083 - val_loss: 0.3286 - val_acc: 0.8815
Epoch 12/13
60000/60000 - 9s - loss: 0.2443 - acc: 0.9117 - val_loss: 0.3264 - val_acc: 0.8839
Epoch 13/13
60000/60000 - 10s - loss: 0.2366 - acc: 0.9136 - val_loss: 0.3163 - val_acc: 0.8900
10000/10000 - 1s - loss: 0.3163 - acc: 0.8900
```
