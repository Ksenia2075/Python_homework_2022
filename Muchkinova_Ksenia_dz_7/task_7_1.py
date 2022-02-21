import os


structure_of_folders = {'my_project':
                            [{'settings':[],
                              'mainapp':[],
                              'adminapp':[],
                              'authapp':[]}]}


def project_starter(meth, struct):
    for other_fold, project_fold in struct.items():
        dir_path = os.path.join(meth, other_fold)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        if len(project_fold) > 0:
            for fold in project_fold:
                project_starter(dir_path, fold)


if __name__ == '__main__':

    project_starter(os.getcwd(), structure_of_folders)
