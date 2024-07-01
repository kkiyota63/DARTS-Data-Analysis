import os
import requests
from PIL import Image
import matplotlib.pyplot as plt

# 「きぼう」の船外実験プラットフォームで実施された「たんぽぽ」実験で得られた画像データ
# https://data.darts.isas.jaxa.jp/pub/tanpopo/data/

#取得したいファイル名を指定
tanpopo_file_name = [
    "01_SD1A0104T.bmp",
    "02_SD1A0120T.bmp"
]

#ダウンロード元のURL
tanpopo_base_url = "https://data.darts.isas.jaxa.jp/pub/tanpopo/data/"

#保存先のディレクトリを指定
tanpopo_save_dir = "tanpopo_data"

# 各ファイルをダウンロードして表示する
for file_name in tanpopo_file_name:
    url = tanpopo_base_url + file_name
    response = requests.get(url)

    # ファイルのフルパスを作成
    tanpopo_file_path = os.path.join(tanpopo_save_dir, file_name)

    # file_nameをバイナリ書き込みモードで開いて、response.contentを書き込む
    with open(tanpopo_file_path, "wb") as f:
        f.write(response.content)

    # 保存したファイルを開いて画像を表示する
    img = Image.open(tanpopo_file_path)
    plt.imshow(img)
    plt.axis('off')  # 軸を表示しないようにする
    plt.show()

    
