from hashlib import md5
import json
from masonite.controllers import Controller
import pendulum
from app.models.User import User
from masonite.authentication import Auth
from masonite.response import Response
from app.helpers import helper
from masonite.request import Request
from masonite.filesystem import Storage
from masonite.helpers import UrlsHelper

from app.notifications.Notice import Notice


class AdminController(Controller):
    def me(self, auth: Auth):
        # 测试
        # return user
        return helper.resModel(auth.user())
        
    def ver(self, response: Response):
        data = '1.0.0'
        return helper.res(data,'', 200, response)

    def mymenu(self):
        jsonMenu = '''
        {
                        "data": {
                            "menu": [
                                {
                                    "name": "home",
                                    "path": "/home",
                                    "meta": {
                                        "title": "首页",
                                        "icon": "el-icon-eleme-filled",
                                        "type": "menu"
                                    },
                                    "children": [
                                        {
                                            "name": "dashboard",
                                            "path": "/dashboard",
                                            "meta": {
                                                "title": "控制台",
                                                "icon": "el-icon-menu",
                                                "affix": true
                                            },
                                            "component": "home"
                                        },
                                        {
                                            "name": "userCenter",
                                            "path": "/usercenter",
                                            "meta": {
                                                "title": "个人信息",
                                                "icon": "el-icon-user"
                                            },
                                            "component": "userCenter"
                                        }
                                    ]
                                },
                                {
                                    "name": "template",
                                    "path": "/template",
                                    "meta": {
                                        "title": "模板",
                                        "icon": "el-icon-files",
                                        "type": "menu"
                                    },
                                    "children": [
                                        {
                                            "path": "/template/blank",
                                            "name": "blank",
                                            "meta": {
                                                "title": "空白模板",
                                                "icon": "el-icon-folder",
                                                "type": "menu"
                                            },
                                            "component": "template/blank"
                                        },
                                        {
                                            "path": "/template/chartlist",
                                            "name": "chartlist",
                                            "meta": {
                                                "title": "统计列表",
                                                "icon": "el-icon-data-analysis",
                                                "type": "menu"
                                            },
                                            "component": "template/chartlist"
                                        },
                                        {
                                            "path": "/template/calendar",
                                            "name": "calendar",
                                            "meta": {
                                                "title": "日历计划",
                                                "icon": "el-icon-calendar",
                                                "type": "menu"
                                            },
                                            "component": "template/calendar"
                                        },
                                        {
                                            "path": "/template/list",
                                            "name": "list",
                                            "meta": {
                                                "title": "详细列表",
                                                "icon": "el-icon-fold",
                                                "type": "menu"
                                            },
                                            "component": "template/list"
                                        },
                                        {
                                            "path": "/template/list/save/:id?",
                                            "name": "list-save",
                                            "meta": {
                                                "title": "新标签",
                                                "hidden": true,
                                                "active": "/template/list",
                                                "type": "menu"
                                            },
                                            "component": "template/list/save"
                                        },
                                        {
                                            "path": "/template/svgmap",
                                            "name": "svgmap",
                                            "meta": {
                                                "title": "地理信息",
                                                "icon": "el-icon-map-location",
                                                "type": "menu"
                                            },
                                            "component": "template/svgmap"
                                        },
                                        {
                                            "path": "/template/tabinfo",
                                            "name": "tabinfo",
                                            "meta": {
                                                "title": "分栏明细",
                                                "icon": "el-icon-document",
                                                "type": "menu"
                                            },
                                            "component": "template/tabinfo"
                                        }
                                    ]
                                }
                            ],
                            "permissions": [
                                "list.add",
                                "list.edit",
                                "list.delete"
                            ]
                        }
                    }
        '''
        return jsonMenu

    def sendNotifi(self, request: Request, auth: Auth):
        # dd(request)
        user_ids = request.input('user_ids', [])
        # dd(user_ids)
        # userList = user_ids.split(",")
        userList = User.find(user_ids)
        # dd(userList)
        # 无法传参
        # userList.map(lambda u: u.notify(Notice()))
        # from = auth.user().only(['name',''])
        userList.map(lambda u: self.notiContent(u))
        return helper.res('')

    def notiContent(self, u):
        # u.ext = {
        #     "avatar": 'avatar',
        #     "from": 'from',
        #     "text": 'textttt',
        # }
        u.notify(Notice())

    def getNotifi(self, auth: Auth):
        user = auth.user()
        return json.dumps(user.notifications.all())
        return helper.resJson(user.notifications.all())

    def upload(self, storage: Storage, request: Request):
        fileName = request.input('fileName', 'file')
        file = request.input(fileName)
        fileType = request.input('fileType', fileName)
        tz = pendulum.now('prc')
        # .to_datetime_string()
        # .encode(encoding='UTF-8')
        # dd(md5(tz).hexdigest())
        fn = md5(tz.to_datetime_string().encode(encoding='UTF-8')).hexdigest()
        fileDiskName = fileType + '/' + tz.to_date_string() + '/'
        # dd(fileDiskName)
        storage.disk('local').put_file(fileDiskName, file, fn)
        # dd(UrlsHelper)
        return UrlsHelper.asset('local', fileDiskName + fn)
        return helper.resJson({
            'data': urls.asset('disk', fileDiskName)
        },'上传成功')