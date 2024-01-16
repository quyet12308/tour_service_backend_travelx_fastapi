import random

def generate_random_6_digit_number():
    # Tạo số ngẫu nhiên có 6 chữ số
    random_number = random.randint(0, 999999)

    # Chuyển số thành chuỗi và thêm số 0 đằng trước nếu cần
    random_number_str = str(random_number).zfill(6)
    
    return random_number_str

# Sử dụng hàm
# random_6_digit_number = generate_random_6_digit_number()
# print("Random 6-digit number:", random_6_digit_number)
