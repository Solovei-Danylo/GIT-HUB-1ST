# Выведите список файлов в указанной директ
from pathlib import Path


path = Path(r"C:\Users\DS\Documents\GitHub\GIT-HUB-1ST\Python_3_Test_Sort")

for elem in path.iterdir():
    print(elem)
