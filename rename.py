import os

for i,f in enumerate(os.listdir("Photos")):
    os.rename(f"Photos/{f}",f"Photos/{i}.jpg")