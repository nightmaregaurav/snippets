import os
import img2pdf

# Specify the folder path where your images are located
main_path = ""
volumes = [f for f in os.listdir(main_path) if os.path.isdir(os.path.join(main_path, f))]

for volume in volumes:
    folder_path = os.path.join(main_path, volume)
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]
    image_files.sort()
    image_paths = []

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image_paths.append(image_path)

    output_pdf_path = os.path.join(main_path, f"{volume}.pdf")
    with open(output_pdf_path, "wb") as f:
        f.write(img2pdf.convert(image_paths))
