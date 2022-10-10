import csv
import json


# We read the corpus
with open(r'C:\Users\ASUS\Desktop\Sanchez\Programas\Sanchtext\corpus.txt','r',encoding='utf8') as fd:
  str = fd.read()



# We make a clean list with all the tokens
wordlist = str.replace("."," . ").replace(","," , ").replace('\"',"").replace("\'","").split()
wordlist = list(map(lambda x : x.strip(), wordlist))
wordlist = list(filter(lambda x : x!="", wordlist))
wordlist[0] = wordlist[0].lower()



# We calculate all the state transitions
state_transitions = {}
word_dict = {}

wd_count = 0

for count,elem in enumerate(wordlist):

  if(count+1!=len(wordlist)):
    next_elem = wordlist[count+1]

    if state_transitions.get(elem+' '+next_elem):
      state_transitions[elem+' '+next_elem] += 1
    else:
      state_transitions[elem+' '+next_elem] = 1

  if word_dict.get(elem)==None:
    word_dict[elem] = wd_count
    wd_count += 1



# We make a matrix with all all state-change occurences
occ_matrix = [[0 for x in range(len(word_dict))] for y in range(len(word_dict))]

for i in state_transitions:
  prev = word_dict[i.split(" ")[0]]
  next = word_dict[i.split(" ")[1]]
  occ_matrix[prev][next] = state_transitions[i]



# We make a matrix with all state-change probabilities
prob_matrix = [[]]

for i in occ_matrix:
  row_total = sum(i)

  if row_total == 0:
    prob_matrix.append([1] + [0]*(len(i)-1))
  else:
    prob_matrix.append(list(map(lambda x : x/row_total, i)))

prob_matrix = prob_matrix[1:]



# We save the probability matrix and the word dictionary
with open("prob_matrix.csv", "w", newline="") as fd:
    writer = csv.writer(fd)
    writer.writerows(prob_matrix)

with open('word_dict.json', 'w') as f:
    json.dump(word_dict, f)