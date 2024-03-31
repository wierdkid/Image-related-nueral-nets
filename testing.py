import tensorflow as tf
import time
import random



(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

data = list(zip(x_test, x_test))

random.shuffle(data)

validation_data = data[:int(len(data) * 0.5)]
test_data = data[int(len(data) * 0.5):]

# Unpack the validation and test data into separate x and y lists
x_val, y_val = zip(*validation_data)
x_test, y_test = zip(*test_data)

histories = []

class CustomCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        try: 
            test_loss, test_accuracy = model.evaluate(x_test, y_test)
            histories[-1].append(test_accuracy)
            if float(test_accuracy) > 0.99:
                print("\nReached 99% test accuracy, stopping training.")
                self.model.stop_training = True
        except Exception as e:
            print(f"An error of type {type(e).__name__} occurred.")

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(8, (3,3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Conv2D(8, (5,5), activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Conv2D(8, (5,5), activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Conv2D(8, (5,5), activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(10, activation='softmax')
])

print(model.summary())

times = []

for i in range(10):
    histories.append([])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    t1 = time.time()
    history = model.fit(x_train, y_train, batch_size = 32, epochs=10, validation_data=(x_val, y_val), callbacks=[CustomCallback()])
    t2 = time.time()
    del model
    times.append(t2-t1)

print(histories)
print(times)