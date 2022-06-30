from tensorflow.keras.preprocessing.image import ImageDataGenerator


from tensorflow.keras.optimizers import RMSprop
import tensorflow as tf

def main():

    train_datagen = ImageDataGenerator(rescale=1/255)
    training_dir = "Images/horse-or-human/training/"
    train_generator = train_datagen.flow_from_directory(
        training_dir,
        target_size=(300,300),
        class_mode='binary'
    )


    validation_datagen = ImageDataGenerator(rescale=1 / 255)
    validation_dir = "Images/horse-or-human/validation/"
    validation_generator = validation_datagen.flow_from_directory(
        validation_dir,
        target_size=(300, 300),
        class_mode='binary'
    )
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(300, 300, 3)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(loss='binary_crossentropy',
                  optimizer=RMSprop(lr=0.001),
                  metrics=['acc'])

    history = model.fit_generator(
        train_generator,
        steps_per_epoch=8,
        epochs=15,
        validation_data=validation_generator)


if __name__ == "__main__":
    main()