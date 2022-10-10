# We define a function for generating sentences
def randomSentence(prob_matrix, word_dict):

  # We start with a full stop to start a sentence by the beginning
  curr_wrd = "."    # The current word during the iteration
  reslist = [curr_wrd]  # The list of resulting words

  # We iterate all the length
  for i in range(LENGTH):

    # We get a random new word depending on the probability
    next_list = prob_matrix[word_dict[curr_wrd]]
    curr_wrd = np.random.choice(list(word_dict.keys()), p=next_list)

    #We save the new word
    reslist.append(curr_wrd)

  # We join and clean the resulting sentence
  res = ' '.join(reslist[1:]).replace(' ,',',').replace(' .','.') + " [...]"

  return res


import random as rd
import numpy as np
import csv
import json
import tweepy
from os import environ
import time
import keys

# Global variables setup
k = keys.get_keys()
LENGTH = 20
CONSUMER_KEY = k['CONSUMER_KEY']
CONSUMER_SECRET = k['CONSUMER_SECRET']
ACCESS_KEY = k['ACCESS_KEY']
ACCESS_SECRET = k['ACCESS_SECRET']

# Api setup
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

# We open the probability matrix (csv)
with open(r'C:\Users\ASUS\Desktop\Sanchez\Programas\Sanchtext\prob_matrix.csv', 'r') as fd:
  csv_reader = csv.reader(fd)
  prob_matrix = list(csv_reader)

# We open the word dictionary (json)
with open(r'C:\Users\ASUS\Desktop\Sanchez\Programas\Sanchtext\word_dict.json') as json_file:
    word_dict = json.load(json_file)

message = f'''
"{randomSentence(prob_matrix, word_dict)}"

Mensaje aleatorio generado automáticamente.
Para leer más cosas como esta: [https://elalber2000.github.io/lacaverna/]
'''


# We execute the function
api.update_status(message)