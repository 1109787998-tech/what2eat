from pydantic_settings import BaseSettings, SettingsConfigDict  #第三方库提供的类具有读取配置和校验数据的能力
from typing import Literal #指定类型为字面量  
from pydantic import computed_field #计算属性

# 继承BaseSettings管理项目配置
class settings(BaseSettings):    
    app_name:str = "Waht to Eat" #在fastapi导入这个对象调用属性，页面里面就会显示这个名字
    debug:bool = False #模式调试开关，开启fastapi调试模式，便于查看错误，关闭适合正式部署

    #数据库类型
    db_type:Literal["postgresql","mysql"] = "postgresql" #只能选择postgresql或mysql

    # 数据库配置
    db_host:str = "localhost" #服务器地址
    db_port:int = 5432        #默认值5432
    db_user:str = "what2eat_user"  #用户
    db_name:str = "what2eat"  #数据库名称
    db_password:str 

    # PostgreSQL连接池 
    pool_size: int = 5 #池内最多保留5条连接供复用
    max_overflow: int = 5 #繁忙时允许额外创建5条临时连接
    pool_timeout: int = 30 #获取连接最多等待30s
    pool_pre_ping:bool = True #每次从池里拿连接前先ping一下，确保连接可用


    # 数据库连接字符串
    @computed_field  #计算字段，不存放结果当场计算，
    @property #让方法变成属性
    def database_url(self) -> str:
        if self.db_type == "postgresql":
            return(
                f"postgresql+asyncpg://{self.db_user}:{self.db_password}"
                f"@{self.db_host}:{self.db_port}/{self.db_name}"
              
            )
        else:
            raise ValueError("不支持的数据库类型")

    @property
    def engine_options(self) -> dict:
        return{
            "pool_size": self.pool_size,
            "max_overflow": self.max_overflow,
            "pool_timeout": self.pool_timeout,
            "pool_pre_ping": self.pool_pre_ping,
        }
    
    #环境配置
    model_config = SettingsConfigDict(   # 指定配置文件路径
        env_file=".env",                # 指定从.env文件读取配置
        env_file_encoding="utf-8",      # 指定文件编码为utf-8
        case_sensitive =False           # 指定大小写不敏感
    )

def test_pool(pool_size,max_overflow,pool_timeout,pool_pre_ping):
    print("连接池大小：", pool_size)
    print("最大额外连接：", max_overflow)
    print("连接等待时间：", pool_timeout)
    print("连接检查：", pool_pre_ping)

 #这里 ** 的作用，就是把字典中的键值对展开为函数的关键字参数
settings = settings()
test_pool(**settings.engine_options)
#data = settings.model_dump()
#print(settings.engine_options)