import datetime as dt

print("==== Welcome to Time Reminder ====")
print(f"Masukkan Tanggal Acara Anda ")

year = 2024
month = 10
date = int(input("Tanggal : "))
hour = int(input("Jam berapa :"))
minute = int(input("Menit berapa : "))

tgl_acara = dt.date(year,month,date)
print("=".center(51, "="))
print(f"Jadwal Acara anda yaitu :{tgl_acara} ({tgl_acara:%A})")
print("=".center(51, "="))

today = dt.date.today()
print(f"Sekarang tanggal : {today}")
print("=".center(51, "="))
selisih = tgl_acara - today
print(f"Acara anda tinggal {selisih} hari lagi!")


print("=".center(51, "="))
day_acara = tgl_acara.strftime("%A")

if day_acara == "Sunday":
    print(f"Acara anda Berada di hari Libur")
else:
    print(f"Acara anda berada di hari kerja")

print("=".center(51, "="))
acara = dt.datetime(year,month,date,hour,minute)
pengingat = acara - dt.timedelta(minutes=15)
print(f"Waktu pengingat: {pengingat.strftime('%Y-%m-%d %H:%M:%S')}")