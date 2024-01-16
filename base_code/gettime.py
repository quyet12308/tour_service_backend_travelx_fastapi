from datetime import datetime, timedelta

import datetime
# from datetime import datetime, timedelta
import pytz
# from datetime import timedelta


def gettime2():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))
    t = local_time.strftime("%Y-%m-%d %H:%M:%S")
    return t

def gettime3():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))
    t = local_time.strftime("%Y_%m_%d")
    return t

def gettime4():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))
    t = local_time.strftime("%Y-%m-%d")
    return t



def check_time_range(created_time, now_time, minute):
    # Chuyển đổi chuỗi thời gian thành đối tượng datetime
    created_datetime = datetime.datetime.strptime(created_time, "%Y-%m-%d %H:%M:%S")
    now_datetime = datetime.datetime.strptime(now_time, "%Y-%m-%d %H:%M:%S")

    # Tính toán khoảng thời gian giữa hai thời điểm
    time_difference = now_datetime - created_datetime

    # Chuyển đổi số phút thành đối tượng timedelta
    minute_delta = datetime.timedelta(minutes=minute)

    # So sánh khoảng thời gian với tham số phút
    if time_difference >= minute_delta:
        return False
    else:
        return True
    


def check_time_range2(date1, date2,days):
    # Chuyển đổi hai chuỗi thời gian thành đối tượng datetime
    date1_obj = datetime.datetime.strptime(date1, "%Y-%m-%d")
    date2_obj = datetime.datetime.strptime(date2, "%Y-%m-%d")

    # Tính khoảng thời gian giữa hai ngày
    time_delta = date2_obj - date1_obj

    # Kiểm tra xem khoảng thời gian có vượt quá 3 ngày hay không
    if time_delta > timedelta(days=days):
        return True
    else:
        return False
    
# a = check_time_range2(date1="2023-11-01",date2="2023-11-03",days=3)
# print(a)



def check_availability(time1, time2, days):
    # Chuyển đổi chuỗi thời gian thành đối tượng datetime
    time1 = datetime.datetime.strptime(time1, "%Y-%m-%d")
    time2 = datetime.datetime.strptime(time2, "%Y-%m-%d")

    # Tính toán thời gian kết thúc (time1 + days)
    end_time = time1 + timedelta(days=days)

    # Kiểm tra nếu time2 nằm ngoài phạm vi time1 + days
    if time2 < time1 or time2 > end_time:
        return True
    else:
        return False
    
# a = check_availability(time1="2023-11-01",time2="2023-11-05",days=3)
# print(a)
    
# created_time = "2023-09-14 10:01:00"
# now_time = "2023-09-14 10:04:59"
# minute = 3

# result = check_time_range(created_time, now_time, minute)
# print(result)  # True nếu khoảng thời gian không vượt qua tham số minute, False nếu vượt qua

# print(gettime3())