"""
REST API Public Fetch
Retrieves NHTSA vehicle-variable data asynchronously and displays only
records whose GroupName is "Active Safety System".

Dependency:
    python -m pip install aiohttp

Run:
    python rest_api_public_fetch.py
"""

import asyncio
import aiohttp

API_URL = (
    "https://vpic.nhtsa.dot.gov/api/vehicles/"
    "GetVehicleVariableList?format=json"
)
TARGET_GROUP = "Active Safety System"


async def fetch_vehicle_variables():
    """GET the public API data and return the matching records."""
    print("Loading vehicle data...")

    try:
        timeout = aiohttp.ClientTimeout(total=30)

        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(API_URL) as response:
                response.raise_for_status()
                data = await response.json()

        # The API returns the records in the JSON "Results" array.
        records = data.get("Results", [])

        if not isinstance(records, list):
            raise ValueError("The API response did not contain a valid Results list.")

        # Filter the JSON records by the GroupName property.
        filtered_records = [
            item for item in records
            if item.get("GroupName") == TARGET_GROUP
        ]

        print("Data loaded successfully.")
        return filtered_records

    except asyncio.TimeoutError:
        print("Error: The API request timed out.")
    except aiohttp.ClientResponseError as error:
        print(f"HTTP error: {error.status} - {error.message}")
    except aiohttp.ClientError as error:
        print(f"Network error: {error}")
    except ValueError as error:
        print(f"Data error: {error}")
    except Exception as error:
        print(f"Unexpected error: {error}")

    return None


async def main():
    results = await fetch_vehicle_variables()

    if results is None:
        print("Unable to retrieve vehicle data.")
        return

    if not results:
        print(f'No records found for GroupName "{TARGET_GROUP}".')
        return

    print(f'\\nFound {len(results)} Active Safety System item(s):\\n')

    for item in results:
        print(f'Variable ID: {item.get("ID", "N/A")}')
        print(f'Name: {item.get("Name", "N/A")}')
        print(f'Group Name: {item.get("GroupName", "N/A")}')
        print("-" * 45)


if __name__ == "__main__":
    asyncio.run(main())
