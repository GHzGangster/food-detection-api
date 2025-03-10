import os

from ultralytics import YOLO

root_path = os.path.dirname(os.path.abspath(__file__))
input_dir_path = os.path.join(root_path, "input")
output_dir_path = os.path.join(root_path, "output")

def predict(input_path, output_path):
    model_path = os.path.join(root_path, "model.pt")
    model = YOLO(model_path)

    results = model.predict(input_path, device="cpu")
    if len(results) == 0:
        return False

    results[0].save(filename=output_path)
    return True
