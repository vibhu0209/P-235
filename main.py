import requests
# 91 data sets are found
for i in range(1,101):
    URL = f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}"
    r = requests.get(url=URL)
    if r.status_code == 200:
        print(URL)
    else:
        print("404\nNot Found")
