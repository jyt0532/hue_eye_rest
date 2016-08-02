import requests
from xml.etree import ElementTree
import json
import datetime
import schedule
import time
import sys
def call_hue(action):
    job_url = "http://10.73.162.241/api/hndH8nlcjI9VXxCW5trJxbU9K2LaQ3ooi29Qs848/lights/2/state"
    green_color = '{"on":true, "sat":254, "bri":254,"hue":25000, "xy":[0.41, 0.51721]}'
    red_color = '{"on":true, "sat":254, "bri":254,"hue":10000, "xy":[0.675, 0.322]}'
    blue_color = '{"on":true, "sat":254, "bri":254,"hue":10000, "xy":[0.1691, 0.0441]}'
    if action == 'on':
        job_response = requests.put(job_url, data = red_color)
    else:
        job_response = requests.put(job_url, data = green_color)

if __name__ == "__main__":
        call_hue("on")
