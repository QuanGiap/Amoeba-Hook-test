from fastapi import FastAPI, Request, Response
import xmltodict
app = FastAPI()

@app.post("/")
async def part_update_hook(request: Request):
    xml_body = await request.body()
    # Optionally log or parse it:
    print(xml_body.decode())

    # Prepare a SOAP XML response
    soap_response = """<?xml version="1.0" encoding="UTF-8"?>
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
        <soapenv:Body>
            <Response xmlns="http://www.mentor.com/harness/Schema/LibrarySchema">
                <Status>Success</Status>
            </Response>
        </soapenv:Body>
    </soapenv:Envelope>"""

    return Response(content=soap_response, media_type="application/xml")

@app.get("/ping")
def ping():
    return "pong"
