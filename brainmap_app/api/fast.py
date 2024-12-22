from fastapi import FastAPI, File, UploadFile
from PIL import Image
from io import BytesIO
from brainmap_app.interface.workflow import predict


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict_cnn/")
async def predict_cnn_endpoint(file: UploadFile = File(...)):
    # Save the uploaded file to disk
    img_path = f"temp_{file.filename}"
    with open(img_path, "wb") as img_file:
        img_file.write(await file.read())

    # Make prediction using CNN
    prediction = predict_cnn(img_path)

    return {"cnn_prediction": prediction.tolist()}

@app.post("/predict_yolo/")
async def predict_yolo_endpoint(file: UploadFile = File(...)):
    # Save the uploaded file to disk
    img_path = f"temp_{file.filename}"
    with open(img_path, "wb") as img_file:
        img_file.write(await file.read())

    # Make prediction using YOLO
    results = predict_yolo(img_path)

    return {"yolo_results": results}

@app.post("/explain_cnn/")
async def explain_cnn_endpoint(file: UploadFile = File(...)):
    # Save the uploaded file to disk
    img_path = f"temp_{file.filename}"
    with open(img_path, "wb") as img_file:
        img_file.write(await file.read())

    # Explain prediction using SHAP
    shap_values = explain_cnn_prediction(img_path)

    return {"shap_values": shap_values}
