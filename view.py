# -*- coding:utf-8 -*-

from bottle import route, run, debug, template, request, redirect, static_file


@route( '/view' )
def view_list():
    names = ['green','red','red','green']
    try:
        f = open( 'E:\\test3\\test\\data\\result.txt', 'r' )
        result = f.read()
    finally:
        if f:
            f.close()

    names = result.split(" ")
    totals = 0
    for data in names:
        if data == 'green':
            totals += 1

    output = template( 'make_table',rows = names, count = totals )
    return output


#定义图片路径
images_path = './static'


@route('/images/<filename:re:.*\.png>')
def server_static(filename):
    return static_file(filename, root=images_path)


debug( True )
run()
