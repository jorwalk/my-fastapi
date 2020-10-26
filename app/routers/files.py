from fastapi import APIRouter, File, Form, UploadFile
from typing import List

router = APIRouter()


@router.post("/file/", tags=["File"])
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@router.post("/upload_file/", tags=["File"])
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename, "contents": await file.read()}


@router.post("/files/", tags=["Files"])
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@router.post("/uploadfiles/", tags=["Files"])
async def create_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}
