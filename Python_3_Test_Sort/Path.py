from pathlib import *

PathExample = Path('Timeweb', 'Cloud', 'Pathlib')
PathExample = Path.home() / PathExample
print(PathExample)
AttributeExample = PathExample / 'file.txt'
print(AttributeExample)
