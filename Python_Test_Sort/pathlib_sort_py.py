import os
from pathlib import Path
import sys


EXTENSIONS = {
    "images": ('.jpeg', '.png', '.jpg', '.svg'),
    "video": ('.avi', '.mp4', '.mov', '.mkv'),
    "documents": ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'),
    "audio": ('.mp3', '.ogg', '.wav', '.amr'),
    "archives": ('.zip', '.gz', '.tar')
}


def clean(folder: Path):
    # проходимось циклом по усім нашим файлам в каталозі
    for file in folder.iterdir():
        # якщо це файл
        if file.is_file():
            # передаємо шлях із файлом до функції, у якій вже будемо перевіряти, якого розширення цей файл
            # та будемо його переміщувати у відповідний каталог
            sort_files(file, folder)

        # якщо це каталог, але не один із archives, video, audio, documents, images
        elif file.name != EXTENSIONS.keys():
            subfolder = file
            # Якщо каталог порожній
            if not os.listdir(subfolder):
                # видаляємо його
                subfolder.rmdir()
            # і перериваємо роботу функції, так як ми порожній каталог видалили і у ньому вже не потрібно шукати файли
                return
            # якщо каталог не порожній, то функція не перерветься і буде виконуватись далі цей код
            # викликаємо цю ж функцію (рекурсія)
            clean(subfolder)


def sort_files(file: Path, folder: Path):
    for folder_name, extensions in EXTENSIONS.items():
        if file.suffix in extensions:
            new_folder = folder.joinpath(folder_name)

            new_folder.mkdir(exist_ok=True)

            new_file_name = normalize(file.name.removesuffix(file.suffix))

            new_file = file.rename(new_folder.joinpath(new_file_name + file.suffix))

            if folder_name == 'archives':
                archive_unpack(new_folder, new_file)

            # перериваємо цикл, так як ми вже знайши потрібне розширення та зробили із файлом все потрібне
            break

    # якщо цикл не був перерваний примусово, то спрацює ця умова
    else:
        new_file_name = normalize(file.name.removesuffix(file.suffix))

        file.rename(folder.joinpath(new_file_name + file.suffix))


def normalize(file_name):
    # тут щось робимо із назвою файлу
    
    return file_name


def archive_unpack(folder: Path, file: Path):
    # створюємо каталог із назвою архіву, але назва повиння бути без розширення
    archive_folder = folder.joinpath(file.name.removesuffix(file.suffix))

    archive_folder.mkdir(exist_ok=True)

    # тут потрібно архів (file) розпакувати у каталог archive_folder

    
def main():
    if len(sys.argv) < 2:
        print('Enter path to folder which should be cleaned')
        exit()

    root_folder = Path(sys.argv[1])

    if (not root_folder.exists()) and (not root_folder.is_dir()):
        print('Path incorrect')
        exit()

    #root_folder = Path("C:\\Users\\38063\OneDrive\\Робочий стіл\\GoIT\\Разное")

    clean(root_folder)


if __name__ == "__main__":
    main()
