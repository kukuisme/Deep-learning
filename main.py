import json
import numpy as np
import os
import matplotlib.pyplot as plt

#509170748 bob
# 設定JSON檔案路徑的格式
input_file_path_format = 'input/input{}.json'
output_directory = 'output'

"""
# 確保output資料夾存在
os.makedirs(output_directory, exist_ok=True)
"""

# 讀取並處理 input1.json 到 input10.json
for i in range(1, 11):
    input_file_path = input_file_path_format.format(i)
    
    # 讀取 JSON 檔案
    with open(input_file_path, 'r') as file:
        json_data = json.load(file)
    
    # 將矩陣存儲在一個列表中
    matrices = [np.array(data["matrix"]) for data in json_data]
    
    # 準備紀錄左上角與右下角的數值
    top_left_values = []
    bottom_right_values = []
    
    # 行矩陣相乘
    if len(matrices) > 1:
        result = matrices[0]  # 初始化結果為第一個矩陣
        top_left_values.append(result[0, 0])  # 記錄最左上角值
        bottom_right_values.append(result[-1, -1])  # 記錄最右下角值
        
        for j in range(1, len(matrices)):
            if result.shape[1] == matrices[j].shape[0]:  # 檢查矩陣乘法條件
                result = np.matmul(result, matrices[j])  # 矩陣相乘
                result = result % 100000  # 題目要求%100000
                
                # 紀錄當前矩陣乘積的最左上角與最右下角的值
                top_left_values.append(result[0, 0])
                bottom_right_values.append(result[-1, -1])
        
        # 將結果寫入對應的 output 檔案
        output_file_path = os.path.join(output_directory, f'output{i}.json')
        with open(output_file_path, 'w') as output_file:
            json.dump({"result": result.tolist()}, output_file)
        
        print(f"Result saved to {output_file_path}.")
        
        #繪製圖表
        plt.plot(range(1, len(top_left_values) + 1), top_left_values, label='Top Left', color='blue')
        plt.plot(range(1, len(bottom_right_values) + 1), bottom_right_values, label='Bottom Right', color='red')
        
        #添加標籤與標題,懶得插入中文插件
        plt.xlabel('Matrix Multiplication Step')
        plt.ylabel('Value')
        plt.title(f'Matrix Top Left and Bottom Right Values - File input{i}.json')
        plt.legend()
        
        # 保存圖片
        output_image_path = os.path.join(output_directory, f'output{i}.png')
        plt.savefig(output_image_path)
        plt.clf()  # 清空圖片
        
















