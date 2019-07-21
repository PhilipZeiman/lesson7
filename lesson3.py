# my_file = open ("C:\\Mail\\philip.txt", "r+", encoding="utf-8")
# content = my_file.read()
# print(content)
# my_file.write("privet")
# print(content)
# my_file.close()

# error because file is missing:
# my_file = open ("C:\\Mail\\hilip.txt", "r+", encoding="utf-8")
# content = my_file.read()

# try:
#     my_file = open ("C:\\Mail\\hilip.txt", "r+", encoding="utf-8")
#     content = my_file.read()
# except IOError as x:
#     # print("error")
#     print(x)
# print("oved")

# try:
#     my_file = open ("C:\\Mail\\hilip.txt", "r+", encoding="utf-8")
#     content = my_file.read()
# except IOError:
#     print("fatal error")
# finally:
#     print("run anyway")

# try:
#     my_file = open ("C:\\Mail\\hilip.txt", "r+", encoding="utf-8")
# finally:
#     print("finally-run anyway")

#run debugger
# x = 4
# y = 5
# z = 6
# x = 7
# print (x)

from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Mail\chromedriver.exe")