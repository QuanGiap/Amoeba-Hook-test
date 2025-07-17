from fastapi import FastAPI, Request, Response
import xmltodict
app = FastAPI()

@app.post("/")
async def part_update_hook(request: Request):
    xml_body = await request.body()
    print('//////////////////////////////////////////////////////////////////////////')
    print('xml original')
    print(xml_body)
    print('//////////////////////////////////////////////////////////////////////////')
    print('xml decoded')
    print(xml_body.decode())
    print('//////////////////////////////////////////////////////////////////////////')
    print('xml to dict')
    dict = xmltodict.parse(xml_body)
    print(dict)
    return Response(content=xml_body, media_type="text/xml")

@app.get("/ping")
def ping():
    return "pong"
