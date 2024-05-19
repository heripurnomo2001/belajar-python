# MENCETAK TANGGAL DENGAN f-strings

# import module datetime
from datetime import datetime, timedelta

# mengambil data hari ini
future_day = datetime.today() + timedelta(days=60)
# menggunakan f-strings untuk mencetak tanggal

print(f"Future day is : {future_day:%B %d, %Y}")
