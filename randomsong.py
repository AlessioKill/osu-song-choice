import os
import random
beatmaps = input("\nPut the path of the osu songs directory: ")
if os.path.isdir(beatmaps): 
    file_nomi = os.listdir(beatmaps)
    song = random.choice(file_nomi)
    print("\nThe song you must play is " + song)
else:
    print("\nThe directory does not exist!")
