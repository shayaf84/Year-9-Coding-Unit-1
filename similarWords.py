#Shaya Farahmand
#November 2,2020
#Asks the user to enter two sentences. Program will return words in both sentences, and words in one sentence

#Takes two sentences as user input, and stores them in the first_phrase and second_phrase variables
first_phrase = input("Enter a sentence: ")
second_phrase = input("Enter a sentence: ")

#Converts the sentences into sets, after parsing the string. 
#Stors into the first_set and second_set variable respectively
first_set = set(first_phrase.split())
second_set = set(second_phrase.split())

#Calculate intersection and symmetric difference of both sets. 
#Intersection variable is for intersection, and not_in_both is for symmetric difference (Concise variable name)
#Sorts each list (capitalization before anything)
intersection = sorted(list(first_set&second_set))
not_in_both = sorted(list(first_set^second_set))

#Prints both intersection and symmetric difference
print("Words in both sentences are: ", intersection)
print("Words not in both sentences are: ", not_in_both)
