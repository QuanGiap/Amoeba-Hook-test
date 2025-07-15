from fastapi import FastAPI, Request, Response
import xmltodict
app = FastAPI()

@app.get("/")
async def part_update_hook(request: Request):
    xml = await request.body()
    print(f"XML part request: {xml}")
    data = xmltodict.parse(xml)
    print(f"Received part update: {data}")
    # component = data["LibraryComponentUpdate"]["Component"]
    # part_number = component["PartNumber"]
    # change_type = component["ChangeType"]
    # attributes = component.get("Attributes", {})

    # Log or process update
    # xml_response = """
    # <LibraryComponentUpdateResponse>
    #     <Status>Success</Status>
    #     <Message>Component received</Message>
    # </LibraryComponentUpdateResponse>
    # """

    # return Response(content=xml_response, media_type="application/xml")
    return Response(content=xml, media_type="application/xml")

@app.get("/ping")
def ping():
    return "pong"