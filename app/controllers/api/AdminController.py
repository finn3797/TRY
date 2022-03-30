import json
from masonite.controllers import Controller
from app.models.User import User
from masonite.authentication import Auth
from masonite.response import Response
from app.helpers import helper


class AdminController(Controller):
    def me(self, auth: Auth):
        # 测试
        # return user
        return helper.resModel(auth.attempt_by_id(1))
        
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