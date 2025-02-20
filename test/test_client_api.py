import unittest
from aiohttp import ClientError
from aioresponses import aioresponses
import asyncio
import json
import os
import sys
import aiohttp
ROOT_DIR=os.path.abspath(os.curdir)
sys.path.append(ROOT_DIR)
from Pheonix.client_api import clientAPI  # Replace `your_module` with the actual module name



class TestClientAPI(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        """Set up before each test."""
        self.client = clientAPI()

    async def test_fetch_success(self):
        """Test fetch() for a successful API call."""
        endpoint = "data"
        expected_response = {"message": "Success"}
        url = f"https://api.example.com/{endpoint}"

        with aioresponses() as mock:
            mock.get(url, payload=expected_response)

            async with aiohttp.ClientSession() as session:
                result = await self.client.fetch(session, endpoint)
                self.assertEqual(result, expected_response)

    async def test_fetch_404(self):
        """Test fetch() handling a 404 error."""
        endpoint = "data"
        url = f"https://api.example.com/{endpoint}"

        with aioresponses() as mock:
            mock.get(url, status=404)

            async with aiohttp.ClientSession() as session:
                with self.assertRaises(ClientError):
                    await self.client.fetch(session, endpoint)

    async def test_fetch_timeout(self):
        """Test fetch() handling a timeout error."""
        endpoint = "data"
        url = f"https://api.example.com/{endpoint}"

        with aioresponses() as mock:
            mock.get(url, exception=asyncio.TimeoutError)

            async with aiohttp.ClientSession() as session:
                with self.assertRaises(asyncio.TimeoutError):
                    await self.client.fetch(session, endpoint)

    async def test_fetch_all_success(self):
        """Test fetch_all() for multiple successful API calls."""
        endpoints = ["data1", "data2"]
        responses = [{"message": "Data 1"}, {"message": "Data 2"}]
        
        with aioresponses() as mock:
            for i, endpoint in enumerate(endpoints):
                mock.get(f"https://api.example.com/{endpoint}", payload=responses[i])

            result = await self.client.fetch_all(endpoints)
            self.assertEqual(result, responses)

if __name__ == "__main__":
    unittest.main()