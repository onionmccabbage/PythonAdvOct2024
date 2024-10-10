import asyncio

async def handle_requests(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    # we may use !r to ensure we are seeing the raw data we received
    print(f'Received {message!r} from {addr}')

    writer.close()

async def main():
    server = await asyncio.start_server(handle_requests, 'localhost', 8889)
    print('server started')
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run( main() )