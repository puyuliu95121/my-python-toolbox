# When you donwload lots of mp3 files that are named 1.mp3, 2.mp3 ... 9.mp3, 10.mp3
# the music players would sort the files into an order like: 1.mp3, 10.mp3, 11.mp3 ...
# 19.mp3, 2.mp3, 20.mp3, 21.mp3, ...

# So, a single '0' should be added before the single digit number file names, which is
# what this python script is for.

# __author__ = Puyu Liu
# __copyright__ = "Copyright (C) 2020 Puyu Liu"
# __version__ = "1.0"
# __date__ = 09-04-2020

import os
import sys
import errno

dir = os.path.dirname(os.path.realpath(sys.argv[0])) 	#get the directory to work on
print("\n" + 'sys.argv: ')
print(sys.argv)

for subdir, dirs, files in os.walk(dir):
 #print("root: " + root)
 print("\n" + "subdir: " + subdir)
 print("dirs: ")
 print('[%s]' % ', '.join(map(str, dirs)))
 
 for fn in files:
  print("\n" + 'fn.split("."): ')
  print(fn.split("."))
  if fn.find('.mp3') > 0 and os.path.splitext(fn)[0][:1] != "0" and float(fn.split(".")[0]) < 10:
   print("fn[0]: " + fn[0])
   print("fn[1]: " + fn[1])
   subdirPath = os.path.relpath(subdir, dir) 	        #get the path to your subdir
   print("dir: " + dir)
   print("subdirPath: " + subdirPath)
   fPath = os.path.join(subdirPath, fn) 				#get the path to your file
   print("oldfn:" + os.path.splitext(fn)[0])
   print("newfn: " + "0" + os.path.splitext(fn)[0])
   newfPath = fPath.replace(os.path.splitext(fn)[0], "0" + os.path.splitext(fn)[0] ) #create the new name
   print("newfPath: " + newfPath + "\n")
   try:
    os.rename(fPath, newfPath) 							#rename your file
   except FileNotFoundError:
    print('file not found.')
    continue 