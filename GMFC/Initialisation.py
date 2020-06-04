import os
import platform

print(platform.uname())

operating_system = platform.uname()[0]
os_version = platform.uname()[1]

GMFC_folder = os.path.dirname(__file__)
images_folder = os.path.join(GMFC_folder, "Project Resources", "Images")

if os.path.exists(os.path.join(images_folder, "Background.png")):
    print("{} does exist!".format(os.path.join(images_folder, "Background.png")))

