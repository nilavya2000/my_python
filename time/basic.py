import time
import os
import pandas
while True:
    if os.path.exists("temps_today.csv"):
        data=pandas.read_csv("temps_today.csv")
        print(data.mean())
    else:
        print("file doesn't exist.")
    time.sleep(10)
