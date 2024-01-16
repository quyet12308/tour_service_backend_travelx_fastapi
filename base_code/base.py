import random
import os
import re

def random_number(start, end):
    return random.randint(start, end)

def random_decimal(start,end):
    return round(random.uniform(start, end),1)

def random_number_price(start,end):
    a = random_number(start, end)
    b = a * 5
    return b

def random_number_rivew(start,end):
    a = random_number(start, end)
    b = a * 5
    return b

def random_3_numbers(start, end):
    # Tạo một danh sách các số từ start đến end
    number_list = list(range(start, end + 1))
    
    # Kiểm tra nếu danh sách không đủ 3 số thì trả về danh sách đó
    if len(number_list) < 3:
        return number_list

    # Lấy ngẫu nhiên 3 số không trùng nhau từ danh sách
    random_numbers = random.sample(number_list, 3)

    return random_numbers

def cover_kelvin_to_c(kelvin):
    c = kelvin - 273.15
    return c

def convert_time_to_period(time_str):
    time_parts = time_str.split(" ")
    date_part = time_parts[0]
    time_part = time_parts[1]

    hour = int(time_part[:2])

    if hour >= 6 and hour < 12:
        period = "sáng"
    elif hour >= 12 and hour < 18:
        period = "chiều"
    elif hour >= 18 and hour < 24:
        period = "tối"
    else:
        period = "đêm"

    return f"{date_part} {period}"


def list_files_in_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

# a = list_files_in_folder(folder_path="img\img_hotels")
# print(a)



def read_and_cover_data_in_txt_file(file_text_path):
    # Đường dẫn đến file văn bản
    # file_path = "du_lieu.txt"

    # Đọc nội dung từ file
    with open(file_text_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Tách thành từng mục
    sections = re.split(r"\d+\.", text)[1:]

    for section in sections:
        # Tách tên và mô tả riêng
        match = re.search(r"(.+?)\((.+?)\)", section)
        if match:
            name = match.group(1).strip()
            description = match.group(2).strip()
            print("Tên:", name)
            print("Mô tả:", description)
            print()

# read_and_cover_data_in_txt_file(file_text_path="test3.txt")

def doc_du_lieu(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            du_lieu = file.read()
        return du_lieu
    except IOError:
        print("Không thể đọc tệp: " + file_path)
        return None
    
def tach_doan_text(text):
    doan_text = text.split('\n\n')
    ket_qua = []
    for doan in doan_text:
        lines = doan.strip().split('\n')
        ten_khach_san = lines[0]
        mo_ta = ' '.join(lines[1:])
        ket_qua.append((ten_khach_san, mo_ta))
    return ket_qua


# c = random_number_rivew(start=2,end=20)
# print(c)