import requests
import openai
import json
import os
from PIL import Image
import climage

openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "if-davinci-v2"

image_dir_name = "openai-images"
image_dir = os.path.join(os.curdir, image_dir_name)

if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

#print(f"{image_dir=}")
print("--------------------------------------------------")
print("# Hello! My name is if-davinci-v2, and i make art!")
print("--------------------------------------------------")
print("# I can create images based on your input.")
print("# I can also create variations of images.")
print("--------------------------------------------------")
while True:    
    prompt = str(input("# Enter what you would like me to create: "))
    print("--------------------------------------------------")
    n = int(input("# How many images would you like to see?(1-10): "))
    print("--------------------------------------------------")
    print("# Generating images...")
    print("--------------------------------------------------")
    print("")
    print("--------------------------------------------------")
    generation_response = openai.Image.create(
        prompt=prompt,
        n=n,
        size="1024x1024",
        response_format="url",
    )

    #print(generation_response)

    generated_image_name = "generated_image.png"
    generated_image_filepath = os.path.join(image_dir, generated_image_name)
    generated_image_url = generation_response["data"][0]["url"]
    generated_image = requests.get(generated_image_url).content

    with open(generated_image_filepath, "wb") as image_file:
        image_file.write(generated_image)

    print(f"# Image saved to {generated_image_filepath}")
    print("")
    print("# Image:")
    print("")
    print("--------------------------------------------------")
    print("")
    display = Image.open(generated_image_filepath)
    display.show()

    print("--------------------------------------------------------------")
    print("# Would you like to generate further variaitons of this image?")
    print("--------------------------------------------------------------")
    print("#  1. Yes")
    print("#  2. No")
    print("#  3. Exit")
    choice = int(input("#  Enter your choice: "))
    print("--------------------------------------------------------------")
    print("")
    if choice == 1:
        variation_response = openai.Image.create_variation(
                image=generated_image,
                n=2,
                size="1024x1024",
                response_format="url",
            )
        print("# Generating variations...")
        print("--------------------------------------------------")
        #print(variation_response)
        print("")

        variation_urls = [datum["url"] for datum in variation_response["data"]]
        variation_images = [requests.get(url).content for url in variation_urls]
        variation_image_names = [f"variation_image_{i}.png" for i in range(len(variation_images))]
        variation_image_filepaths = [os.path.join(image_dir, name) for name in variation_image_names]
        for image, filepath in zip(variation_images, variation_image_filepaths):
            with open(filepath, "wb") as image_file:
                image_file.write(image)
        print("# Variations saved to {variation_image_filepaths}")
        print("--------------------------------------------------")
        print("")
        print("# Original image:")
        print("")
        original = Image.open(generated_image_filepath)
        original.show()
        print("# Variations:")
        print("")
        for variation_image_filepaths in variation_image_filepaths:
            print(variation_image_filepaths)
            display(Image.open(variation_image_filepaths))
            print("")
            continue

    elif choice == 2:
        break

    elif choice == 3:
        print("")
        print("# Goodbye!")
        exit()
    else:
        print("Invalid choice")
        break

    print("-----------------------------------------------")
    print("# Generate new image?")
    print("")
    print("# 1. Yes")
    print("# 2. No")
    again = int(input("# Enter your choice: "))
    print("-----------------------------------------------")
    print("")
    if again == 1:
        continue
    elif again == 2:
        break
    else:
        print("Invalid choice")
        continue
print("----------")
print("# Goodbye!")
print("----------")
exit()

