from file_broadcaster import broadcast_file,broadcast_config
import time
import datetime
from multiprocessing import Process

def broadcast_all():
    texec = dict()
    configs = broadcast_config()
    catat_awal = datetime.datetime.now()
    for config in configs:
        print(f"broadcasting file data.txt to {config['ip_address']}")
        waktu = time.time()
        texec[config['ip_address']] = Process(target=broadcast_file, args=(config['ip_address'],5005))
        texec[config['ip_address']].start()
    for config in configs:
        texec[config['ip_address']].join()
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    
if __name__=='__main__':
    broadcast_all()