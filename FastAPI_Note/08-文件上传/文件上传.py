import uvicorn
from fastapi import FastAPI, File, UploadFile
from typing import List
import os

app = FastAPI()


# 08-文件上传
@app.post('/file')
async def get_file(file: bytes = File()):
    # 适合小文件上传
    print('文件', file)
    return {'file': len(file)}


@app.post('/files')
async def get_files(files: List[bytes] = File()):
    # 多个文件上传
    for file in files:
        print('文件', len(file))
    return {'file': len(files)}


@app.post('/uploadFile')
async def upload_file(file: UploadFile):
    # 单个文件上传
    print('文件', file)  # 拿到一个文件句柄

    # 将文件下载到服务器
    path = os.path.join('imgs', file.filename)
    with open(path, 'wb') as f:
        for line in file.file:
            f.write(line)

    return {'file': file.filename}


@app.post('/uploadFiles')
async def upload_files(files: List[UploadFile]):
    # 多个文件上传
    print(files)
    return {'names': [file.filename for file in files]}


if __name__ == '__main__':
    uvicorn.run('08-文件上传:app', port=8000, reload=True)
