#
# In inkscape saveas jessyInk .zip file to get all the layers
# http://www.imagemagick.org/Usage/anim_basics/
#
# -loop 0 : inf loop

import os
import os.path
import shutil


if os.path.exists("tempa"):
    shutil.rmtree("tempa")

os.makedirs("tempa")

os.chdir("tempa")
os.system("unzip ../boom.zip")
os.chdir("..")
os.system("C:\\Progra~1\\ImageMagick-6.9.0-Q16\\convert.exe  -dispose Background -delay 7 -loop 1 -resize 150x150 tempa\\*.png boom.gif")

shutil.rmtree("tempa")
