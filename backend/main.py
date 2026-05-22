from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import shutil
import os
from pathlib import Path
import subprocess
from fastapi import Form
import zipfile
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:5173"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)
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

# Limits
MAX_FILES = 10

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
async def compress(files: list[UploadFile] = File(...), quality: str = Form("medium")):
    if not files:
        raise HTTPException(status_code=400, detail="File must be a pdf")
    
    if len(files) > MAX_FILES:
        raise HTTPException(
            status_code=400,
            detail=f"Maximum {MAX_FILES} files allowed, got {len(files)}",
        )
    
    if quality not in QUALITY_PRESENTS:
        raise HTTPException(
            status_code=400,
            detail=f"Quality must be one of: {list(QUALITY_PRESENTS.keys())}",
        )

    present = QUALITY_PRESENTS[quality]
    compressed_paths =[]

        # Process each file
    for file in files:
        # Validate it's a PDF
        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail=f"File '{file.filename}' is not a PDF",
            )

        # Save upload
        input_path = UPLOAD_DIR / file.filename
        with open(input_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Build output path
        output_path = COMPRESSED_DIR / f"compressed_{file.filename}"

        # Compress
        try:
            compress_pdf(input_path, output_path, present)
        except RuntimeError as e:
            raise HTTPException(status_code=500, detail=str(e))

        compressed_paths.append(output_path)

    # If only one file, return it directly (no ZIP)
    if len(compressed_paths) == 1:
        return FileResponse(
            path=compressed_paths[0],
            media_type="application/pdf",
            filename=compressed_paths[0].name,
        )

    # Multiple files: bundle into a ZIP
    zip_path = COMPRESSED_DIR / "compressed_files.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in compressed_paths:
            zf.write(path, arcname=path.name)

    return FileResponse(
        path=zip_path,
        media_type="application/zip",
        filename="compressed_files.zip",
    )