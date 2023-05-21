```python
# код с теста гугл колаба
import timeit
import tensorflow as tf
print(tf.__version__)
```

    2.10.0
    


```python
tf.debugging.set_log_device_placement(False) # тут у них было тру
```


```python
tf.config.experimental.list_physical_devices() # а отсюда воруем айдишник в функцию
```




    [PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU'),
     PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]




```python
def func():
    random_image_gpu = tf.random.normal((100, 100, 100, 3))
    net_gpu = tf.keras.layers.Conv2D(32, 7)(random_image_gpu)
    return tf.math.reduce_sum(net_gpu)
```


```python
def cpu_test():
  with tf.device('/CPU:0'):
    return func()

def gpu_test():
  with tf.device('/GPU:0'):
    return func() 
```


```python
# Run the op several times.
print('Time (s) to convolve 32x7x7x3 filter over random 100x100x100x3 images '
      '(batch x height x width x channel). Sum of ten runs.')
print('CPU (s):')
cpu_time = timeit.timeit('cpu_test()', number=10, setup="from __main__ import cpu_test")
print(cpu_time)
print('GPU (s):')
gpu_time = timeit.timeit('gpu_test()', number=10, setup="from __main__ import gpu_test")
print(gpu_time)
print('GPU speedup over CPU: {}x'.format(int(cpu_time/gpu_time)))
```

    Time (s) to convolve 32x7x7x3 filter over random 100x100x100x3 images (batch x height x width x channel). Sum of ten runs.
    CPU (s):
    0.9308616000000001
    GPU (s):
    0.03719900000000109
    GPU speedup over CPU: 25x
    
