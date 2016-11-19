import os

# from datetime import datetime
#
# # to print the current path
# print(os.getcwd())
#
# # to navigate into a specif directory
# os.chdir('C:/Users/bidro/Desktop/')
#
# print(os.getcwd())
#
# # list dir
#
# # create dir
#
# os.makedirs('makedir1/makedir2/makedir3')
# os.removedirs('makedir1/makedir2/makedir3')
#
# print(os.listdir())
#
# # os.rename('','')
# print(os.stat('MD_Moshiour_Rahman_CV.docx'))
# print(os.stat('MD_Moshiour_Rahman_CV.docx').st_size)
#
# print(datetime.fromtimestamp(os.stat('MD_Moshiour_Rahman_CV.docx').st_mtime))
#
# for dirpath, dirnames, filenames in os.walk('C:/Users/bidro/Desktop/'):
#     print('Current Path: ', dirpath)
#     print('Directories: ', dirnames)
#     print('Files: ', filenames)
#     print()
# print(os.environ)
# print(os.environ.get('JAVA_HOME'))

file_path = os.path.join(os.environ.get('JAVA_HOME'), 'test.txt')
print(file_path)
print(os.environ)

#it doesn't need to be a real path
os.path.basename('/')
