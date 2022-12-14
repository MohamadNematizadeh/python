import imageio
import os
# محتوای یک لیست میتواند نمایش دهد
# 
# result=os.listdir("session2")
# print(result)
# ساخت یک گیفت
file_list = sorted(os.listdir("gft/img"))
IMAGES = []
for file_name in file_list:
    file_path = "gft/img/"+file_name
    image= imageio.imread(file_path)
    IMAGES.append(image)
imageio.mimsave("my_gft.gif", IMAGES)    