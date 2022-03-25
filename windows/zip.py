import os, zipfile


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(
                os.path.join(root, file),
                os.path.relpath(os.path.join(root, file), os.path.join(path, "..")),
            )

path = "place you want to zip"
with zipfile.ZipFile("path.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
    zipdir(path, zipf)  # Zip all of the things