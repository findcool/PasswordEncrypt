# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
"""
斗鱼网登录'password'加密参数破解
url：http://www.douyu.com/directory
# import hashlib
# print(hashlib.md5("666666".encode("utf-8")).hexdigest())--->'f379eaf3c831b04de153469d1bec345e'
"""
import os
from passwordencrypt.utils import get_execjs_instance


current_filename = os.path.basename(__file__)
js_filename = get_execjs_instance.get_js_filename(current_filename)
ctx = get_execjs_instance.get_ctx_obj(js_filename)


password = "666666"
js_pattern = 'getPwd("{}")'.format(password)
print(ctx.eval(js_pattern))
