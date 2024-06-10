from ultralytics import YOLO
import argparse
import os
from PIL import Image
import json
parser = argparse.ArgumentParser(description='yolov8')
parser.add_argument('--image', help='image path')
parser.add_argument('--output', help='output jsonfile')

args = parser.parse_args()
source = args.image # change the path of the model config file
output = args.output

pretrain_path = "./yolocheckpoint.pt"
# image_path = "/home/mmlab206/CVPDL/HW1/hw1_dataset/test"
# pretrain_path = "/home/mmlab206/CVPDL/HW1/ultralytics/runs/detect/train_prepth/weights/best.pt"
img = os.listdir(source)

# Load a model
model = YOLO(pretrain_path, task="detect")  # build a new model from scratch
# results = model(image_path)
with open(output,'w') as f:
	results = model.predict(source=source,conf=0.001 ,iou=0.7 ,max_det=300)
	img_json = {}
	for result in results:
		
		img_name = result.path
		img_name = os.path.basename(img_name)
		
		result = result.cuda()
		result = result.cpu()
		result = result.to('cpu')
		result = result.numpy()
		boxes = result.boxes
		# print(boxes.orig_shape)
		# print(type(boxes.xywhn))
		new_pred_boxes=[]
		for box in boxes.xyxy:
			new_pred_boxes.append(box.tolist())
			# print(list(box))
		cls = boxes.cls.tolist()
		# print(cls)
		conf = boxes.conf.tolist()
		# print(conf)
		
		pred_dict = {
			'boxes': new_pred_boxes,
			'labels': [int(l) for l in cls],
			'scores' : [s for s in conf]
		}
		img_json[img_name] = pred_dict
	
	json.dump(img_json, f)
