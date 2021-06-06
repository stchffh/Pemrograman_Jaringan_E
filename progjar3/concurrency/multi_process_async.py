from file_broadcaster import broadcast_file,broadcast_config
import time
import datetime
from multiprocessing import Process, Pool

def broadcast_all():
    texec = dict()
    configs = broadcast_config()
    status_task = dict()
    task_pool = Pool(processes=20)
    catat_awal = datetime.datetime.now()
    for config in configs:
        print(f"broadcasting file data.txt to {config['ip_address']}")
        texec[config['ip_address']] = task_pool.apply_async(func=broadcast_file, args=(config['ip_address'],5005))
    for config in configs:
        status_task[config['ip_address']]=texec[config['ip_address']].get(timeout=10)

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("status TASK")
    print(status_task)

if __name__=='__main__':
    broadcast_all()