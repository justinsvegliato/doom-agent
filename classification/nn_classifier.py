#!/usr/bin/env python
import data_handler
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.optimizers import Nadam

CLASS_COUNT = 64
TRAINING_EXAMPlE_COUNT = 9000

def main():
    examples, labels = data_handler.get_dataset('data.csv', CLASS_COUNT)

    training_examples, test_examples = data_handler.split_dataset(examples, TRAINING_EXAMPlE_COUNT)
    training_labels, test_labels = data_handler.split_dataset(labels, TRAINING_EXAMPlE_COUNT)

    model = Sequential([
        Dense(64, input_dim=training_examples.shape[1], init='normal'),
        Activation('relu'),
        Dense(128),
        Activation('relu'),
        Dense(256),
        Activation('relu'),
        Dense(CLASS_COUNT),
        Activation('softmax')
    ])
    nadam = Nadam(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=1e-08, schedule_decay=0.004)
    model.compile(loss='categorical_crossentropy', optimizer=nadam, metrics=['accuracy'])
    model.fit(training_examples, training_labels)

    print '\nAccuracy: %s' % model.evaluate(test_examples, test_labels)[1]

if __name__ == '__main__':
    main()