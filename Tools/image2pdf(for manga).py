import os
import img2pdf

# Specify the folder path where your images are located
main_path = "/home/nightmare/Downloads/DemonSlayer"
volumes = ["v01", "v02", "v03", "v04", "v05", "v06", "v07", "v08", "v09", "v10", "v11", "v12", "v13", "v14", "v15", "v16", "v17", "v18", "v19", "v20", "v21", "v22", "v23"]

for volume in volumes:
    folder_path = os.path.join(main_path, volume)
    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]

    # Sort the image files in alphabetical order
    image_files.sort()

    # Create a list to hold the image paths
    image_paths = []

    # Convert each image file to a PDF
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image_paths.append(image_path)

    # Specify the output PDF file path
    output_pdf_path = volume + ".pdf"

    # Convert the images to PDF using img2pdf library
    with open(output_pdf_path, "wb") as f:
        f.write(img2pdf.convert(image_paths))
