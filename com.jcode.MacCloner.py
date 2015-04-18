# import the os library (below)
import os
# Get User Input (below)
clonePrompt = raw_input("Git Repo URL: ")
# Turn User Input into string (below)
clonePromptAnswers = str(clonePrompt)
# git clone variable (below) 
gitCloneRepo = 'git clone ' + clonePrompt
# execute cloning
os.system(gitCloneRepo)

