import uvicorn
from fastapi import FastAPI
from app01.urls import user
from app02.urls import shop

app = FastAPI()

# 路由分发配置：采用模块化路由设计，便于大型项目的路由管理和维护
# 路由分发的核心思路（3步）：
# 1. 在子模块中通过APIRouter创建子路由对象，并定义该模块下的路由与对应视图函数
# 2. 在主应用文件中导入各子模块的路由实例（如上面导入的user和shop）
# 3. 通过主应用实例的include_router方法注册子路由，实现路由的集中管理

# 注册用户中心子路由
# 参数说明：
# - user：导入的子路由实例
# - prefix='/user'：为该子路由下所有接口统一添加前缀，访问时需加上`/user`
# - tags=['用户中心接口']：在自动生成的API文档（如Swagger UI）中，将该路由下的接口归类到该标签下
app.include_router(user, prefix='/user', tags=['用户中心接口'])

# 注册购物中心子路由
# 同理，所有接口路径将自动添加`/shop`前缀，文档中归类到"购物中心接口"标签
app.include_router(shop, prefix='/shop', tags=['购物中心接口'])

if __name__ == '__main__':
    uvicorn.run('app:app', port=8000, reload=True)
