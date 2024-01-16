import sqlite3

from base_code.cover_base_64_img import convert_image_to_base64
from base_code.base import doc_du_lieu,tach_doan_text,random_decimal,random_number_price,random_number_rivew
from base_code.gettime import gettime2


def create_database_for_offer_basic(tablename):
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/offer.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE {tablename}
                  (id INTEGER PRIMARY KEY,
                   id_hotel TEXT,
                   hotel_name TEXT,
                   stars TEXT,
                   price TEXT,
                   num_reviews TEXT,
                   avata_img TEXT,
                   describe_hotel TEXT,
                   createdTime TEXT)''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# create_database_for_offer_basic(tablename="offer_basic")

def query_database_for_offer_by_id_hotel( id_hotel):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/offer.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    # chuyển dữ liệu qua bảng mới basic_login_register2
    cursor.execute(f"SELECT * FROM offer_basic WHERE id_hotel=?", (id_hotel,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()
    if data:
        columns = ['id', 'id_hotel', 'hotel_name', 'stars','price','num_reviews' ,'avata_img','describe_hotel', 'createdTime']
        data_dict = dict(zip(columns, data))
        
        return data_dict
    else:
        return None
    
def query_database_for_offer_by_id_hotel_order_by( ):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/offer.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    # chuyển dữ liệu qua bảng mới basic_login_register2
    
    # cursor.execute(f"SELECT * FROM offer_basic order by CAST(num_reviews AS INTEGER) DESC ", (id_hotel,))
    cursor.execute(f"SELECT * FROM offer_basic WHERE num_reviews = 40 or num_reviews = 50 or num_reviews = 70 ORDER BY CAST(num_reviews AS INTEGER) DESC ,CAST(stars AS FLOAT) ASC ")
    data = cursor.fetchall()

    
    # Đóng kết nối
    conn.close()
    if data:
        columns = ['id', 'id_hotel', 'hotel_name', 'stars','price','num_reviews' ,'avata_img','describe_hotel', 'createdTime']

        data_dict = dict(zip(columns, zip(*data)))
        return data_dict
    else:
        return None
    
    # return data

    

# lưu dữ liệu 
def save_data_for_offer_in_table( id_hotel, hotel_name,stars,price,num_reviews,avata_img,describe_hotel,createdTime ):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/offer.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng diseases
    # chuyển dữ liệu qua bảng mới basic_login_register2
    # if birthday is None and avata_img is None:
    #     birthday = avata_img == ""
    cursor.execute(f"INSERT INTO offer_basic ( id_hotel, hotel_name,stars,price,num_reviews,avata_img,describe_hotel,createdTime) VALUES (?,?,?,?,?,?,?,?)",
               ( id_hotel, hotel_name,stars,price,num_reviews,avata_img,describe_hotel,createdTime))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

def sort_data_offer_database(table_name,price_offer=None,name_hotel_offer=None,star_offer=None,distance_offer=None,review_offer=None):
    conn = sqlite3.connect('database/offer.db')
    cursor = conn.cursor()
    query_text1 = ""
    query_text2 = ""
    order_by_conditions = []
    where_by_conditions = []
    
    if price_offer is not None:
        if price_offer == "show_all_price":
            pass
        elif price_offer == "ascending_price":
            order_by_conditions.append(f"CAST(price AS INTEGER) ASC ")
            # query_text2 = query_text2 + f"CAST(price AS INTEGER) ASC "
        elif price_offer == "decrease_price":
            order_by_conditions.append(f"CAST(price AS INTEGER) DESC")
            # query_text2 = query_text2 + f"CAST(price AS INTEGER) DESC " 
        else:
            print(f'The value "price_offer" entered is invalid')
    if name_hotel_offer is not None:
        if name_hotel_offer == "default_name_hotel":
            pass
        elif name_hotel_offer == "a_to_z_location":
            order_by_conditions.append(f"CAST(hotel_name AS TEXT) ASC")
        else:
            print(f'The value "name_hotel_offer" entered is invalid')    
    if star_offer is not None:
        if star_offer == "show_all_star":
            pass
        elif star_offer == "ascending_star":
            order_by_conditions.append(f"CAST(stars AS FLOAT) ASC")
        elif star_offer == "decrease_star":
            order_by_conditions.append(f"CAST(stars AS FLOAT) DESC")
        elif star_offer == "3_star":
            where_by_conditions.append(f"stars LIKE '3.%'")
        elif star_offer == "4_star":
            where_by_conditions.append(f"stars LIKE '4.%'")
        elif star_offer == "5_star":
            where_by_conditions.append(f"stars LIKE '5.%'")
        else:
            print(f'The value "star_offer" entered is invalid')
    if distance_offer is not None:
        if distance_offer == "default_distance":

            pass
    if review_offer is not None:
        if review_offer == "default_review":
            pass
        elif review_offer == "ascending_review":
            order_by_conditions.append(f"CAST(num_reviews AS INTEGER) ASC")
        elif review_offer == "decrease_review":
            order_by_conditions.append(f"CAST(num_reviews AS INTEGER) DESC")
        else:
            print(f'The value "review_offer" entered is invalid') 
            
    if len(order_by_conditions) > 0:
        query_text1 = ", ".join(order_by_conditions)
        order_by_word = "ORDER BY"
    else:
        order_by_word = ""
    if len(where_by_conditions) > 0:
        query_text2 = "AND ".join(where_by_conditions)
        where_word = "WHERE"
    else:
        where_word = ""

    print(f'SELECT * FROM {table_name} {where_word} {query_text2} {order_by_word} {query_text1}')
    final_query_text = f'SELECT * FROM {table_name}'
    cursor.execute(f"SELECT * FROM {table_name} {where_word} {query_text2} {order_by_word} {query_text1}")
    data = cursor.fetchall()
    conn.close()
    if data:
        columns = ['id', 'id_hotel', 'hotel_name', 'stars','price','num_reviews' ,'avata_img','describe_hotel', 'createdTime']

        data_dict = dict(zip(columns, zip(*data)))
        return data_dict
    else:
        return None

# a = doc_du_lieu(file_path="test3.txt")
# # print(a)
# ket_qua = tach_doan_text(a)

# for i, (ten_khach_san, mo_ta) in enumerate(ket_qua):
#     # print(f"Đoạn {i+1}:")
#     star = random_decimal(end=5,start=3)
#     price = random_number_price(start=6,end=20)
#     number_review = random_number_rivew(start=2,end=20)
#     id_hotel = 1000 + i
#     print(id_hotel)
#     print(star)
#     print(i)
#     img_base64_str = convert_image_to_base64(image_path=f"img\\img_hotels\\anh{i+2}.jpeg")
#     print("Tên khách sạn:", ten_khach_san)
#     print("Mô tả:", mo_ta)
#     print()
#     save_data_for_offer_in_table(describe_hotel=mo_ta,avata_img=img_base64_str,createdTime=gettime2(),hotel_name=ten_khach_san,id_hotel=id_hotel,num_reviews=number_review,price=price,stars=star)

# d = query_database_for_offer_by_id_hotel(id_hotel=f"1001")
# print(f'id = {d["id"]}')
# print(f'id_hotel = {d["id_hotel"]}')
# print(f'hotel_name = {d["hotel_name"]}')
# print(f'stars = {d["stars"]}')
# print(f'price = {d["price"]}')
# print(f'num_reviews = {d["num_reviews"]}')
# print(f'createdTime = {d["createdTime"]}')

# a = query_database_for_offer_by_id_hotel_order_by()
# print(len(a))
# print(type(a[1]))

# a = query_database_for_offer_by_id_hotel_order_by()
# a = sort_data_offer_database(
#     star_offer="show_all_star",
#     review_offer="default_review",
#     price_offer="show_all_price",
#     distance_offer="default_distance",
#     name_hotel_offer="default_name_hotel",
#     table_name=f"offer_basic"
#     )
# print(a["hotel_name"])
# print(a["num_reviews"])
# print(a["stars"])
# print(a["price"])

