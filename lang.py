
import os

def clone(url):
  cloneCommand = 'git clone ' + url
  os.system(cloneCommand)

