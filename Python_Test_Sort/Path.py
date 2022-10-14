import pathlib


def get_all_files(dir_path_to_search):
    filename_list = []

    file_iterator = dir_path_to_search.iterdir()

    for entry in file_iterator:
        if entry.is_file():
            # print(entry.name)
            filename_list.append(entry.name)

    return filename_list


dir_path_to_search = pathlib.Path("D:\Загрузки с браузера")
print(get_all_files(dir_path_to_search))
