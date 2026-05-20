from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import shutil
import os
from pathlib import Path
import subprocess
from fastapi import Form


app = FastAPI()

#folder to temp hold upload files
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
COMPRESSED_DIR = Path("compressed")
COMPRESSED_DIR.mkdir(exist_ok=True)

GHOSTSCRIPT_PATH = r"C:\\Program Files\\gs\\gs10.07.1\\bin\\gswin64c.exe"

QUALITY_PRESENTS={
    "low": "/printer",
    "medium": "/ebook",
    "high": "/screen",
}


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

def compress_pdf(input_path: Path,output_path: Path, present: str)-> None:
    #run the ghostscript to compress a pdf
    result = subprocess.run(
        [ GHOSTSCRIPT_PATH,
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            f"-dPDFSETTINGS={present}",
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            f"-sOutputFile={output_path}",
            str(input_path),],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Ghostscript failed: {result.stderr}")
    
@app.post("/api/compress")
async def compress(file: UploadFile = File(...), quality: str = Form("medium")):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="File must be a pdf")
    
    if quality not in QUALITY_PRESENTS:
        raise HTTPException(
            status_code=400,
            detail=f"Quality must be one of: {list(QUALITY_PRESENTS.keys())}",
        )
    #save uploaded file to the disk
    input_path = UPLOAD_DIR/file.filename
    with open(input_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    output_path = COMPRESSED_DIR / f"compressed_{file.filename}"

    present = QUALITY_PRESENTS[quality]
    try:
        compress_pdf(input_path, output_path, present)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

    return FileResponse(
        path=output_path,
        media_type="application/pdf",
        filename=f"compressed_{file.filename}",
    )