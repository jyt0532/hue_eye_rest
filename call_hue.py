import requests
from xml.etree import ElementTree
import json
import datetime
import schedule
import time
import sys
def unipoll(building, status):
    job_url = "http://10.73.162.241/api/hndH8nlcjI9VXxCW5trJxbU9K2LaQ3ooi29Qs848/lights/2/state"
    success_color = '{"on":true, "sat":254, "bri":254,"hue":25000, "xy":[0.41, 0.51721]}'
    failure_color = '{"on":true, "sat":254, "bri":254,"hue":10000, "xy":[0.675, 0.322]}'
    pending_color = '{"on":true, "sat":254, "bri":254,"hue":10000, "xy":[0.1691, 0.0441]}'
    if building == 'True':
        job_response = requests.put(job_url, data = pending_color)
        print "building"
        return
    if status == 'FAILURE':
        job_response = requests.put(job_url, data = failure_color)
    elif status == 'SUCCESS':
        job_response = requests.put(job_url, data = success_color)
    print "finished"

if __name__ == "__main__":
        building = sys.stdin.readline().strip()
        status = sys.stdin.readline().strip() 
        unipoll(building, status)
