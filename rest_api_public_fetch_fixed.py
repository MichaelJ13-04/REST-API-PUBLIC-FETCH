import asyncio
import aiohttp


# NHTSA Public Vehicle API
API_URL = (
    "https://vpic.nhtsa.dot.gov/api/vehicles/"
    "GetVehicleVariableList?format=json"
)


async def fetch_vehicle_data():
    print("Loading vehicle data from NHTSA API...")
    print("Please wait...\n")

    try:
        timeout = aiohttp.ClientTimeout(total=30)

        async with aiohttp.ClientSession(timeout=timeout) as session:
            # Send an asynchronous GET request
            async with session.get(API_URL) as response:
                response.raise_for_status()
                data = await response.json(content_type=None)

        # Extract records from the API response
        vehicle_data = data.get("Results", [])

        # Keep only Active Safety System records
        active_safety_data = [
            item for item in vehicle_data
            if item.get("GroupName") == "Active Safety System"
        ]

        print("Vehicle data retrieved successfully!")
        print("\nACTIVE SAFETY SYSTEM VEHICLE VARIABLES")
        print("=" * 50)

        if not active_safety_data:
            print("No Active Safety System records were found.")
            return

        for item in active_safety_data:
            print(f"ID: {item.get('ID')}")
            print(f"Name: {item.get('Name')}")
            print(f"Group: {item.get('GroupName')}")
            print("-" * 50)

        print(f"Total matching records: {len(active_safety_data)}")

    except asyncio.TimeoutError:
        print("Error: The API request timed out. Please try again.")

    except aiohttp.ClientError as error:
        print(f"Error connecting to the NHTSA API: {error}")

    except (ValueError, TypeError) as error:
        print(f"Error processing the API response: {error}")


async def main():
    await fetch_vehicle_data()


if __name__ == "__main__":
    asyncio.run(main())
