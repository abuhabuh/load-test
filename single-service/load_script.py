from collections import Counter

import asyncio
import aiohttp


async def fetch_fibonacci(session, url) -> str:
    try:
        print(f'sending requests')
        async with session.get(url) as response:
            return f'status: {response.status}'
    except TimeoutError as e:
        return f'timeout: client side'
    except Exception as e:
        return f'failed: {e}'


async def main():
    print('Starting load script')
    url = f'http://localhost:5881/fibonacci?n=2'  # Adjust the URL as needed

    # Define the number of concurrent requests to send
    num_requests = 1000

    start_time = asyncio.get_event_loop().time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_fibonacci(session, url) for _ in range(num_requests)]
        results = await asyncio.gather(*tasks)

        response_counts = Counter(results)
        for response, count in response_counts.items():
            print(f'Response "{response}" occurred {count} times')

    end_time = asyncio.get_event_loop().time()
    print(f'Time taken: {end_time - start_time} seconds')


if __name__ == '__main__':
    asyncio.run(main())