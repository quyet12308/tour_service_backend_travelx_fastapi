import asyncio
import json
from fastapi import FastAPI, HTTPException # import fastapi để sử dụng trong dự án
from fastapi.middleware.cors import CORSMiddleware # import thư viện cors để bỏ chặn bảo mật giữa frontend và backend
from pydantic import BaseModel
from base_code.security_info import *
from base_code.string_python_en import responses
from base_code.get_token import generate_random_token_string
from base_code.base import *
from base_code.gettime import *
from base_code.get_token import *
from base_code.get_code import *
from email_with_python.send_emails import *
from contact_database import *
from check_database import *
from home_screen_database import *
from connect_open_weather_api import *
from offers_database import *
from booking_tour_database import *

app = FastAPI() # khởi tạo app fastapi

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #  chỉ định các nguồn mà bạn muốn chấp nhận yêu cầu từ server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# chức năng contact
@app.post("/api/contact_basic")
async def contact_basic(request_data: dict):
    if request_data:
        name = request_data['name']
        subject = request_data['subject']
        email = request_data['email']
        message = request_data['message']

        tim_now = gettime2()

        save_data_for_contact_in_table(createdTime=tim_now,email=email,username=name,message=message,subject=subject) # lưu thông tin contact
        send_email_reminder_admin_about_contact_customer(username=name,created_time=tim_now,password=passwords["outlook"],to_email=emails["email_admin"]) #gửi email cho admin
        return {"response":{
                        "message":responses["cam_on_dong_gop_cua_ban"],
                        "status":True
                    }}
    
# hiển thị tour trên trang chính
@app.get("/api/get_tourist_destination_information")
async def get_tourist_destination_information():
    tourist_destination_name_arr = []
    img_base64_arr = []
    price_arr = []
    the_right_time_to_go_arr = []
    tourist_destination_describe_arr = []
    tourist_destination_location_arr = []
    number_of_stars_arr = []
    number_of_travel_days_arr = []
    type_file_arr = []
    max_id = get_max_id_from_table(path_of_database='database\\tourist_destination_information.db',table_name="type_of_file_img")
    random_num_list = random_3_numbers(end=max_id,start=1)
    for i in range(3):

        # max_id = get_max_id_from_table(path_of_database='database\\tourist_destination_information.db',table_name="type_of_file_img")
        # randum_num = random_number(end=max_id,start=1)
        ttestdata =  query_database_for_tourist_destination_information_by_id(random_num_list[i]) # lấy thông tin các tour du lịch
        testdata2 = query_database_for_type_file_img_by_id(random_num_list[i])
        id_ , name_ , type_file_ = testdata2
        # id ,tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days = ttestdata
        
        tourist_destination_name = ttestdata["tourist_destination_name"]
        img_base64 = ttestdata["img_base64"]
        price = ttestdata["price"]
        the_right_time_to_go = ttestdata["the_right_time_to_go"]
        tourist_destination_describe = ttestdata["tourist_destination_describe"]
        tourist_destination_location = ttestdata["tourist_destination_location"]
        number_of_stars = ttestdata["number_of_stars"]
        number_of_travel_days = ttestdata["number_of_travel_days"]

        tourist_destination_name_arr.append(tourist_destination_name)
        img_base64_arr.append(img_base64)
        price_arr.append(price)
        the_right_time_to_go_arr.append(the_right_time_to_go)
        tourist_destination_describe_arr.append(tourist_destination_describe)
        tourist_destination_location_arr.append(tourist_destination_location)
        number_of_stars_arr.append(number_of_stars)
        number_of_travel_days_arr.append(number_of_travel_days)
        type_file_arr.append(type_file_)

        
    return {
            "response":{
                "tourist_destination_name_arr":tourist_destination_name_arr,
                "img_base64_arr":img_base64_arr,
                "price_arr": price_arr,
                "the_right_time_to_go_arr":the_right_time_to_go_arr,
                "tourist_destination_describe_arr":tourist_destination_describe_arr,
                "tourist_destination_location_arr":tourist_destination_location_arr,
                "number_of_stars_arr":number_of_stars_arr,
                "number_of_travel_days_arr":number_of_travel_days_arr,
                "type_file_arr":type_file_arr
            }
        }

# hiện thông tin tour chi tiết 
@app.post("/api/get_tourist_destination_information_by_name")
async def tourist_destination_information_by_name(request_data: dict):
    if request_data:
        name_ = request_data["name"]
        token = request_data["token"]
        # print(name_)
        # get_all_data_from_table()
        
        data_ = query_database_for_tourist_destination_information_by_name(name=name_) # lấy thông tin các tour du lịch
        # print(data_)
        tourist_destination_name = data_["tourist_destination_name"]
        img_base64 = data_["img_base64"]
        price = data_["price"]
        the_right_time_to_go = data_["the_right_time_to_go"]
        tourist_destination_describe = data_["tourist_destination_describe"]
        tourist_destination_location = data_["tourist_destination_location"]
        number_of_stars = data_["number_of_stars"]
        number_of_travel_days = data_["number_of_travel_days"]
        lat = data_["lat"]
        lon = data_["lon"]
        hotel_info = data_["hotel_info"]
        five_day_weather_datas = get_5_datas_from_5_day_weather(lang="vi",lat=lat,lon=lon) # lấy thông tin thời tiết
        # id_ ,tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days = data_
        return {
            "response":{
                "status":True,
                'message':{
                    "tourist_destination_name":tourist_destination_name,
                    "img_base64":img_base64,
                    "price": price,
                    "the_right_time_to_go":the_right_time_to_go,
                    "tourist_destination_describe":tourist_destination_describe,
                    "tourist_destination_location":tourist_destination_location,
                    "number_of_stars":number_of_stars,
                    "number_of_travel_days":number_of_travel_days,
                    "five_day_weather_datas":five_day_weather_datas,
                    "hotel_info":hotel_info
                }
                
            }
        }



# chức năng offer hotel đăng hoàn thiện       
@app.post("/api/get_offer_data")
        
   
async def get_offer_data(request_data: dict):
    if request_data:

        price_offer = request_data["price_offer"]
        name_hotel_offer = request_data["name_hotel_offer"]
        star_offer = request_data["star_offer"]
        distance_offer = request_data["distance_offer"]
        review_offer = request_data["review_offer"]

        print(f"{price_offer} , {name_hotel_offer} , {star_offer} , {distance_offer} , {review_offer}")

        data = sort_data_offer_database(
            table_name="offer_basic",
            distance_offer=distance_offer,
            name_hotel_offer=name_hotel_offer,
            price_offer=price_offer,
            star_offer=star_offer,
            review_offer=review_offer
            )
        
        return {
            "response":{
                "status":True,
                'message':{
                    "id_hotel":data["id_hotel"],
                    "hotel_name":data["hotel_name"],
                    "stars": data["stars"],
                    "price":data["price"],
                    "num_reviews":data["num_reviews"],
                    "avata_img":data["avata_img"],
                    "describe_hotel":data["describe_hotel"]
                }
                
            }
        }  

@app.post("/api/the_blog")
async def the_blog(request_data: dict):
    if request_data:
        pass

@app.post("/api/booking_tour")
async def booking_tour(request_data: dict):
    if request_data:
        # print(request_data)
        full_name = request_data["full_name"]
        email = request_data["email"]
        num_adults = request_data["num_adults"]
        num_children = request_data["num_children"]
        time = request_data["time"]
        price = request_data["price"]
        name_tour = request_data["name_tour"]
        days = request_data["days"]
        name_hotel = request_data["name_hotel"]

        # check data
        data = query_database_for_booking_tour_by_email(email=email)
        if data == None:
            # save data
            t = gettime2()
            save_data_for_booking_tour_basic_in_table(
                booking_tour_name=name_tour,
                createdTime=t,
                days=days,
                email=email,
                fullname=full_name,
                hotel_infor=name_hotel,
                number_adults=num_adults,
                number_children=num_children,
                price=price,
                timeCheckin=time,
                admin_check_payment="0"
            )
            return  {
                "response":{
                    "status":True,
                    'message': responses["booking_tour_thanh_cong"]
                    
                }
            } 
        else:
            # print(data["days"])
            # print(data["timeCheckin"])
            # print(time)
            check_time = check_availability(days=int(data["days"]),time1=data["timeCheckin"],time2=time)
            if check_time:
                t = gettime2()
                save_data_for_booking_tour_basic_in_table(
                booking_tour_name=name_tour,
                createdTime=t,
                days=days,
                email=email,
                fullname=full_name,
                hotel_infor=name_hotel,
                number_adults=num_adults,
                number_children=num_children,
                price=price,
                timeCheckin=time,
                admin_check_payment="0"
            )
                return  {
                "response":{
                    "status":True,
                    'message': responses["booking_tour_thanh_cong"]
                    
                }
            }
            else:
                return  {
                "response":{
                    "status":False,
                    'message': responses["thoi_gian_nay_ban_dang_lua_chon_tour_du_lich_khac_roi"]
                    
                }
            } 

@app.post("/api/my_booking_tour")
async def my_booking_tour(request_data: dict):
    if request_data:
        email = request_data["email"]
        print(request_data)
        data_list = query_database_for_booking_tour_by_email_all(email=email)
        if data_list:
            img_tours = []
            for i in range(len(data_list)):
                name_tour = data_list[i]["booking_tour_name"]
                print(name_tour)
                data4 = query_database_for_tourist_destination_information_by_name(name=name_tour)
                img_tour = data4["img_base64"]
                img_tours.append(img_tour)
            return  {
                "response":{
                    "status":True,
                    'message': {
                        "data_list":data_list,
                        "img_tours_list":img_tours
                    }
                    
                }
            } 
        else:
            return  {
                "response":{
                    "status":False,
                    'message': responses["ban_chua_dang_ky_tour_du_lich_nao"]
                    
                }
            } 
@app.post("/api/delete_my_booking_tour")
async def delete_my_booking_tour(request_data: dict):
    if request_data:
        email = request_data["email"]
        created_time = request_data["created_time"]
        timeCheckin = request_data["timeCheckin"]
        # print(request_data)
        # print(timeCheckin)
        # print(created_time)

        time_now = gettime4()
        print(time_now)
        check_time = check_time_range2(date2=str(timeCheckin),date1=time_now,days=3)
        print(f"check time = {check_time}")
        if check_time:
            delete_data_booking_tour_by_email_and_created_time(createdTime=str(created_time),email=email)

            return  {
                "response":{
                    "status":True,
                    'message': responses["tour_du_lich_da_duoc_xoa_thanh_cong"]
                }
            }
        else:
            return  {
                "response":{
                    "status":False,
                    'message': responses["tour_da_het_thoi_gian_de_xoa"]
                }
            }

@app.get("/api/show_all_tour")
async def show_all_tour():
    data = query_database_for_tourist_destination_information_all_table()
    id_list = data['id']
    tourist_destination_name_list = data['tourist_destination_name']
    img_base64_list = data["img_base64"]
    price_list = data["price"]
    the_right_time_to_go_list = data["the_right_time_to_go"]
    number_of_stars_list = data["number_of_stars"]
    tourist_destination_describe_list = data["tourist_destination_describe"]
    tourist_destination_location_list = data["tourist_destination_location"]
    number_of_travel_days_list = data["number_of_travel_days"]
    hotel_info_list = data["hotel_info"]

    return  {
                "response":{
                    "status":True,
                    'message': {
                        "id_list":id_list,
                        "tourist_destination_name_list":tourist_destination_name_list,
                        "img_base64_list":img_base64_list,
                        "price_list":price_list,
                        "the_right_time_to_go_list":the_right_time_to_go_list,
                        "number_of_stars_list":number_of_stars_list,
                        "tourist_destination_describe_list":tourist_destination_describe_list,
                        "tourist_destination_location_list":tourist_destination_location_list,
                        "number_of_travel_days_list":number_of_travel_days_list,
                        "hotel_info_list":hotel_info_list
                    }
                }
            } 
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8012, workers=5, reload=True)