import os
import requests
import matplotlib.pyplot as plt
import pandas as pd

#はやぶさ2の軌道データ
#https://data.darts.isas.jaxa.jp/pub/hayabusa2/nirs3_bundle/data/Ryugu/

#取得したいファイル名を指定
hyb2 = [
    "hyb2_nirs3_20180710_geo.csv",
    #"hyb2_nirs3_20180711_geo.csv"
]

#ダウンロード元のURL
hy2_base_url = "https://data.darts.isas.jaxa.jp/pub/hayabusa2/nirs3_bundle/data/Ryugu/"

#保存先のディレクトリを指定
hy2_save_dir = "hyb2_data"

# 各ファイルをダウンロードして表示する
for file_name in hyb2:
    url = hy2_base_url + file_name
    response = requests.get(url)

    # ファイルのフルパスを作成
    hyb2_file_path = os.path.join(hy2_save_dir, file_name)

    # file_nameをバイナリ書き込みモードで開いて、response.contentを書き込む
    with open(hyb2_file_path, "wb") as f:
        f.write(response.content)
    
    # 保存したファイルを開いて表示する
    df = pd.read_csv(hyb2_file_path)
    print(df)

    # 'UTC_START'を文字列として変換
    df['UTC_START'] = df['UTC_START'].astype(str)

    # x軸のラベルを間引いて表示
    num_labels = len(df['UTC_START'])
    step = max(1, num_labels // 10)  # ラベルの数が多すぎないようにステップを調整
    plt.xticks(ticks=range(0, num_labels, step), labels=df['UTC_START'][::step], rotation=45)

    plt.plot(df["UTC_START"], df["TARGET-S/C_RANGE[km]"])
    plt.title('Distance between Ryuguu and Hayabusa2')
    plt.xlabel('UTC Start Time')
    plt.ylabel('Target-S/C Range (km)')

    #表示したグラフを保存
    plt.savefig('hyb2_data/hyb2_nirs3_20180710_geo.png')

    plt.show()

    