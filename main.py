# import os

# txtDir = "./data"  # specify the path to the directory
# imgDir = "./images"

# for file in os.listdir(txtDir):

#     path = os.path.join(txtDir, file)  # construct the full file path

#     with open(path, "r") as f:
#         contents = f.read()    
#         print(f)
#         print(contents.split())  # do something with the contents (in this case, just print them)
    

#############

# coords = [2753.0, 2385.0, 2888.0, 2385.0, 2888.0, 2502.0, 2753.0, 2502.0]

# x_coords = coords[::2]  # get every other element starting from the first (x coordinates)
# y_coords = coords[1::2]  # get every other element starting from the second (y coordinates)

# x_min = min(x_coords)
# x_max = max(x_coords)
# y_min = min(y_coords)
# y_max = max(y_coords)

# x_final = x_max - x_min
# y_final = y_max - y_min
# print(f"Bounding box: ({x_final} , {y_final})")
# print(f"Center points: ({x_final} , {y_final})")

# print(f"Bounding box: ({x_min}, {y_min}), ({x_max}, {y_max})")

###############


import os
import cv2
from timeit import default_timer as timer

startTimer = timer()

# textDir = "./data"

textDir = "./testData"
imageDir = "./images"
metaFiles = int()

objects = {
    "plane": 0,
    "ship": 1,
    "storage-tank": 2,
    "baseball-diamond": 3,
    "tennis-court": 4,
    "basketball-court": 5,
    "ground-track-field": 6,
    "harbor": 7,
    "bridge": 8,
    "large-vehicle": 9,
    "helicopter": 10,
    "roundabout": 11,
    "soccer-ball-field": 12,
    "swimming-pool": 13,
    "container-crane": 14,
    "airport": 15,
    "helipad": 16
}

#! Make user-selectable later

# neededObjects = list()
# filter = list()

neededObjects = ["large-vehicle", "small-vehicle", "ship"]
filter = ["beans", "toast"]


# print(objects[1])

#? Iterate over the files in both directories
def main():
    global metaFiles
    for imageFile, textFile in zip(os.listdir(imageDir), os.listdir(textDir)):
        
        #? Check if the file extensions match
        if imageFile.endswith(".png") and textFile.endswith(".txt"):
            #? If the filenames match, process the files
            if imageFile[:-4] == textFile[:-4]:
                imagePath = os.path.join(imageDir, imageFile)
                textPath = os.path.join(textDir, textFile)

                #! Process the files: 

                #? this loops over each file in the directory
                with open(textPath, "r") as f:
                    contents = f.read()
                    contentsSplit = contents.split()
                    contentsSplitLine = contents.split("\n")

                    #? filter out objects that are not wanted 
                    #! ask user if to filter ALL or ANY

                    #? check if all of the needed objects exist
                    # if all(obj in contents for obj in neededObjects):
                    #     print(f"File includes all needed objects ({textPath})")
                    # else:
                    #     print(f"File does not include all needed objects ({textPath})")
                    #     continue

                    #? check if one or more of the needed objects exist
                    # if any(obj in contents for obj in neededObjects):
                    #     print(f"File includes >=1 of the needed objects ({textPath})")
                    # else:
                    #     print(f"File doesn't include any of the needed objects ({textPath})")
                    #     continue

                    # for obj in neededObjects:
                    #     if obj not in contents:
                    #         #? splice the first 2 items in the array
                    #         # print("test")
                    #         # contents = contents.split()[2:]
                    #         print(textPath)
                    # else:
                    #     # print(textPath)
                    #     continue

                    #? remove metadata
                    #! ask user to remove metada or not

                    # if "imagesource" in contents or "gsd" in contents:
                    #     metaFiles += 1            
                    #     #? splice the first 2 items in the array
                    #     contents = contentsSplit[2:]
                    #     print(f"\nFile includes metadata ({textFile})\n")
                    #     print(f"{contents}")
                    # else:
                    #     print(f"\nFile does not include metadata ({textFile})\n")
                    #     print(f"{contents}")
                    #     continue

                    # print(contentsSplitLine)
                    for i in range(len(contentsSplitLine)):
                        contentsSplitLine[i] = ' '.join(contentsSplitLine[i].rsplit(' ', 2)[:-2]).split()
                        coordinatesList = contentsSplitLine

                    for coordinates in coordinatesList:
                        print(coordinates)

                    # print(contentsSplitLine)
                    # print(f"\n{coordinatesList}")

                    

                
                #? output
                # print(contents)

                    
                            
                # Load the image from the file
                # img = cv2.imread(imagePath)
                
                # Get the height and width of the image
                # height, width, channels = img.shape

                # print(f"\nImage resolution: {width}x{height}\n")
            else:
                continue
            
        else:
            # If the file extensions do not match, skip this iteration
            filesSkipped += 1
            continue


# print(filesSkipped)

if __name__ == "__main__":
    main()
    endTimer = timer()
    print(f"\nNumber of files with metadata: {metaFiles}/{len(os.listdir(textDir))}")    

    print(f"Time to execute: {endTimer - startTimer}s")