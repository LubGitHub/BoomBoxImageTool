Instructions:

In commandline, type cd to change destination to the folder you put the script.

Make sure that the image is 105x105 pixels in area, else it will not work.

In commandline, type "Boxtool.py" followed by either "-c", "-hi", "-f"

"-c" creates a cutout for each black pixel in the image and exports it as a mcfunction.

"-f" creates a pillar of bedrock for each black pixel in the image and exports it as a mcfunction.

"-hi" creates a heightmap batch clone which encodes heigh based on its darkness in the image and exports it as a mcfunction. Darker means farther down, lighter means higher.

You can also use multiple options at once to create a cutout, heightmap, and template out of one image.

Requires Pillow and atleast Python 3.
