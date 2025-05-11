import json

# Load the canvas file
with open("Data Structures & Algorithms.canvas", "r", encoding="utf-8") as file:
    canvas = json.load(file)

# Update file paths
for node in canvas.get("nodes", []):
    if node.get("type") == "file" and isinstance(node.get("file"), str):
        node["file"] = node["file"].replace("Curtin 2/DSA", "DSA_Shared")

# Save the updated canvas file
with open("Data Structures & Algorithms.canvas", "w", encoding="utf-8") as file:
    json.dump(canvas, file, indent=4)

print("All 'Curtin 2/DSA' paths have been updated to 'DSA_Shared'.")
