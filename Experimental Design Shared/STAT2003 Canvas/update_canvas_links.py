import json

canvas_file = "Experimental Design.canvas"  # change if needed

with open(canvas_file, "r", encoding="utf-8") as file:
    canvas = json.load(file)

for node in canvas.get("nodes", []):
    if node.get("type") == "file" and isinstance(node.get("file"), str):
        node["file"] = node["file"].replace("Experimental Design Shared", "Experimental Design Shared/")

with open(canvas_file, "w", encoding="utf-8") as file:
    json.dump(canvas, file, indent=4)

print("Canvas paths updated successfully.")