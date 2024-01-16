import sqlite3
import datetime

from base_code.gettime import gettime2

list_element = ['id', 'username', 'fullname', 'email', 'timeCheckin', 'days', 'booking_tour_name', 'booking_tour_id', 'number_adults', 'number_children', 'flight_infor', 'hotel_infor', 'support_persion', 'createdTime']

def create_database_for_booking_tour_basic(tablename):
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/booking_tour.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE {tablename}
                  (id INTEGER PRIMARY KEY,
                   username TEXT,
                   fullname TEXT,
                   email TEXT,
                   timeCheckin TEXT,
                   days TEXT,
                   booking_tour_name TEXT,
                   booking_tour_id TEXT,
                   number_adults TEXT,
                   number_children TEXT,
                   flight_infor TEXT,
                   hotel_infor TEXT, 
                   support_persion TEXT,
                   createdTime TEXT)''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

def create_database_for_booking_tour_basic1(tablename):
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/booking_tour.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE {tablename}
                  (id INTEGER PRIMARY KEY,
                   fullname TEXT,
                   email TEXT,
                   timeCheckin TEXT,
                   days TEXT,
                   booking_tour_name TEXT,
                   price TEXT,
                   number_adults TEXT,
                   number_children TEXT,
                   hotel_infor TEXT,
                   createdTime TEXT)''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# create_database_for_booking_tour_basic(tablename="booking_tour_basic")
# create_database_for_booking_tour_basic1(tablename="booking_tour_basic1")


# lưu dữ liệu 
def save_data_for_booking_tour_basic_in_table( fullname, email, timeCheckin, days, booking_tour_name, price, number_adults, number_children, hotel_infor, createdTime,admin_check_payment):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/booking_tour.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng diseases
    
    cursor.execute(f"INSERT INTO booking_tour_basic1 (fullname, email, timeCheckin, days, booking_tour_name, price, number_adults, number_children, hotel_infor, createdTime,admin_check_payment) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
               (fullname, email, timeCheckin, days, booking_tour_name, price, number_adults, number_children, hotel_infor, createdTime,admin_check_payment))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

def update_data_booking_tour_by_id(id, column, value):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/booking_tour.db')

    cursor = conn.cursor()
    
    # Xây dựng truy vấn SQL để cập nhật dòng dựa trên email và cột chỉ định
    # chuyển dữ liệu qua bảng mới basic_login_register2
    update_query = f"UPDATE booking_tour_basic1 SET {column} = ? WHERE id = ?"
    
    # Thực thi truy vấn với các giá trị thay thế
    cursor.execute(update_query, (value, id))
    
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# delete
def delete_data_booking_tour_by_id(id):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/booking_tour.db')

    cursor = conn.cursor()
    
    # Xây dựng truy vấn SQL để cập nhật dòng dựa trên email và cột chỉ định
    # Xây dựng truy vấn SQL để xóa dòng dựa trên id
    delete_query = "DELETE FROM booking_tour_basic1 WHERE id = ?"
    
    # Thực thi truy vấn với giá trị thay thế
    cursor.execute(delete_query, (id,))
    
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# delete
def delete_data_booking_tour_by_email_and_created_time(email,createdTime):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/booking_tour.db')

    cursor = conn.cursor()
    
    # Xây dựng truy vấn SQL để cập nhật dòng dựa trên email và cột chỉ định
    # Xây dựng truy vấn SQL để xóa dòng dựa trên id
    delete_query = "DELETE FROM booking_tour_basic1 WHERE email = ? AND createdTime = ? "
    
    # Thực thi truy vấn với giá trị thay thế
    cursor.execute(delete_query, (email,createdTime))
    
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

def query_database_for_booking_tour_by_email(email):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/booking_tour.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng và sắp xếp theo id giảm dần
    cursor.execute(f"SELECT * FROM booking_tour_basic1 WHERE email=? ORDER BY id DESC LIMIT 1", (email,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()
    if data:
        columns = ['id', 'fullname', 'email', 'timeCheckin', 'days', 'booking_tour_name', 'price', 'number_adults', 'number_children', 'hotel_infor', 'createdTime','admin_check_payment']
        data_dict = dict(zip(columns, data))
        return data_dict
    else:
        return None
    
# def query_database_for_booking_tour_by_email(email):
#     # Kết nối tới cơ sở dữ liệu
#     conn = sqlite3.connect('database/booking_tour.db')
#     cursor = conn.cursor()

#     # Thực hiện truy vấn dữ liệu từ bảng và sắp xếp theo id giảm dần
#     cursor.execute(f"SELECT * FROM booking_tour_basic1 WHERE email=? ORDER BY id DESC LIMIT 1", (email,))
#     data = cursor.fetchone()

#     # Đóng kết nối
#     conn.close()
#     if data:
#         columns = ['id', 'fullname', 'email', 'timeCheckin', 'days', 'booking_tour_name', 'price', 'number_adults', 'number_children', 'hotel_infor', 'createdTime']
#         data_dict = dict(zip(columns, data))
#         return data_dict
#     else:
#         return None
    
def query_database_for_booking_tour_by_id( id):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/booking_tour.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    # chuyển dữ liệu qua bảng mới basic_login_register2
    cursor.execute(f"SELECT * FROM booking_tour_basic1 WHERE id=?", (id,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()
    if data:
        columns = ['id','fullname', 'email', 'timeCheckin', 'days', 'booking_tour_name', 'price', 'number_adults', 'number_children', 'hotel_infor', 'createdTime','admin_check_payment']
        data_dict = dict(zip(columns, data))
        return data_dict
    else:
        return None

def query_database_for_booking_tour_by_email_all(email):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/booking_tour.db')
    cursor = conn.cursor()

    # Lấy thời gian hiện tại
    current_time = datetime.datetime.now()

    # Thực hiện truy vấn dữ liệu từ bảng và sắp xếp theo id giảm dần và timeCheckin > time hiện tại
    cursor.execute(f"SELECT * FROM booking_tour_basic1 WHERE email=? AND timeCheckin > ? ORDER BY id DESC", (email, current_time))
    data = cursor.fetchall()

    # Đóng kết nối
    conn.close()

    if data:
        columns = ['id', 'fullname', 'email', 'timeCheckin', 'days', 'booking_tour_name', 'price', 'number_adults', 'number_children', 'hotel_infor', 'createdTime','admin_check_payment']
        data_list = []
        for row in data:
            data_dict = dict(zip(columns, row))
            data_list.append(data_dict)
        return data_list
    else:
        return None

# delete_data_booking_tour_by_id(id=2)

# a = query_database_for_booking_tour_by_email(email="quyet12306@gmail.com")
# print(a)

# save_data_for_booking_tour_basic_in_table(
#                 booking_tour_name="test1",
#                 createdTime=gettime2(),
#                 days=7,
#                 email="quyet12306@gmail.com",
#                 fullname="full name test",
#                 hotel_infor="name_hotel",
#                 number_adults= 3,
#                 number_children=2,
#                 price="price",
#                 timeCheckin="2023-09-20"
#             )

# delete_data_booking_tour_by_email_and_created_time(email="quyet12306@gmail.com",createdTime="2023-10-30 21:32:28")

# for i in range(5):
#     b = query_database_for_booking_tour_by_id(id=i)
#     print(b)

# d = query_database_for_booking_tour_by_email_all(email="quyet12306@gmail.com")
# print(d)



