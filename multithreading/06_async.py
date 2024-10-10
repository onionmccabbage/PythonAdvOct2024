# see https://docs.python.org/3/library/asyncio-runner.html

import asyncio

async def main():
    await asyncio.sleep(1) # block the main thread until done
    print('thread is done')

if __name__ == '__main__':
    # asyncio.run( main() ) # run the function in a thread
    with asyncio.Runner() as runner:
        runner.run(main())
        runner.run(main())
        runner.run(main())
        runner.run(main())
        runner.run(main())