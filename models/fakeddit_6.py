from torch import mode
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import preprocessor as p
import pandas as pd
import numpy as np
import argparse
from models.model import TextAttBiRNN

def caller(test):
    max_features = 30000 
    maxlen = 20
    batch_size = 512
    embedding_dims = 50
    SAVED_DIR = "./saved_models/fakeddit/6way/"
    data = "fakeddit"
    model2 = TextAttBiRNN(maxlen, max_features, embedding_dims, class_num = 6, last_activation= 'softmax')
    model2.compile('adam', 'categorical_crossentropy', metrics=['accuracy'])
    model2.load_weights(SAVED_DIR)
    # test = test.dropna()
    print(test)
    x_test = test['Tweet'].to_numpy()
    #y_test = pd.get_dummies(y_test).to_numpy()
    token = pickle.load(open(f'{SAVED_DIR}{data}_tokenizer', 'rb'))
    x_test = pad_sequences(token.texts_to_sequences(x_test), maxlen=maxlen)
    result = model2.predict(x_test)
    result = np.argmax(result, axis = 1)
    test['Category'] = pd.Series(result)
    print(result)
    return test
