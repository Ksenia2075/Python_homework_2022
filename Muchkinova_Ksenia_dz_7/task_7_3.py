import os
import shutil


BASE_DIR_7 = os.path.dirname(os.path.abspath(__file__))
my_project = os.path.join(BASE_DIR_7, 'my_project')
templates = os.path.join(my_project, 'templates')
if not os.path.exists(templates):
    os.mkdir(templates)

files = [os.path.relpath(os.path.join(root, file), my_project)
         for root, dirs, files in os.walk(my_project) for file in files if file.endswith(".html")]
for rel_path in files:
    path, file = os.path.split(rel_path)
    shutil.copyfile(os.path.join(my_project,rel_path), os.path.join(templates, file))
