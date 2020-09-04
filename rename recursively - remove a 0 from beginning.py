# This python script removes a '0' from the beginning of the number file names
# that are smaller than decimal 10, in the current directory and its subdirectories.

# __author__ = Puyu Liu
# __copyright__ = "Copyright (C) 2020 Puyu Liu"
# __version__ = "1.0"
# __date__ = 09-04-2020

import os
import sys

directory = os.path.dirname(os.path.realpath(sys.argv[0])) 	#get the directory to work on through commandline argument
print('The arguments are: ', str(sys.argv))

for subdir, dirs, files in os.walk(directory):
 for fn in files:
  if fn.find('.mp3') > 0 and os.path.splitext(fn)[0][:1] == "0" and float(fn.split(".")[0]) < 10:
   subdirectoryPath = os.path.relpath(subdir, directory) 	#get the path to your subdirectory
   filePath = os.path.join(subdirectoryPath, fn) 			#get the path to your file
   newFilePath = filePath.replace(os.path.splitext(fn)[0], os.path.splitext(fn)[0][1:]) #create the new name
   print("filename: " + os.path.splitext(fn)[0])
   print("newfilename: " + os.path.splitext(fn)[0][1:])
   os.rename(filePath, newFilePath) 				#rename your file
