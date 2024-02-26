import os
import cv2
from timeit import default_timer as timer

startTimer = timer()

textDir = "./inputData"
imageDir = "./images"
outDir = "./outputData"
textFiles = os.listdir(textDir)
imagesFiles = os.listdir(imageDir)
outFiles = os.listdir(outDir)

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
                contentsSplitLine = []
                test = []

                with open(textPath, "r") as unreadText:                    
                    contents = unreadText.read()
                    contentsSplitLine = contents.splitlines()

                    #? the block below checks for the presence of an "object" in the
                    #? file which isn't included in the metadata so it gets removed
                    # contentsSplitLine = contents.splitlines()[2:] 
                    
                for line in contentsSplitLine:
                    if "large-vehicle" in line or "small-vehicle" in line or "ship" in line:
                        test.append(line)

                contentsSplitLine = test
                    
                for i in range(len(contentsSplitLine)):
                    splitLine = ' '.join(contentsSplitLine[i].rsplit(' ', 2)[:-2]).split()
                    coordinatesList.append(splitLine)
             
                imageHeight, imageWidth, _ = img.shape
                # print(f"{imageWidth}x{imageHeight}")
                
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

                    out = (f"0 {centerX} {centerY} {boundingWidth} {boundingHeight}\n")
                    finalFile = open(f"./outputData/{textFile[:-4]}.txt", "a")
                    finalFile.write(out)

                finalFile.close()

    for outFile in outFiles:
        outPath = os.path.join(outDir, outFile)
        if os.path.getsize(outPath) == 0:
            os.remove(outPath)
            os.remove(f"./images/{outFile[:-4]}.png")
            
            print(f"File {outFile} is empty and has been removed.")

if __name__ == "__main__":
    main()
    endTimer = timer()
    print(f"Time to execute: {endTimer - startTimer}s")