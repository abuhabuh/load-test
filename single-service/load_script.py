import asyncio
import aiohttp

# Define the number of requests to send
NUM_REQUESTS = 50000  # You can change this to any number

async def fetch_fibonacci(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return True
            else:
                return False
    except Exception as e:
        print(f"Request failed: {e}")
        return False

async def main():
    url = 'http://localhost:5881/fibonacci?n=30'  # Adjust the URL as needed
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_fibonacci(session, url) for _ in range(NUM_REQUESTS)]
        results = await asyncio.gather(*tasks)

        success_count = sum(results)
        failure_count = NUM_REQUESTS - success_count

        print(f"Successes: {success_count}, Failures: {failure_count}")

if __name__ == '__main__':
    asyncio.run(main())