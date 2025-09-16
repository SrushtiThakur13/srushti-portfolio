import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

def predict_image(model_path, img_path):
    model = tf.keras.models.load_model(model_path)

    img = image.load_img(img_path, target_size=(128,128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)[0][0]
    return "Malignant" if pred > 0.5 else "Benign"

if __name__ == "__main__":
    print(predict_image("cancer_cnn.h5", "sample.jpg"))
