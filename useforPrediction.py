
from ultralytics import YOLO
from PIL import Image
import io
import base64

model = YOLO('best.pt')


def predict (imageByte):
    image  = Image.open(io.BytesIO(imageByte)).convert("RGB")# read the image as bytes
    result = model(image)
    img_res= Image.fromarray(result[0].plot()) #result[0] contain original image and the boxes
    buf=io.BytesIO()
    img_res.save(buf,format="PNG")
    base64_str = base64.b64encode(buf.getvalue()).decode('utf-8')
    uri =f"data:image/png;base64,{base64_str}"
    return uri  # return the uri to the client

