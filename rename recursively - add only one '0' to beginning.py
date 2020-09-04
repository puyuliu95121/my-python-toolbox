import os
import sys
import errno

dir = os.path.dirname(os.path.realpath(sys.argv[0])) 	#get the directory to work on
print('sys.argv: ')
print(sys.argv)

for subdir, dirs, files in os.walk(dir):
 #print("root: " + root)
 print("subdir: " + subdir)
 print("dirs: ")
 print('[%s]' % ', '.join(map(str, dirs)))
 
 for fn in files:
  print('fn.split("."): ')
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