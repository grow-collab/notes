# 数据库配置内容对象
TORTOISE_ORM = {
    'connections': {
        'default': {
            # 'engine': 'tortoise.backends.asyncpg', PostgreSQL
            'engine': 'tortoise.backends.mysql',  # MYSQL or Mariadb
            'credentials': {
                'host': '127.0.0.1',
                'port': 3306,
                'user': 'root',
                'password': '123456',
                'database': 'fastapi',
                'charset': 'utf8mb4',
                'minsize': 1,
                'maxsize': 5,
                'echo': True
            }
        }
    },
    'apps': {
        'models': {
            'models': ['models','aerich.models'],
            'default_connection': 'default'
        }
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai',
}
