#This script does not need to be run!
#it is here for keeping track of project history only!
#pickle database is already built as markov_database.p
#the main section of code will pull phrases from phrases_generated.txt
#running this script will likely result in errors!

#markov database builder using source text from isaac asimov
#Author: Brenly
#requires pickle library
#requires markovify github library by @jsvine

import markovify
import pickle

f = open ("asimov-chemistry.txt")
text_chemistry = f.read()
model_chemistry = markovify.Text(text_chemistry, state_size=2)

f = open ("phys2.txt")
text_physics = f.read()
model_physics = markovify.Text(text_physics, state_size=2)


model_combo = markovify.combine([model_physics, model_chemistry], [1.4, 1])
#combines two models to generate sentences weighted accordingly 1 to 1.4 created in my opinion the best balance of language

#this next line is ultimately a bit useless as the next script will generate a txt file of sentences
#python 3.6 shifted usage of pickle so this will need to be rewritten past 2.7 possibly
pickle.dump(model_combo, open("markov_database.p", "w"))

##### this next code segment does not work.
##### there is poor documentation of converting the markov libraries to JSON format so I opted for pickle and plain text file generation
#json_model_combo = model_combo.to_json()
#with open ('main_database.json', 'w') as outfile:
#	json.dump(json_model_combo, outfile)
#with the json database successfully built it can then be reloaded as needed into other scripts