import requests
import random
from base_code.security_info import api_key
from base_code.base import cover_kelvin_to_c,convert_time_to_period

api_key = api_key["openweather"]  # Thay YOUR_API_KEY bằng API key bạn đã lấy từ OpenWeather
city = "hanoi"  # Thay Hanoi bằng tên thành phố bạn muốn lấy thông tin thời tiết

# vd 24°28′B 54°22′Đ thì bắc nam là vĩ độ , đông tây là kinh độ
# lat = 33.12 # vĩ độ 
# lon = 103.54# kinh độ
# -12.2 -77.2


# lat = -12.2
# lon = -77.2
# lang = "vi"



# Gửi yêu cầu GET đến API OpenWeather để lấy thông tin dự báo thời tiết
# response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}")


def get_all_data_weather(lat,lon,lang):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&lang={lang}")

    # Kiểm tra mã trạng thái của yêu cầu
    if response.status_code == 200:
        # Yêu cầu thành công, lấy thông tin dự báo thời tiết từ phản hồi
        forecast_data = response.json()
        # print(type(forecast_data))
        return forecast_data
        
        # Xử lý thông tin dự báo thời tiết ở đây
        # Ví dụ:
        # for forecast in forecast_data['list']:
        #     date = forecast['dt_txt']
        #     temperature = forecast['main']['temp']
        #     humidity = forecast['main']['humidity']
        #     print(f"Date: {date}")
        #     print(f"Temperature: {temperature} K")
        #     print(f"Humidity: {humidity}%")
        #     print('---')
    else:
        # Yêu cầu không thành công, in ra lỗi
        print("Failed to retrieve weather forecast data.")

# get_all_data_weather(lang="vi",lat=35.04,lon= 109.05)

def get_random_elements2():
    result = []
    for i in range(5):
        start2 = i * 8
        end2 = start2 + 7
        element2 = random.randint(start2,end2)
        # start = random.randint(0, 4) * 8
        # end = start + 7
        # element = random.randint(start, end)
        result.append(element2)
    return result

def select_data_of_weather_data(weather_data_dict):
    main = weather_data_dict["main"]
    weather = weather_data_dict["weather"]
    visibility = weather_data_dict["visibility"]
    pop = round(weather_data_dict["pop"]*100,1)
    dt_txt = convert_time_to_period(time_str=weather_data_dict["dt_txt"])
    dt_day_txt = dt_txt[:10]

    temp = round(cover_kelvin_to_c(kelvin=main["temp"]),1)
    feels_like = round(cover_kelvin_to_c(kelvin=main["feels_like"]),1)
    humidity = main["humidity"]

    weather_main = weather[0]["main"]
    description = weather[0]["description"]
    
    icon = f"https://openweathermap.org/img/wn/{weather[0]['icon']}@2x.png"

    data = {
        "temp":temp,
        "feels_like":feels_like,
        "humidity":humidity,
        "weather_main":weather_main,
        "description":description,
        "icon":icon,
        "visibility":visibility,
        "pop":pop,
        "dt_txt":dt_txt,
        "dt_day_txt":dt_day_txt
    }
    # print(feels_like)
    return data

def get_5_datas_from_5_day_weather(lat,lon,lang):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&lang={lang}")

    # Kiểm tra mã trạng thái của yêu cầu
    if response.status_code == 200:
        # Yêu cầu thành công, lấy thông tin dự báo thời tiết từ phản hồi
        forecast_data = response.json()
        # print(forecast_data)
        # print(type(forecast_data))
        forecast_data_list = forecast_data["list"]
        results = get_random_elements2() 
        datas = []
        for i in results:
            data = forecast_data_list[i]
            data_selectd = select_data_of_weather_data(weather_data_dict=data)
            datas.append(data_selectd)
        return datas
    else:
        # Yêu cầu không thành công, in ra lỗi
        print("Failed to retrieve weather forecast data.")



# a = get_5_datas_from_5_day_weather(lang="vi",lat=45.53,lon= 8.31)
# # print(a)
# for i in a :
#     print(i)

# data4 = {'dt': 1696917600, 'main': {'temp': 292.39, 'feels_like': 291.39, 'temp_min': 292.39, 'temp_max': 292.39, 'pressure': 1022, 'sea_level': 1022, 'grnd_level': 928, 'humidity': 39, 'temp_kf': 0}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'mây rải rác', 'icon': '03d'}], 'clouds': {'all': 50}, 'wind': {'speed': 3.47, 'deg': 109, 'gust': 3.71}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2023-10-10 06:00:00'}

# b = select_data_of_weather_data(data4)
# print(b)