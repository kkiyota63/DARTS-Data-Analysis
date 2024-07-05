import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#取得元：https://data.darts.isas.jaxa.jp/pub/selene/sp/

# ファイルパスの設定
file_path_new = 'kaguya_data/SPDATAread181min_SPCread_SP_2C_03_01177_S651_E1896.csv'

# CSVファイルの読み込み
df_new = pd.read_csv(file_path_new)

# 適切な列名を設定
columns = [
    'MOON_SUN_DISTANCE', 'INCIDENCE_ANGLE', 'EMISSION_ANGLE', 'PHASE_ANGLE',
    'SPACECRAFT_AZIMUTH', 'SOLAR_AZIMUTH', 'slope', 'slope_azimuth', 'XL_norm',
    'S_sp_spectrum_ref1'
]
columns += [f'sp_spectrum_ref1_corr_{i}' for i in range(1, 182)]
columns += ['S_sp_spectrum_ref2']
columns += [f'sp_spectrum_ref2_corr_{i}' for i in range(1, 182)]
columns += ['S_sp_spectrum_ref3']
columns += [f'sp_spectrum_ref3_corr_{i}' for i in range(1, 182)]
columns += [f'agreement_ref_{i}' for i in range(1, 4)]
columns += ['recommendation_ref', 'incident_angle_flag', 'Unnamed_560']

df_new.columns = columns

# 必要な列の抽出
columns_of_interest = [
    'MOON_SUN_DISTANCE', 'INCIDENCE_ANGLE', 'EMISSION_ANGLE', 'PHASE_ANGLE',
    'SPACECRAFT_AZIMUTH', 'SOLAR_AZIMUTH', 'slope', 'slope_azimuth', 'XL_norm',
    'sp_spectrum_ref1_corr_1'
]
df_interest = df_new[columns_of_interest]

# 地理座標の変換（仮定としてランダム生成）
lons = np.linspace(185, 190, len(df_interest))  # 経度
lats = np.linspace(-70, -65, len(df_interest))  # 緯度

# マッピング
plt.figure(figsize=(10, 6))
plt.scatter(lons, lats, c=df_interest['sp_spectrum_ref1_corr_1'], cmap='viridis')  # 'sp_spectrum_ref1_corr_1'の値を使用
plt.colorbar(label='Reflectance')
plt.xlabel('Longitude (E)')
plt.ylabel('Latitude (S)')
plt.title('Moon Reflectance Map around South Pole')
plt.savefig('kaguya_data/moon_reflectance_map.png')
plt.show()
