import os
from datetime import datetime

# print(dir(os))

# print(os.getcwd())
# os.chdir('/Users/Alex Koshy/works/python')

# print(os.listdir())

# os.mkdir('OS_DEMO')
# os.makedirs('OS_DEMO/SUB')

# os.rmdir('OS_DEMO')
# os.removedirs('OS_DEMO/SUB')

# os.rename('OS_DEMO','OS_DEMO2')

# mod_time = os.stat('integer.py').st_mtime
# print(datetime.fromtimestamp(mod_time))

# for dirpath, dirname, filenames in os.walk('/Users/Alex Koshy/Desktop'):
# # for dirpath, dirname, filenames in os.walk(os.getcwd()):
#     print('Current path: ',dirpath)
#     print('Directories:', dirname)
#     print('Files: ',filenames)
#     print()

# print(os.environ.get('USERPROFILE'))

# file_path = os.path.join(os.environ.get('USERPROFILE'),'test.txt')
# print(file_path)

# print(os.path.basename('/tmp/text.txt'))

# print(os.path.dirname('/tmp/text.txt'))

# print(os.path.split('/tmp/text.txt'))

# print(os.path.exists('C:/Users/Alex Koshy/works/python/dictionary.py'))

# print(os.path.isdir('C:/Users/Alex Koshy/works/python/'))

# print(os.path.isfile('dictionary.py'))

# print(os.path.isfile('C:/Users/Alex Koshy/works/python/dictionary.py'))
# C:\Users\Alex Koshy\works\python

print(os.path.splitext("/tmp/text.txt"))

print(dir(os))
