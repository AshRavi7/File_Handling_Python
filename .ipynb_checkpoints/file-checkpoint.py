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

# def create():
#     open('files/test.md','x')
#     return 

# def add_content(string='Hello, Good Morning!'):
#     x=open('files/test.md','w')
#     x.write(string)
#     x.close() # after you write , ensure to close the file. 
    
# def append_content(string='\nWe are learning git commands and file handling'):
#     x=open('files/test.md','a')
#     x.write(string)
#     x.close()

# def read_content():
#     x=open('files/test.md','r')
#     print(x.read())


# def using_print():
#     x=open('files/test.md','a')
#     print('New line',file=x)
#     print('This is another line',file=x)
#     print('I am done',file=x)
#     x.close()
#     return

# def pdf_func():
#     x=open('files/test.pdf','a')
#     x.write('This is a new pdf')
#     x.close()
#     return

# def read_pdf():
#     x=open('files/test.pdf','r')
#     print(x.read())
#     return 

# def docs():
#     from docx import Document
#     document=Document()
#     document.add_heading('Good morning',level=1)
#     document.add_paragraph('We are learning python ; great tool to talk to the computer.Best used for data analytics and web development')
#     document.add_heading('Foundation is the stepping stone to success', level=1)
#     document.add_paragraph('We will overcome the difficult time to become who we are', style='Intense Quote')
#     document.add_page_break()
#     document.save('files/test.docx')
#     return 

   


if __name__=='__main__':
#     create()
#     add_content()
#     append_content()
    # read_content()
    # print('This is file handling examples')
    # print('DONE')
    # using_print()
    # pdf_func()
    # read_pdf()
    docs()
    print('Done writing')
