import onnx

model = onnx.load("new_plate_detect_merged/best_nms.onnx")

for node in model.graph.node:
    if node.op_type == "NonZero":
        print("❌ Found NonZero:", node.name)