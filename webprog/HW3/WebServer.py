import aiohttp
import os
from aiohttp import web

# функция для чтения файлов
def getText(fileName):
    f = open(fileName)
    return f.read()

# функция получения списка
def getList():
    return web.Response(text=os.listdir(path="."))

# функция, которая печатает текст в корневой странице
async def hello(request):
    return web.Response(text="Hello world")

# 1 задание
async def getFileText(request):
    return web.Response(content_type="text/plain", text=getText('myfile1.txt'))

# 2 задание
async def getFilePython(request):
    return web.Response(content_type="text/plain", text=getText('myserver.py'))

# 3 задание
async def getFileRST(request):
    return web.Response(content_type="text/x-rst", text=getText('README.rst'))

# Функция-обработчик
async def websocket_handler(request):

    ws = web.WebSocketResponse()
    await ws.prepare(request)
    await getList()

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == "close":
                await ws.close()
            else:
                await ws.send_str(msg.data + "/answer")
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print("ws connection closed with exception %s" % ws.exception())

    print("websocket connection closed")

    return ws


# Добавление веб-сокетов
app = web.Application()
app.add_routes([web.get("/", hello)])
app.add_routes([web.get("/myfile1.txt", getFileText)])
app.add_routes([web.get("/myserver.py", getFilePython)])
app.add_routes([web.get("/README.rst", getFileRST)])
app.add_routes([web.get("/ws", websocket_handler)])
web.run_app(app)
