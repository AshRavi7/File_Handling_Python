# File handling

# 1. In python, file handling can be acheived with the help of
# the open () . 
# The open () works well to open any kind of file format. 
# It accepts 2 arguments, one -> file name with extension 
# two -> the mode in which you want to interact with the file. 

# 4 types of modes are available.
# 'r' which is used for reading contents from a file, throws error if the file does not exist. 
# 'w' which is used for writing to the file, it will create the file if it does not exist.
# 'a' which is used for appending to the file, it will create the file if it does not exist. 
# 'x' which is create to just create the file if it does not exist. 

def create():
    open('files/test.md','x')
    return 

def add_content(string='Hello, Good Morning!'):
    x=open('files/test.md','w')
    x.write(string)
    x.close() # after you write , ensure to close the file. 
    
def append_content(string='\nWe are learning git commands and file handling'):
    x=open('files/test.md','a')
    x.write(string)
    x.close()

def read_content():
    x=open('files/test.md','r')
    print(x.read())

if __name__=='__main__':
#     create()
#     add_content()
#     append_content()
    read_content()
