# Task 3 client
# Echo server with asyncio
# Create a socket echo server which handles each connection using asyncio Tasks.

import asyncio

async def send_message(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Closing the connection')
    writer.close()
    await writer.wait_closed()

async def main():
    message = "Hello, server!"
    await send_message(message)

if __name__ == '__main__':
    asyncio.run(main())
