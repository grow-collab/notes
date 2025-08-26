from fastapi import FastAPI
from typing import Union, Optional

app = FastAPI()

# 声明不属于路径参数的其他函数参数时,他们将自动解释为“查询字符串”参数,就是 url?之后用&分割的 key-value 键值对
@app.get('/jobs/{kd}')
async def get_jobs(kd: str, xl: Union[str, None] = None, gj: Optional[str] = None):  # 没有默认参数即前端必须输入
    # 基于 kd,xl,gj的数据库查询操作
    return {'kd': kd, 'xl': xl, 'gj': gj}
