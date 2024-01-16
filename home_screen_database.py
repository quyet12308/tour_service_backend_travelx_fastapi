import sqlite3
import json
from base_code.gettime import gettime2
from base_code.cover_base_64_img import convert_image_to_base64,show_image_from_base64,write_to_text_file

# bảng data địa điểm du lịch để get khi hiển thị 

def create_database_for_tourist_destination_information(tablename):
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/tourist_destination_information.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE {tablename}
                  (id INTEGER PRIMARY KEY,
                   tourist_destination_name TEXT NOT NULL,
                   img_base64 TEXT NOT NULL,
                   price TEXT NOT NULL,
                   the_right_time_to_go TEXT NOT NULL,
                   createdTime TEXT NOT NULL,
                   tourist_destination_describe TEXT NOT NULL,
                   tourist_destination_location TEXT NOT NULL,
                   number_of_stars TEXT NOT NULL,
                   number_of_travel_days TEXT NOT NULL,
                   lat TEXT NOT NULL,
                   lon TEXT NOT NULL
                   )''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# create_database_for_tourist_destination_information(tablename='tourist_destination_information_basic_for_get_data2')

# lưu dữ liệu đăng nhập
def save_data_in_table_tourist_destination_information( tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/tourist_destination_information.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng diseases
    cursor.execute(f"INSERT INTO tourist_destination_information_basic_for_get_data (tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days) VALUES (?,?,?,?,?,?,?,?,?)",
               (tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars,number_of_travel_days ))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

def save_data_in_table_tourist_destination_information2( tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days,lat,lon):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/tourist_destination_information.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng diseases
    cursor.execute(f"INSERT INTO tourist_destination_information_basic_for_get_data2 (tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days,lat,lon) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
               (tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars,number_of_travel_days ,lat,lon))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()


# truy vấn token bằng email
def query_database_for_tourist_destination_information_by_id( id):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/tourist_destination_information.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM tourist_destination_information_basic_for_get_data2 WHERE id=?", (id,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    # return data
    if data:
        columns = ['id','tourist_destination_name', 'img_base64', 'price', 'the_right_time_to_go', 'createdTime', 'tourist_destination_describe', 'tourist_destination_location', 'number_of_stars', 'number_of_travel_days','lat','lon','hotel_info','flight_info']
        data_dict = dict(zip(columns, data))
        return data_dict
    else:
        return None

def query_database_for_tourist_destination_information_by_name( name):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/tourist_destination_information.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM tourist_destination_information_basic_for_get_data2 WHERE tourist_destination_name=?", (name,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    # return data
    if data:
        columns = ['id','tourist_destination_name', 'img_base64', 'price', 'the_right_time_to_go', 'createdTime', 'tourist_destination_describe', 'tourist_destination_location', 'number_of_stars', 'number_of_travel_days','lat','lon','hotel_info','flight_info']
        data_dict = dict(zip(columns, data))
        return data_dict
    else:
        return None
    
def query_database_for_tourist_destination_information_all_table():
    conn = sqlite3.connect('database/tourist_destination_information.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM tourist_destination_information_basic_for_get_data2 ")
    data = cursor.fetchall()

    # Đóng kết nối
    conn.close()

    # return data
    if data:
        columns = ['id','tourist_destination_name', 'img_base64', 'price', 'the_right_time_to_go', 'createdTime', 'tourist_destination_describe', 'tourist_destination_location', 'number_of_stars', 'number_of_travel_days','lat','lon','hotel_info','flight_info']
        data_dict = dict(zip(columns, zip(*data)))
        return data_dict
    else:
        return None

def update_data_tourist_destination_information_by_id(id, column, value):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/tourist_destination_information.db')
    cursor = conn.cursor()
    
    # Xây dựng truy vấn SQL để cập nhật dòng dựa trên email và cột chỉ định
    # chuyển dữ liệu qua bảng mới basic_login_register2
    update_query = f"UPDATE tourist_destination_information_basic_for_get_data2 SET {column} = ? WHERE id = ?"
    
    # Thực thi truy vấn với các giá trị thay thế
    cursor.execute(update_query, (value, id))
    
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# thêm cột vào bảng
def add_more_column_to_table_tourist_destination_information(column_name,column_type):
    conn = sqlite3.connect('database/tourist_destination_information.db')
    cursor = conn.cursor()

    # Thêm cột mới 
    cursor.execute(f"ALTER TABLE tourist_destination_information_basic_for_get_data2 ADD COLUMN {column_name} {column_type}")

    # Lưu thay đổi
    conn.commit()

    # Đóng kết nối
    conn.close()

# add_more_column_to_table_tourist_destination_information(column_type="TEXT",column_name="hotel_info")
# add_more_column_to_table_tourist_destination_information(column_type="TEXT",column_name="flight_info")


# loại file database
def create_database_for_type_file_img(tablename):
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/tourist_destination_information.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE {tablename}
                  (id INTEGER PRIMARY KEY,
                   tourist_destination_name TEXT NOT NULL,
                   type_of_file_img TEXT NOT NULL)''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# create_database_for_type_file_img(tablename='type_of_file_img')

# lưu dữ liệu đăng nhập
def save_data_in_table_type_file_img(type_of_file_img,tourist_destination_name):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/tourist_destination_information.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng diseases
    cursor.execute(f"INSERT INTO type_of_file_img (type_of_file_img,tourist_destination_name) VALUES (?,?)",
               (type_of_file_img ,tourist_destination_name))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()



def query_database_for_type_file_img_by_id( id):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/tourist_destination_information.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM type_of_file_img WHERE id=?", (id,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    return data



# def query_database_for_type_file_img_and_tourist_destination_information_by_id( id):
#     # Kết nối tới cơ sở dữ liệu
#     conn = sqlite3.connect('database/tourist_destination_information.db')
#     cursor = conn.cursor()

#     # Thực hiện truy vấn dữ liệu từ bảng
#     cursor.execute(f"""SELECT *
#                         FROM type_of_file_img
#                         INNER JOIN tourist_destination_information_basic_for_get_data ON type_of_file_img.tourist_destination_name = tourist_destination_information_basic_for_get_data.tourist_destination_name;
#                         WHERE id=?""", (id,))
#     data = cursor.fetchone()

#     # Đóng kết nối
#     conn.close()

#     return data

def get_all_data_from_table(table_name,database_path):
    # Kết nối tới cơ sở dữ liệu SQLite
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Truy vấn lấy tất cả dữ liệu từ bảng
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)

    # Lấy tất cả các hàng dữ liệu
    rows = cursor.fetchall()

    # Đóng kết nối và trả về kết quả
    conn.close()
    return rows



# Sử dụng hàm để lấy dữ liệu từ bảng "my_table"
# database_path = 'database\\tourist_destination_information.db'
# table_name = "type_of_file_img"
# data = get_all_data_from_table(database_path=database_path,table_name=table_name)
# print(data)
# print(type(data))
# print(data[1])
# print(data[1][1])

# save_data_in_table_tourist_destination_information(
#     createdTime=gettime2(),
#     img_base64=convert_image_to_base64("img\\thac_havasu_arizona.jpg"),
#     number_of_stars="4.2",
#     price="1150",
#     number_of_travel_days="8",
#     the_right_time_to_go="every day of the year",
#     # the_right_time_to_go="from May to September",
#     tourist_destination_describe="Thác Havasu là một thác nước nằm trên nhánh Havasu Creek, thuộc Grand Canyon, Arizona, Hoa Kỳ. Thác nước nằm trong vùng đất của bộ lạc Havasupai. Đây là thác nước nổi tiếng nhất trong số các thác dọc theo Havasu Creek. Thác nước hùng vĩ này có độ cao 27 mét, nước chảy xuống từ một vách đá thẳng đứng cao 30 mét xuống một hồ bơi lớn. Do hàm lượng khoáng chất cao trong nước, hình dạng của thác nước luôn luôn thay đổi, đôi khi tạo thành hai máng nước riêng biệt rất đặc sắc. Nhờ lượng Canxi Carbonat và Magiê khá lớn, hồ nước tự nhiên phía dưới thác có màu ngọc lam đẹp mắt. Bạn sẽ phải cuốc bộ cả chục dặm trước khi có thể hòa mình vào dòng nước xanh mát gần công viên quốc gia Grand Canyon này, nhưng đây cũng là dịp lý tưởng để ngắm cảnh dọc đường.",
#     tourist_destination_location="Grand Canyon, Arizona, Hoa Kỳ",
#     tourist_destination_name="Thác Havasu, Arizona"
# )

# for i in range(20):
#     a = query_database_for_tourist_destination_information_by_id(i)
#     if a:
#         id ,tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days = a
#         print(f"{tourist_destination_name}, {tourist_destination_location}")


#     else:
#         print(f"id {i} chưa có data")


#test show img by load data from sqlite
# b = query_database_for_tourist_destination_information_by_id(3)
# id ,tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days = b
# show_image_from_base64(base64_string=img_base64)

data_dict = {
'Đại thánh đường Sheikh Zayed, Abu Dhabi':'jpg',
'Đông Xuyên, Trung Quốc':'jpg',
'Ốc đảo sa mạc Huacachina':'jpg',
'Cửu Trại Câu':'webp',
'Isola Bella':'jpg',
'Nhà thờ Las Lajas':'jpg',
'LonDon':'jpg',
'Mauritius':'webp',
'Lệ giang cổ trấn':'webp',
'Phúc Kiến Thổ Lâu':'webp',
'Phượng Hoàng Cổ Trấn':'webp',
'Popeye, Malta':'jpg',
'Santorini Greece':'jpg',
'Scotland':'jpg',
'Setenil de las Bodegas':'jpg',
'Thung lũng Shangrila':'webp',
'Thác Havasu, Arizona':'jpg'
}

# data5 = 'tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars,number_of_travel_days'
# data5s = data5.split(",")
# print(data5s)
# for i in range(len(data5s)):
#     d = f"data{i} = a['{data5s[i]}']"
#     print(d)
    

# for destination, file_type in data_dict.items():
#     save_data_in_table_type_file_img(type_of_file_img=file_type, tourist_destination_name=destination)

# for i in range(20):
#     print(query_database_for_type_file_img_by_id(i))

# d = query_database_for_type_file_img_and_tourist_destination_information_by_id(id=2)
# write_to_text_file(data=d,file_path="test_data2.txt")


cau_truc_bang = [(0, 'id', 'INTEGER', 0, None, 1), (1, 'tourist_destination_name', 'TEXT', 1, None, 0), (2, 'img_base64', 'TEXT', 1, None, 0), (3, 'price', 'TEXT', 1, None, 0), (4, 'the_right_time_to_go', 'TEXT', 1, None, 0), (5, 'createdTime', 'TEXT', 1, None, 0), (6, 'tourist_destination_describe', 'TEXT', 1, None, 0), (7, 'tourist_destination_location', 'TEXT', 1, None, 0), (8, 'number_of_stars', 'TEXT', 1, None, 0), (9, 'number_of_travel_days', 'TEXT', 1, None, 0)]

data_test = data_dict.keys()
# print(data_test)
# print(type(data_test))
# for i in data_test:
#     print(i)
#     a = query_database_for_tourist_destination_information_by_name(name=i)
#     if a is None:
#         print("none=====================================================================================")
#     else:
#         data0 = a['tourist_destination_name']
#         data1 = a['img_base64']
#         data2 = a['price']
#         data3 = a['the_right_time_to_go']
#         data4 = a['createdTime']
#         data5 = a['tourist_destination_describe']
#         data6 = a['tourist_destination_location']
#         data7 = a['number_of_stars']
#         data8 = a['number_of_travel_days']
#         data8 = a['number_of_travel_days']
#         data9 = a['id']
#         print(f"name = {data0}")
#         print(data2)
#         print(data3)
#         print(data4)
#         print(data5)
#         print(data6)
#         print(data7)
#         print(data8)
#         print(data9)

# for i in range(20):
#     f = query_database_for_tourist_destination_information_by_id(id=i)
#     if f is None:
#         print(f"{i} = none")
#     else:
#         print(f['tourist_destination_name'])

# g = query_database_for_tourist_destination_information_by_name(name="Lệ giang cổ trấn")
# print(g)
# print(g["tourist_destination_name"])



lat_and_lon = ['24.28 54.22', '35.04 109.05', '-12.2 -77.2', '33.12 103.54', '45:53 8:31', '0.48 -77.35', '51.30 -0.7', '-20.12 57.30', '26.52 100.14', '25.1 117.41', '27.56 109.36', '35.58 14.20', '36.24 25.25', '57 -4', '36.51 -5.10', '27.50 99.42', '36.15 -112.41']

# for i in range(17):
#     q = query_database_for_tourist_destination_information_by_id(i+1)
#     tourist_destination_name = q["tourist_destination_name"]
#     img_base64 = q["img_base64"]
#     price = q["price"]
#     the_right_time_to_go = q["the_right_time_to_go"]
#     tourist_destination_describe = q["tourist_destination_describe"]
#     tourist_destination_location = q["tourist_destination_location"]
#     number_of_stars = q["number_of_stars"]
#     number_of_travel_days = q["number_of_travel_days"]
#     createdTime = q["createdTime"]

# # for i in range(len(lat_and_lon)):
#     # print(i)
#     a = lat_and_lon[i]
#     # print(a)
#     # lat_and_lon = lat_and_lon.strip()
#     lat = a.split(" ")[0]
#     lon = a.split(" ")[1]
#     # print(f"lat = {lat}")
#     # print(f"lon = {lon}")
#     save_data_in_table_tourist_destination_information2(
#         lon=lon,
#         createdTime=createdTime,
#         img_base64=img_base64,
#         lat=lat,
#         number_of_stars=number_of_stars,
#         number_of_travel_days=number_of_travel_days,
#         price=price,
#         the_right_time_to_go=the_right_time_to_go,
#         tourist_destination_describe=tourist_destination_describe,
#         tourist_destination_location=tourist_destination_location,
#         tourist_destination_name=tourist_destination_name
#     )
 
# update_data_tourist_destination_information_by_id(value="45.53",column="lat",id=5)
# update_data_tourist_destination_information_by_id(value="8.31",column="lon",id=5)

# k = query_database_for_tourist_destination_information_all_table()
# print(k["tourist_destination_name"])
# print(k["id"])


# id_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)

v = ('Đại thánh đường Sheikh Zayed, Abu Dhabi',#1
      'Đông Xuyên, Trung Quốc', 
      'Ốc đảo sa mạc Huacachina', #3
      'Cửu Trại Câu', 
      'Isola Bella', #5
      'Nhà thờ Las Lajas', 
      'LonDon', #7
      'Mauritius', 
      'Lệ giang cổ trấn', #9
      'Phúc Kiến Thổ Lâu', 
      'Phượng Hoàng Cổ Trấn', #11
      'Popeye, Malta', #12
      'Santorini Greece', 'Scotland', 'Setenil de las Bodegas', 'Thung lũng Shangrila', 'Thác Havasu, Arizona')

def cover_to_json_hotel_data(name , img , describe, star , link,some_amenities):
    data = {
        "name" : name,
        "img" : img,
        "describe" : describe,
        "star" :star,
        "link":link,
        "some_amenities":some_amenities
    }
    return json.dumps(data,ensure_ascii=False)




# a = cover_to_json_hotel_data(
#     describe="Nơi nghỉ ở Lake Havasu City này cách Cầu Luân Đôn 5 phút lái xe. Nơi nghỉ này có 3 hồ bơi ngoài trời, 3 bể sục và bãi đậu xe có mái che miễn phí. Havasu Dunes có bếp nhỏ hoặc nhà bếp đầy đủ tiện nghi trong mỗi chỗ ở. Truyền hình cáp và đầu đĩa DVD cũng được bao gồm. Du khách có thể sử dụng phòng xông hơi khô hoặc tiện nghi giặt là tại Havasu Dunes. Tiện nghi nướng thịt bằng gas và Wi-Fi cũng được cung cấp. Công viên Tiểu bang Hồ Havasu cách Cồn cát WorldMark Havasu khoảng 8 km. Trung tâm mua sắm thời trang Island cách nơi nghỉ này 5 phút lái xe.",
#     img=convert_image_to_base64(image_path="test_python_code\\img\\17.jpg"),
#     link="https://www.booking.com/hotel/us/havasu-dunes-resort.vi.html?aid=318615&label=New_English_EN_VI_27026991385-SbfX4qC7oAyHRYJK_yRWPwS640819031013%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi55438833383%3Atiaud-297601666475%3Adsa-302962658775%3Alp1028580%3Ali%3Adec%3Adm%3Aag27026991385%3Acmp400679185&sid=4dd67f0c693c47ca078e452bc0859ff5&dest_id=20006548&dest_type=city&dist=0&group_adults=2&group_children=0&hapos=1&hpos=1&no_rooms=1&req_adults=2&req_children=0&room1=A%2CA&sb_price_type=total&sr_order=popularity&srepoch=1698589991&srpvid=a332665033b40130&type=total&ucfs=1&activeTab=main",
#     name="WorldMark Havasu Dunes",
#     star="4.4",
#     some_amenities = ['Giặt ủi', 'Tiện nghi BBQ', 'Khu vực xem TV/sảnh chung', 'Sân gôn (trong vòng 3km)', 'Đi bộ đường dài', 'Hệ thống sưởi', 'Hồ bơi ngoài trời', 'Bãi đỗ xe miễn phí', 'Ghế/ghế dài tắm nắng', 'Phòng không hút thuốc']
#     )

# print(a)


# update_data_tourist_destination_information_by_id(column="hotel_info",value=a,id=17) # đang làm đến cái id thứ 5 
# update_data_tourist_destination_information_by_id(column="hotel_info",value=a,id=17) # đang làm đến cái id thứ 5 

# b = query_database_for_tourist_destination_information_by_id(id=1)
# # print(b["hotel_info"]["some_amenities"])
# print(type(b))
# print(type(b["hotel_info"]))

# data_load = json.loads(b["hotel_info"])
# print(type(data_load))
# print(data_load["some_amenities"])