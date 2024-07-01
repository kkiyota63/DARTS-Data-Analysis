import os
import requests
from PIL import Image
import matplotlib.pyplot as plt


# ハヤブサのAMICAで撮影されたイトカワの画像データ
#https://data.darts.isas.jaxa.jp/pub/hayabusa/amica/20051016/

hyb_file_name = [
    "ST_2465140661_v.jpg",
    "ST_2465255855_v.jpg",
    "ST_2465735909_v.jpg"
]

# ダウンロード元のURL
hyb_base_url = "https://data.darts.isas.jaxa.jp/pub/hayabusa/amica/20051016/"

# 保存先のディレクトリを指定
hyb_save_dir = "itokawa_data"

# 各ファイルをダウンロードして表示する
for file_name in hyb_file_name:
    url = hyb_base_url + file_name
    response = requests.get(url)

    # ファイルのフルパスを作成
    hyb_file_path = os.path.join(hyb_save_dir, file_name)

    # file_nameをバイナリ書き込みモードで開いて、response.contentを書き込む
    with open(hyb_file_path, "wb") as f:
        f.write(response.content)
    
    image = Image.open(hyb_file_path)
    plt.imshow(image)
    plt.axis('off')
    plt.show()