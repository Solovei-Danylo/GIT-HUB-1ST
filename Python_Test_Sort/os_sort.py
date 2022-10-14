import os
import sys


EXTENSIONS = {
    "images": ('.jpeg', '.png', '.jpg', '.svg'),
    "video": ('.avi', '.mp4', '.mov', '.mkv'),
    "documents": ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'),
    "audio": ('.mp3', '.ogg', '.wav', '.amr'),
    "archives": ('.zip', '.gz', '.tar')
}


def clean(folder):
    # проходимось циклом по усім нашим файлам в каталозі
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        # якщо це файл
        if os.path.isfile(file_path):
            # передаємо шлях із файлом до функції, у якій вже будемо перевіряти, якого розширення цей файл
            # та будемо його переміщувати у відповідний каталог
            sort_files(folder, file)

        # якщо це каталог, але не один із archives, video, audio, documents, images
        elif file != EXTENSIONS.keys():
            subfolder = os.path.join(folder, file)
            # Якщо каталог порожній
            if not os.listdir(subfolder):
                # видаляємо його
                os.rmdir(subfolder)
            # і перериваємо роботу функції, так як ми порожній каталог видалили і у ньому вже не потрібно шукати файли
                return
            # якщо каталог не порожній, то функція не перерветься і буде виконуватись далі цей код
            # викликаємо цю ж функцію (рекурсія)
            clean(subfolder)


def sort_files(folder: str, file: str):
    file_name, file_suffix = file.rsplit('.', maxsplit=1)

    for folder_name, extensions in EXTENSIONS.items():
        if file.endswith(extensions):
            new_folder = os.path.join(folder, folder_name)

            os.makedirs(new_folder, exist_ok=True)

            new_file_name = normalize(file_name)

            file_path = os.path.join(folder, new_file_name)

            new_file = os.path.join(new_folder, new_file_name + file_suffix)

            os.replace(file_path, new_file)

            if folder_name == 'archives':
                archive_folder = os.path.join(new_folder, new_file_name)

                archive_unpack(new_file, archive_folder)

            # перериваємо цикл, так як ми вже знайши потрібне розширення та зробили із файлом все потрібне
            break

    else:
        new_file_name = normalize(file_name)

        new_file = os.path.join(folder, new_file_name + file_suffix)

        os.replace(file, new_file)


def normalize(file_name):
    # тут щось робимо із назвою файлу
    
    return file_name


def archive_unpack(file: str, folder: str):
    # створюємо каталог із назвою архіву, але назва повиння бути без розширення
    os.makedirs(folder, exist_ok=True)

    # тут потрібно архів (file) розпакувати у каталог folder


def main():
    if len(sys.argv) < 2:
        print('Enter path to folder which should be cleaned')
        exit()

    root_folder = sys.argv[1]

    if (not os.path.exists(root_folder)) and (not os.path.isdir(root_folder)):
        print('Path incorrect')
        exit()

    #root_folder = "C:\\Users\\38063\OneDrive\\Робочий стіл\\GoIT\\Разное"
    clean(root_folder)


if __name__ == "__main__":
    main()
