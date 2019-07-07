from sys import argv
from os.path import exists

script, from_file, to_file = argv

with open(from_file,'r') as in_file, open(to_file,'w') as out_file:

    out_file.write(in_file.read())

#print(f"Copying from {from_file} to {to_file}")

#in_file = open(from_file)
#indata = in_file.read()

#print(f"The input file is {len(indata)} bytes long")

#print(f"Does the output file exists? {exists(to_file)}")
#exists(path)表示的是判断该文件是否存在
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

#out_file = open(to_file, 'w')
#out_file.write(indata)

#print("Alright, all done.")

#out_file.close()
#in_file.close()
