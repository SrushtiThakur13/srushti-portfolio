import tensorflow as tf
from tensorflow.keras import layers, models
from data_loader import load_data

DATA_DIR = "data/breast_cancer_images"  # replace with your dataset path
EPOCHS = 10
BATCH_SIZE = 32

# Load data
train_gen, val_gen = load_data(DATA_DIR, batch_size=BATCH_SIZE)

# Define CNN
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation="relu", input_shape=(128,128,3)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation="relu"),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(128, (3,3), activation="relu"),
    layers.MaxPooling2D(2,2),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(1, activation="sigmoid")
])

# Compile
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
              loss="binary_crossentropy",
              metrics=["accuracy"])

# Learning Rate Scheduler
def scheduler(epoch, lr):
    if epoch % 3 == 0 and epoch:
        return lr * 0.5
    return lr

callback = tf.keras.callbacks.LearningRateScheduler(scheduler)

# Train
history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=EPOCHS,
    callbacks=[callback]
)

# Save model
model.save("cancer_cnn.h5")
