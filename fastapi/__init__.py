"""FastAPI framework, high performance, easy to learn, fast to code, ready for production"""

# 概览: 本文件是项目的起始文件，在我们使用import语句导入fastapi时，相当于进入了本文件的范围；

# 全局变量：
#  1. 全局变量__version__用来说明此fastapi的版本；
#  2. 另加17个从不本包中导入的各个模块中的接口/方法；
#  3. 从这里可以看到，模块主要的内容有：
#    1）application：应用
#    2）background：后台任务
#    3）exceptions：异常处理相关
#    4）param_functions：与传参相关的内容
#    5）requests：请求
#    6）response：响应
#    7）routing：路由
#    8）websocket：websocket相关的操作，后面可以看到，都是直接调用的starlette模块中响应的内容
#  这里没有出现pydantic是因为它主要用于数据验证，到时候在相关模块中直接调用来使用；

# 外部导入：从starlette中导入status，作为本模块的status来调用，status中主要定义了一些HTTP状态码相关的常量，也包括websocket的部分状态码；

# 代码格式说明：因为在“.flake8”中定义了"exclude = __init__.py"，所以此文档中代码风格虽然不符合要求（比如，从param_functions导入多个函数），但是不会提示警告信息；

# better-codes：
#  1. “from ... import ... as ..."的引入方式，有助于将来万一修改类名，对使用者来说，仍然是无感知的；
#  2. 命名中的”param_functions“意味着导入的是函数，而非类；

# 代码逻辑：
#  1. 因为我们创建FastAPI的app时，是创建一个实例的，这个实例就是基于这里的FastAPI建立的，下面我们进入applications文件中查看FastAPI类。

__version__ = "0.65.1"

from starlette import status as status

from .applications import FastAPI as FastAPI
from .background import BackgroundTasks as BackgroundTasks
from .datastructures import UploadFile as UploadFile
from .exceptions import HTTPException as HTTPException
from .param_functions import Body as Body
from .param_functions import Cookie as Cookie
from .param_functions import Depends as Depends
from .param_functions import File as File
from .param_functions import Form as Form
from .param_functions import Header as Header
from .param_functions import Path as Path
from .param_functions import Query as Query
from .param_functions import Security as Security
from .requests import Request as Request
from .responses import Response as Response
from .routing import APIRouter as APIRouter
from .websockets import WebSocket as WebSocket
from .websockets import WebSocketDisconnect as WebSocketDisconnect
