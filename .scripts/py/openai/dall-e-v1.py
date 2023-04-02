
import os
import openai
import json
import time
from yaspin import yaspin
from PIL import Image
from rich.prompt import Prompt
from rich.prompt import IntPrompt
from rich.prompt import Confirm
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich import print
import requests
#import climage

cont = True
# set API key
openai.api_key = os.environ.get("OPENAI_API_KEY")
model_engine = "if-davinci-v2"
# set dir to save generated images
image_dir_name = "openai-images"
image_dir = os.path.join(os.curdir, image_dir_name)
# Create dir if it doesn't exist
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

console = Console(width=80)
console.print("# ")
console.print("#     Hello! My name is [bold red]if-davinci-v2[/], and i make art!")
console.print("#     I can generate images based on your prompt.")
console.print("# ")
# main loop
while cont == True:
    while True:
        console.print("     What do you want to generate?", style="bold red")
        # Prompt for a string to generate an image
        prompt = Prompt.ask("     [prompt]>> ")
        if len(prompt) > 0:
            break
        console.print("[prompt.invalid]#     Please enter a prompt.", style="bold red")
        console.print("# ")
    while True:
        n = IntPrompt.ask("#     How many images do you want to generate?(1-10)", default=1)
        if n >= 1 and n <= 10:
            break
        console.print("[prompt.invalid]#     Please enter a number between 1 and 10")
        console.print("# ")
    size = Prompt.ask("#     What size do you want the image to be?", 
    choices=["256x256", "512x512", "1024x1024"], default="1024x1024")
    console.print("#--------------------------------------------------")
    #print(f"{image_dir=}")
    with yaspin(text=" Generating image...", color="magenta", spinner="dots") as spinner:
        generation_response = openai.Image.create(
            prompt=prompt,
            n=n,
            size=size,
            response_format="url",
        )
    console.print("# ")
    console.print(generation_response)
    generated_image_name = "generated_image.png"
    generated_image_filepath = os.path.join(image_dir, generated_image_name)
    generated_image_url = generation_response["data"][0]["url"]
    generated_image = requests.get(generated_image_url).content
    with open(generated_image_filepath, "wb") as image_file:
        image_file.write(generated_image)
        console.print(f"#     Images saved to {generated_image_filepath}")
        console.print("# ")
        display = Image.open(generated_image_filepath)
        display.show()
    cont = Confirm.ask("#     Do you want to generate another image?", default=True)
    console.print("# ")
console.print("[bold red]#     Goodbye![/]")
