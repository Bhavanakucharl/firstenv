import os
from PIL import Image

def generate_images_in_folder(folder_path):
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is an image
        if os.path.isfile(file_path) and is_image_file(file_path):
            yield Image.open(file_path)

def is_image_file(file_path):
    try:
        Image.open(file_path)
        return True
    except (IOError, SyntaxError):
        return False

# Specify the folder path
folder_path = "C:\\Users\\bhava\\OneDrive\\Desktop\\insta"

# Call the generator function to yield images in the folder
image_generator = generate_images_in_folder(folder_path)

print(type(image_generator))


image_generator.__next__().show()

# for i, image in enumerate(image_generator, start=1): 
#     next(image.show())
#     i+=1; 
#     next(image.show())
#     i+=1; 
#     next(image.show())

    



# # Iterate over the generator and perform operations on the images
# for i, image in enumerate(image_generator, start=1):
#     # Do something with the image
#     image.show()
#     # Or save the image to a file

#     # image.save(f"image_{i}.png")

