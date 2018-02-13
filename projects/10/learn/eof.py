fp=open('file_name','r')
lines=fp.readlines()
eof=fp.tell() # here we store the pointer
              # indicating the end of the file in eof
fp.seek(0) # we bring the cursor at the begining of the file
if eof != fp.tell(): # we check if the cursor
     do_something()  # reaches the end of the file
