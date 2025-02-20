import aiohttp






class clientAPI:

    def __init__(self,url):
        self.url = url

    async def fetch(self,session, variables,horizon,model,start_date,end_date,longtitude,latitude):
        params = {
            "latitude": longtitude,
            "longitude": latitude,
            "start_date": start_date,
            "end_date": end_date,
            "hourly": variables
        }
      
        async with session.get(self.url, params=params) as response:
            return await response.json()

    async def fetch_all(self, variables,horizon,model,start_date,end_date,longtitude,latitude):
        async with aiohttp.ClientSession() as session:
            return await self.fetch(session, variables,horizon,model,start_date,end_date,longtitude,latitude)

    