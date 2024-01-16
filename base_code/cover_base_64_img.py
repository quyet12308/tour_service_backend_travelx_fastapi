import base64
import io
import base64
from PIL import Image

import os

# from home_screen_database import save_data_in_table_tourist_destination_information

def get_file_paths(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_paths.append(file_path)
    return file_paths

# cover img to base64
def convert_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

#show img using base64
def show_image_from_base64(base64_string):
    image_data = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(image_data))
    image.show()

def write_to_text_file(data, file_path):
    with open(file_path, 'w') as file:
        file.write(data)

# a = convert_image_to_base64(image_path="img\icon_persion.jpg")
# # print(a)
# write_to_text_file(data=a,file_path="test_data.txt")

# show_image_from_base64(base64_string=a)

# print(get_file_paths(folder_path="img"))