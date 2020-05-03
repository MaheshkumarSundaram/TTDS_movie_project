from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from pickle import load
import numpy as np
import os

#This model just predict one word only

model_path = os.path.join('checkpoints', 'word_pred_Model2.h5')
model = load_model(model_path)
tokenizer = load(open('tokenizer_Model2','rb'))

seq_len = 2
num_gen_words = 1
 
def gen_text(model, tokenizer, seq_len, seed_text, num_gen_words):
    output_text = []
    input_text = seed_text
    for i in range(num_gen_words):
        encoded_text = tokenizer.texts_to_sequences([input_text])[0]
        pad_encoded = pad_sequences([encoded_text], maxlen=seq_len,truncating='pre')
        pred_word_ind = model.predict_classes(pad_encoded,verbose=0)[0]
        
        pred_word = tokenizer.index_word[pred_word_ind]
        input_text += ' '+pred_word
        output_text.append(pred_word)
    return ' '.join(output_text)

print('\n\n===>Enter --exit to exit from the program')
while True:
    seed_text  = input('Enter string: ')
    if seed_text.lower() == '--exit':
        break
    else:
        out = gen_text(model, tokenizer, seq_len=seq_len, seed_text=seed_text, num_gen_words=num_gen_words)
        print('Output: '+seed_text+' '+out)