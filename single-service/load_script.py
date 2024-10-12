from collections import Counter

import asyncio
import aiohttp


# Define the number of requests to send
NUM_REQUESTS = 10 # You can change this to any number

async def fetch_fibonacci(session, url):
    try:
        async with session.get(url) as response:
            return response.status
    except Exception as e:
        print(f"Request failed: {e}")
        return None

async def main():
    num_seconds = 1
    url = f'http://localhost:5881/wait-n?n={num_seconds}'  # Adjust the URL as needed
    start_time = asyncio.get_event_loop().time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_fibonacci(session, url) for _ in range(NUM_REQUESTS)]
        results = await asyncio.gather(*tasks)

        response_counts = Counter(results)
        for response, count in response_counts.items():
            print(f"Response {response} occurred {count} times")

    end_time = asyncio.get_event_loop().time()
    print(f"Time taken: {end_time - start_time} seconds")

if __name__ == '__main__':
    asyncio.run(main())