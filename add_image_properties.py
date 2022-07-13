import os
import json
from definitions import DATA_PATH
#we must create a folder called 'data' and create a txt called image_properties.txt in the folder of this python file, because you can check with print (DATA_PATH)


# all machine object parameters needed to develop the gcode machine instructions,
# parameter values are specific to the If Then Paint proof-of-concept prototype machine

image_properties = {'name': 'image_properties',
                    'x_width': 120,
                    'y_height': 160,
                    'pixel_per_mm': 6.4,
                    'grid_side_pixel_length': 64}

#print(os.listdir())
print (DATA_PATH)

#file = open(r'C:\Users\yushuo\Desktop\Inlead internship\Draw oil painting with robot\IfThenPaint\IfThenPaint_Image2Gcode-master\IfThenPaint_Image2Gcode')

#os.chdir(r'C:\Users\yushuo\Desktop\Inlead internship\Draw oil painting with robot\IfThenPaint\IfThenPaint_Image2Gcode-master\IfThenPaint_Image2Gcode')

#DataPath="Users\yushuo\Desktop\Inlead internship\Draw oil painting with robot\IfThenPaint\IfThenPaint_Image2Gcode-master\IfThenPaint_Image2Gcode";

with open(os.path.join(DATA_PATH, 'image_properties.txt'), 'w') as f:
#with open(os.path.join(DataPath, "image_properties.txt"), 'w') as f:
     
    json.dump(image_properties, f, separators = (',', ':'), sort_keys = True, indent = 4)
f.close()

