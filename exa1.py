import requests

url = 'https://xgtrial.herokuapp.com/trial/xgorgon'

data = {'url':'https://api16-normal-c-alisg.tiktokv.com/aweme/v1/discover/search/?os_api=23&device_type=SM-J700F&ssmix=a&manifest_version_code=170503&dpi=320&uoo=0&carrier_region=KE&region=US&carrier_region_v2=639&app_name=musically_go&version_name=17.5.3&timezone_offset=10800&ts=1609425115&ab_version=17.5.3&residence=KE&cpu_support64=false&current_region=KE&ac2=wifi&app_type=normal&ac=wifi&host_abi=armeabi-v7a&update_version_code=170503&channel=googleplay&_rticket=1609425114755&device_platform=android&iid=6912314043555612421&build_number=17.5.3&locale=en&op_region=KE&version_code=170503&timezone_name=Africa%2FNairobi&cdid=5286261c-2e3e-491c-8a8a-33c2d1c66bf7&openudid=5cb332e130e0b5d1&sys_region=US&device_id=6498732577740817925&app_language=en&resolution=720*1280&os_version=6.0.1&language=en&device_brand=samsung&aid=1340'}

r = requests.post(url, data=data)

print(r.json())