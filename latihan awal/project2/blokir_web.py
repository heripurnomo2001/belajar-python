""" Program python untuk memblokir website
    --------------------------------------
"""
import time
from datetime import datetime as dt

#r adalah raw untuk string
hosts_path = r"C://Windows//System32//drivers//etc"
hosts_temp = "hosts"
redirect = "127.0.0.1"

#user dapat memilih website yang akan diblok
website_list = ["www.astaga.com","twitter.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month, dt.now().day,22):
        print("Waktu kerja bos")
        with open(hosts_path,"r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Fun time")
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0) #reset pointer ke bagian atas file text
            for line in content:
                # overwrite seluruh file
                    if not any(website in line for website in website_list):
                        file.write(line)

            file.truncate() # Baris ini digunakan untuk menghapus baris (termasuk DNS)
    time.sleep(5)



                                   
                               


