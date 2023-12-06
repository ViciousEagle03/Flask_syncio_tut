import requests
import time

def response_get():
    before_req = time.time()
    response = requests.get(url = "http://127.0.0.1:5000/gen_num")
    after_req = time.time()
    latency = after_req - before_req
    return (response.json(),latency)
    
def main():
    '''
    req made in 2 mins
    '''
    data1=[]
    average_latency=0
    latency_list=[]
    start_time = time.time()
    req_count=0
    while True:
    
        data,latency = response_get()
        latency_list.append(latency)
        data1.append(data)
        req_count+=1
        current_time = time.time()
        if current_time - start_time >=20:
            break
    average_latency = sum(latency_list)/len(latency_list)
    print(f"Total number of requests handled:{req_count}")
    print(f"Average request latency:{average_latency}")

main()
