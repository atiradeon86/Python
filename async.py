import asyncio

async def myCoroutine():
    print('A simple Coroutine with Event Loop example')

def main():
    asyncio.run(myCoroutine())

if __name__ == '__main__':
    main()

