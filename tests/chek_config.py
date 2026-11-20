from src.core.config import settings as Settings

def test_pool(pool_size,max_overflow,pool_timeout,pool_pre_ping):
    print("连接池大小：", pool_size)
    print("最大额外连接：", max_overflow)
    print("连接等待时间：", pool_timeout)
    print("连接检查：", pool_pre_ping)


test_pool(**Settings().engine_options)
