# ThumbnailProject
This function creates a small picture from a large picture

The architecture selected was Azure Functions due to the capacity and easiness of creating the code using Python language with
PIL (now Pillow) library which manages correctly the image processing.

Azure function it not have a high cost because it is payment as you go. 

Path description:
1. The user uploads the original size picture in a storage container
2. once the file is uploaded, the trigger blob detects a new file starting to run
3. It becomes a 128 x 128 px file size
4. the new file is pulled into a new storage container
