import azure.functions as func
import logging
from PIL import Image
from io import BytesIO

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="original/{name}",
                               connection="AzureWebJobsStorage")
@app.blob_output(arg_name="outputBlob",path="newpicture/{name}",connection="AzureWebJobsStorage") 
def smallestPictures(myblob: func.InputStream, outputBlob:func.Out[func.InputStream]):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
    
    image = Image.open(myblob)

    thumbnail_size = (128,128)

    image.thumbnail(thumbnail_size)

    thumb_stream = BytesIO()

    image.save(thumb_stream,format='JPEG')
    thumb_stream.seek(0)

    outputBlob.set(thumb_stream)