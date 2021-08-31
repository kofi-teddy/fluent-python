# Async await

# from timeit import default_timer
# import requests


# def load_data(delay):
#     print(f"Starting {delay} second timer")
#     text = requests.get(f"https://httpbin.org/delay/{delay}").text
#     print(f"Completed {delay} second timer")
#     return text


# def run_demo():
#     start_time = default_timer()

#     two_data = load_data(2)
#     three_data = load_data(3)

#     elapsed_time = default_timer() - start_time
#     print(f"The operation took {elapsed_time:.2} seconds")    

# def main():
#     run_demo()

# main()


from timeit import default_timer

from requests.sessions import session
import aiohttp
import asyncio


async def load_data(session, delay):
    print(f"Starting {delay} second timer")
    async with session.get(f"https://httpbin.org/delay/{delay}") as resp:
        text = await resp.text()
        print(f"Completed {delay} second timer")
        return text


async def main():
    start_time = default_timer()

    # Create a single session
    async with aiohttp.ClientSession() as session:
        # Set up task and keep things running
        two_task = asyncio.create_task(load_data(2)) 
        three_task = asyncio.create_task(load_data(3)) 

        # Simulate other processing
        await asyncio.sleep(1)
        print("Doing other works")

        # Get values
        two_result = await two_task
        three_result = await three_task

        # Print results
        elapsed_time = default_timer() - start_time
        print(f"The operation took {elapsed_time:.2} seconds")    


asyncio.run(main())