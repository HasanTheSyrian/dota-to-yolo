import os
import cv2
from timeit import default_timer as timer

startTimer = timer()

textDir = "./testData"
imageDir = "./images"
metaFiles = int()
coordinatesList = list()

#? iterate over the files in both directories
def main():
    global metaFiles
    global coordinatesList
    for imageFile, textFile in zip(os.listdir(imageDir), os.listdir(textDir)):
        
        #? check if the file extensions match
        if imageFile.endswith(".png") and textFile.endswith(".txt"):
            #? if the filenames match, process the files
            if imageFile[:-4] == textFile[:-4]:
                imagePath = os.path.join(imageDir, imageFile)
                textPath = os.path.join(textDir, textFile)
                img = cv2.imread(imagePath) 

                #? loop over each file in the directory
                with open(textPath, "r") as f:
                    contents = f.read()
                    contentsSplitLine = contents.splitlines()[2:]

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