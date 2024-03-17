import numpy as np
import tensorflow as tf
import pygame

class MLModel:
    def __init__(self):
        self.model = tf.keras.models.load_model('shape_classifier_model.h5')
        self.CLASSES = ['Circle', 'Triangle', 'Rectangle']

    def preprocess_shape(self, surface):
        resized_surface = pygame.transform.scale(surface, (28, 28))
        image = pygame.surfarray.array2d(resized_surface)
        image = np.invert(image)
        image = image.reshape(1, 28, 28, 1)
        return image.astype('float32') / 255.0

    def classify_shape(self, surface):
        preprocessed_image = self.preprocess_shape(surface)
        prediction = self.model.predict(preprocessed_image)
        predicted_class_index = np.argmax(prediction)
        predicted_class = self.CLASSES[predicted_class_index]
        return predicted_class
