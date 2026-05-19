from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "PDF Compressor API is alive"}


@app.get("/api/health")
def health():
    return{
        "status":"ok",
        "service": "pdf-compressor",
        "version": "0.1.0",
    }