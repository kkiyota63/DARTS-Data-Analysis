import requests
from astropy.io import fits
from io import BytesIO
import matplotlib.pyplot as plt

# ダウンロードするFITSファイル名
fits_file_names = [
    #"hyb2_nirs3_20180710_cal.fit",
    "hyb2_nirs3_20180710_raw.fit"
]

# ベースURL
fits_base_url = "https://data.darts.isas.jaxa.jp/pub/hayabusa2/nirs3_bundle/data/Ryugu/"

# 各ファイルをダウンロードしてFITSファイルとして表示
for file_name in fits_file_names:
    url = f"{fits_base_url}{file_name}"
    response = requests.get(url)
    if response.status_code == 200:
        byte_data = BytesIO(response.content)
        hdulist = fits.open(byte_data)
        
        # FITSファイルの情報を表示
        hdulist.info()
        
        # データ部分を取得（例として最初のハードユニット）
        data = hdulist[0].data
        
        # データのサマリを表示
        print(data)
        
        # データの2Dイメージをプロット
        plt.imshow(data, cmap='gray')
        plt.colorbar()
        plt.title(f"FITS data from {file_name}")

        plt.savefig(f"hyb2_data/{file_name}.png")
        plt.show()
        
        # FITSファイルを閉じる
        hdulist.close()
    else:
        print(f"Failed to download {file_name} with status code {response.status_code}")
