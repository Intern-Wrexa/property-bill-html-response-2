import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse


app = FastAPI()


# root fucntion
@app.get("/")
async def root():
  html_content = """
    <html>
        <head>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                h1 {
                    font-size: 48px;
                    color: #333;
                }
            </style>
        </head>
        <body>
            <h1>Api Made By D</h1>
        </body>
    </html>
    """
  return HTMLResponse(content=html_content)



@app.get("/fetch-property-details/old-bill/load-response/{zone_no}/{ward_no}/{property_id}/{sub_no}")
async def fetch_property_details(zone_no: str, ward_no: str, property_id: str, sub_no: str):
    url = f"https://erp.chennaicorporation.gov.in/ptis/citizensearch/searchPropByBillNumber!search.action?isNew=N&zoneNo={zone_no}&wardNo={ward_no}&propertyId={property_id}&subNo={sub_no}"

    response = requests.get(url)

    if response.status_code == 200:
        return HTMLResponse(content=response.text)
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch details")



@app.get("/fetch-property-details/new-bill/load-response/{zone_no}/{ward_no}/{bill_no}")
async def fetch_property_details(zone_no: str, ward_no: str, bill_no: str):
    url = f"https://erp.chennaicorporation.gov.in/ptis/citizensearch/searchPropByBillNumber!search.action?isNew=Y&newzoneNo={zone_no}&newwardNo={ward_no}&newbillNo={bill_no}"

    response = requests.get(url)

    if response.status_code == 200:
        return HTMLResponse(content=response.text)
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch details")
