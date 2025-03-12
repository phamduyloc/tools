import time
import json
import requests
from itertools import cycle
import sys
from termcolor import colored, cprint


# Danh sách API Keys
API_KEYS = [
    "53111d0b869d21bfac28d143578261dc0cd93b4bd8549ebb4299b3c1f5e952a6", 
    "e8be98ed28bd4c45cb98d0156d756cf4b50406866a53b86d484e6177be9590c8", 
    "37c3d4c50a12832727216a9ef639cdbb50a6d2b0c04cc378a91d821bb1320f8d", 
    "15ff51093064d0ec723adcdf41bc5455b332c896044e25552418cd0123f39de9", 
    "6595c849d129dd8451a7a1602c3bb29ac10dce24765639b3b489fd3d67080c82", 
    "f02c4ec317b99705cd167ff7e1366b5c4f9d6d4b27362c1ebd8354cb40b78ef2"
]

API_USAGE = {key: {"daily": 0, "minute": 0} for key in API_KEYS}
API_LIMITS = {"daily": 500, "minute": 4}
API_ROTATION = cycle(API_KEYS)



def get_available_api_key():
    """Chọn API key khả dụng theo giới hạn sử dụng"""
    for _ in range(len(API_KEYS)):
        api_key = next(API_ROTATION)
        if API_USAGE[api_key]["daily"] < API_LIMITS["daily"] and API_USAGE[api_key]["minute"] < API_LIMITS["minute"]:
            return api_key
    return None


def reset_minute_usage():
    """Đặt lại giới hạn phút sau mỗi phút"""
    while True:
        time.sleep(60)
        for key in API_KEYS:
            API_USAGE[key]["minute"] = 0


def query_virustotal(api_key, domain):
    VT_URL = "https://www.virustotal.com/vtapi/v2/domain/report?apikey=" + api_key + "&domain=" + domain
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(VT_URL, stream=True)
    if response.status_code == 200:
        API_USAGE[api_key]["daily"] += 1
        API_USAGE[api_key]["minute"] += 1
        return response.json()
    return None


def process_domains(input_file, output_file):
    with open(input_file, "r") as file:
        domains = [line.strip() for line in file.readlines()]
    
    results = []
    for domain in domains:
        api_key = get_available_api_key()
        if not api_key:
            print(colored("Hết API key khả dụng, dừng kiểm tra!",'red'))
            break
        
        print(colored(f"Đang kiểm tra: {domain} với API Key: {api_key}",'blue'))
        data = query_virustotal(api_key, domain)
        #print(data)

        undetected_urls = data.get("undetected_urls", [])
        if undetected_urls:
            result = ""
            for url_data in undetected_urls:
                result += f"{url_data[0]}\n"
            print(result)
            with open(output_file, "a") as f:
                f.write(result + "\n")
        else:
            result = f"Không có undetected_urls cho {domain}.\n"
            print(colored(result,'red'))
        time.sleep(15)  # Để tránh vượt giới hạn API

    
if __name__ == "__main__":
    import threading
    threading.Thread(target=reset_minute_usage, daemon=True).start()
    file_path = input("Nhập đường dẫn tập tin chứa danh sách domain: ")
    output_file = input("Nhập đường dẫn tập tin kết quả: ")
    process_domains(file_path, output_file)

    print(colored("All Done!",'yellow'))
