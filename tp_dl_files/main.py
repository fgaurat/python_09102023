import requests
import os
import threading
import time
import concurrent.futures
def download_and_write(url):
    response = requests.get(url,timeout=5)
    file_name = url.split("/")[-1]
    # print(file_name)
    with open(f"./tmp/{file_name}","w") as f:
        print(response.text,file=f,end="")
        # f.write(response.text)


def main():
    start = time.perf_counter()
    root = "http://logs.eolem.com/"
    os.makedirs('tmp',exist_ok=True)
    urls = []
    for i in range(1,11):
        url = f"{root}apache_logs_{i:02d}.log"
        urls.append(url)

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_and_write,urls)

    end = time.perf_counter()
    
    print(end-start)

def main_thread():
    start = time.perf_counter_ns()
    root = "http://logs.eolem.com/"
    os.makedirs('tmp',exist_ok=True)
    urls = []
    for i in range(1,11):
        url = f"{root}apache_logs_{i:02d}.log"
        urls.append(url)

    threads =[]
    for url in urls:
        # download_and_write(url)
        th = threading.Thread(target=download_and_write,args=[url])
        threads.append(th)
        th.start()
    
    for th in threads:
        th.join()

    end = time.perf_counter_ns()
    
    print(end-start)

if __name__=='__main__':
    main()
