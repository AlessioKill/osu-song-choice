import os
import random
import os
beatmaps = input("Put the path of the osu songs directory: ")
if os.path.isdir(beatmaps): 
    file_nomi = os.listdir(beatmaps)
    song = random.choice(file_nomi)
    print("The song you must play is" + song)
else:
    print("The directory does not exist!")
