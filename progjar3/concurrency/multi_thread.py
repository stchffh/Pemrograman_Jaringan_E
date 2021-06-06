from file_broadcaster import broadcast_file,broadcast_config
import datetime
import threading

def broadcast_all():
    texec = dict()
    configs = broadcast_config()

    catat_awal = datetime.datetime.now()

    for config in configs:
        print(f"broadcasting file data.txt to {config['ip_address']}")
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multithread
        texec[config['ip_address']] = threading.Thread(target=broadcast_file, args=(config['ip_address'],5005))
        texec[config['ip_address']].start()

    #setelah menyelesaikan tugasnya, dikembalikan ke main thread dengan join
    for config in configs:
        texec[config['ip_address']].join()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")


#fungsi download_gambar akan dijalankan secara multithreading

if __name__=='__main__':
    broadcast_all()