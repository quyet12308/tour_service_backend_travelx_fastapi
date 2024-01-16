import sqlite3




def create_database_for_contact(tablename):
    
    # Kết nối tới cơ sở dữ liệu (hoặc tạo mới nếu chưa tồn tại)
    conn = sqlite3.connect('database/contact.db')

    # Tạo một đối tượng cursor để thực thi truy vấn
    cursor = conn.cursor()
    
        # Tạo bảng diseases
    cursor.execute(f'''CREATE TABLE {tablename}
                  (id INTEGER PRIMARY KEY,
                   username TEXT,
                   email TEXT,
                   subject TEXT,
                   message TEXT,
                   createdTime TEXT)''')
    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# create_database_for_contact(tablename='contact_basic')

# lưu dữ liệu đăng nhập
def save_data_for_contact_in_table( username,email, subject,message,createdTime):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/contact.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng diseases
    cursor.execute(f"INSERT INTO contact_basic (username,email, subject,message,createdTime) VALUES (?,?,?,?,?)",
               (username,email, subject,message,createdTime ))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()


# truy vấn token bằng email
def query_data_for_contact_in_table_by_email( email):
    # Kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('database/contact.db')
    cursor = conn.cursor()

    # Thực hiện truy vấn dữ liệu từ bảng
    cursor.execute(f"SELECT * FROM contact_basic WHERE email=?", (email,))
    data = cursor.fetchone()

    # Đóng kết nối
    conn.close()

    return data