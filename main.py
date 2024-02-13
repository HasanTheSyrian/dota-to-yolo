import os
import cv2
from timeit import default_timer as timer

startTimer = timer()

textDir = "./inputData"
imageDir = "./images"
imagesFiles = os.listdir(imageDir)
textFiles = os.listdir(textDir)
# out = list()

objects = {
    "plane": 0,
    "ship": 1,
    # "storage-tank": 2,
    # "baseball-diamond": 3,
    # "tennis-court": 4,
    # "basketball-court": 5,
    # "ground-track-field": 6,
    # "harbor": 7,
    # "bridge": 8,
    # "large-vehicle": 9,
    # "helicopter": 10,
    # "roundabout": 11,
    # "soccer-ball-field": 12,
    # "swimming-pool": 13,
    # "container-crane": 14,
    # "airport": 15,
    # "helipad": 16
}

#? make user-selectable later
# neededObjects = list()
# filter = list()
# filter = ["beans", "toast"]
# neededObjects = ["large-vehicle", "small-vehicle", "ship"]


#? iterate over the files in both directories
def main():
    for imageFile, textFile in zip(imagesFiles, textFiles):
        
        #? check if the file extensions match
        if imageFile.endswith(".png") and textFile.endswith(".txt"):
            #? if the filenames match, process the files
            if imageFile[:-4] == textFile[:-4]:

                imagePath = os.path.join(imageDir, imageFile)
                textPath = os.path.join(textDir, textFile)
                img = cv2.imread(imagePath) 

                coordinatesList = []


                with open(textPath, "r") as f:
                    
                    contents = f.read()
                    contentsSplitLine = contents.splitlines()[2:]

                    # print(contents)

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
                    
                    #? contentsSplitLine after the following blocks is stripped of strings and numbers are converted into integers

                    for i in range(len(contentsSplitLine)):
                        splitLine = ' '.join(contentsSplitLine[i].rsplit(' ', 2)[:-2]).split()
                        coordinatesList.append(splitLine)       

                    imageHeight, imageWidth, channels = img.shape
                    print(f"{imageWidth}x{imageHeight}")

                    for coordinates in coordinatesList:

                        coordinates = [eval(i) for i in coordinates]
                        coordsX = coordinates[::2]  # get every other element starting from the first (x coordinates)
                        coordsY = coordinates[1::2]  # get every other element starting from the second (y coordinates)

                        minX = min(coordsX)
                        maxX = max(coordsX)

                        minY = min(coordsY)
                        maxY = max(coordsY)
                        
                        centerX = ((maxX + minX)/2) * (1/imageWidth)
                        centerY = ((maxY + minY)/2) * (1/imageHeight)

                        boundingWidth = (maxX - minX) * (1/imageWidth)
                        boundingHeight = (maxY - minY) * (1/imageHeight)

                        #! There is an issue with the output data, the coordinates are not correct
                        #! when there is more than one file in testData. For now, it works with one file.
                        out = (f"0 {centerX} {centerY} {boundingWidth} {boundingHeight}\n")
                        # print(out)
                        #? Make outputData clearable with a command argument later
                        f = open(f"./outputData/{textFile[:-4]}.txt", "a")
                        f.write(out)
                        f.close()
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
    print(f"Time to execute: {endTimer - startTimer}s")