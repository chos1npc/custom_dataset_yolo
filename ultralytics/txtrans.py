import json
import argparse
import os

parser = argparse.ArgumentParser(description='transfer file')
parser.add_argument('--json_file', help='json file path')
args = parser.parse_args()
source = args.json_file
# 讀取 JSON 檔案
with open(source, 'r') as f:
    data = json.load(f)


# 定義yolo格式的標注資訊存放路徑
output_path = "./dateset_yolo/val"

# 確認存放路徑是否存在，如果不存在則建立資料夾
if not os.path.exists(output_path):
    os.makedirs(output_path)

# 定義類別名稱對應的編號，需要與json檔案中的id對應
class_id_map = {
    "creatures": 0,
    "fish": 1,
    "jellyfish": 2,
    "penguin": 3,
    "puffin": 4,
    "shark": 5,
    "starfish": 6,
    "stingray": 7,
}

# 逐一處理每張圖片
for image in data["images"]:
    # 取得圖片名稱
    image_name = image["file_name"]
    # 取得圖片的寬度和高度
    image_width = image["width"]
    image_height = image["height"]

    # 打開對應的txt檔案，如果檔案不存在則建立檔案
    output_file = open(os.path.join(output_path, os.path.splitext(image_name)[0] + ".txt"), "w+")

    # 尋找所有跟這張圖片有關聯的annotation
    for annotation in data["annotations"]:
        if annotation["image_id"] == image["id"]:
            # 取得這個annotation對應的類別編號和bbox
            
            class_id = annotation["category_id"]
            bbox = annotation["bbox"]
            # 計算bbox的中心點座標和寬度、高度
            bbox_x = bbox[0] + bbox[2] / 2
            bbox_y = bbox[1] + bbox[3] / 2
            bbox_w = bbox[2]
            bbox_h = bbox[3]

            # 將bbox座標、寬度和高度轉換為yolo格式
            yolo_x = bbox_x / image_width
            yolo_y = bbox_y / image_height
            yolo_w = bbox_w / image_width
            yolo_h = bbox_h / image_height

            # 將資訊寫入txt檔案
            output_file.write(f"{class_id} {yolo_x:.6f} {yolo_y:.6f} {yolo_w:.6f} {yolo_h:.6f}\n")

    # 關閉txt檔案
    output_file.close()
