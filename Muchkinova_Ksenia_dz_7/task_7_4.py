import os


BASE_DIR_7 = os.path.dirname(os.path.abspath(__file__))
some_data = os.path.join(BASE_DIR_7, 'some_data')
groups = [0, 100, 1000, 10000, 1000000]
size_files = dict.fromkeys(groups, 0)
for file in os.listdir(some_data):
    file_path = os.path.join(some_data, file)
    if os.path.isfile(file_path):
        size = os.path.getsize(file_path)
        group = min(filter(lambda x: size < x, groups))
        size_files[group] += 1
print(size_files)
