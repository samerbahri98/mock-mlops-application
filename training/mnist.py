from tensorflow.keras.datasets import mnist
import tensorflow.keras as keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

(x_train, y_train), (x_valid, y_valid) = mnist.load_data()
x_train = x_train.reshape(60000, 784)
x_valid = x_valid.reshape(10000, 784)
x_train = x_train / 255
x_valid = x_valid / 255

num_categories = 10

y_train = keras.utils.to_categorical(y_train, num_categories)
y_valid = keras.utils.to_categorical(y_valid, num_categories)

model = Sequential()

model.add(Dense(units=512, activation='relu', input_shape=(784, )))

model.add(Dense(units=512, activation='relu'))

model.add(Dense(units=10, activation='softmax'))

model.compile(loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(x_train,
                    y_train,
                    epochs=5,
                    verbose=2,
                    validation_data=(x_valid, y_valid))
