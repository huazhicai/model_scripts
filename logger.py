"""1、按照时间回滚
使用TimedRotatingFileHandler
对log，通常有一种想要的效果：log按天切分，每天一个log文件，保留三天内的log，过期删除。"""

# coding:utf-8
import time
import logging
from logging.handlers import TimedRotatingFileHandler

# logging的初始化,must
logging.basicConfig()

# logger的初始化
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

# 添加TimedRotatingFileHandler
# 定义一个1秒换一次log文件的handler,保留3个旧log文件
timefilehandler = TimedRotatingFileHandler("log/myapp.log", when='S', interval=3, backupCount=3)
# 设置后缀名称，跟strftime的格式一样
timefilehandler.suffix = "%Y-%m-%d_%H-%M-%S"

# 日志内容记录格式
# formatter = logging.Formatter('%(asctime)s|%(name)-12s: %(levelname)-8s %(message)s')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
timefilehandler.setFormatter(formatter)
logger.addHandler(timefilehandler)


while True:
    logger.info("test")
    time.sleep(0.5)
    
    
=========================================================================================================
"""RotatingFileHandler基于文件大小切分
这个配置是可以生效的，符合预期"""

# coding:utf-8
import time
import logging
from logging.handlers import RotatingFileHandler


logging.basicConfig()

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

# 写入文件，如果文件超过10M，仅保留5个文件。
handler = RotatingFileHandler('log/myapp.log', maxBytes=500, backupCount=5)
# formatter = logging.Formatter('%(asctime)s|%(name)-4s: %(levelname)-4s %(message)s')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# 设置后缀名称，跟strftime的格式一样
logger.addHandler(handler)

while True:
    time.sleep(0.5)
    logger.info("file teest")


