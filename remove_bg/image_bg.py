# Remove Background using Python 
# remember to pip install rembg
# see https://github.com/danielgatis/rembg
# this seems to work best in a venv
from rembg import remove

input_path = 'm323.jpg'
output_path = 'output.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)