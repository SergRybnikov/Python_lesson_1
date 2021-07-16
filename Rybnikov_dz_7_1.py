import os

dir_path = os.path.join('settings', 'mainapp', 'adminapp', 'authapp')
print(os.getcwd())
if not os.path.isdir('my_project'):
    os.mkdir('my_project')
os.chdir('my_project')
print(os.getcwd())
if not os.path.isdir(dir_path):
    os.makedirs(dir_path)
print(os.listdir())
