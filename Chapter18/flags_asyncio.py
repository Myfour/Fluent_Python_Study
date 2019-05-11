import asyncio
import aiohttp
import sys
import os
from flags import BASE_URL, save_flag, show, main


@asyncio.coroutine
def get_flag(cc):
    url = f'{BASE_URL}/{cc}/{cc}.gif'
    print(
        f'< {cc} >:[yield from 1]--------------------------------------------> started'
    )
    resp = yield from aiohttp.ClientSession().get(url)
    print(
        f'< {cc} >:[yield from 1]--------------------------------------------> end'
    )
    print(
        f'< {cc} >:[yield from 2]--------------------------------------------> started'
    )
    image = yield from resp.read()
    print(
        f'< {cc} >:[yield from 2]--------------------------------------------> end'
    )
    return image


@asyncio.coroutine
def download_one(cc):
    print(
        f'< {cc} >:[download_one]--------------------------------------------> started'
    )
    image = yield from get_flag(cc)
    print(
        f'< {cc} >: return image------------------------------------------------>>'
    )
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list[:3])]
    print('to_do list have:', to_do)
    wait_coro = asyncio.wait(to_do)
    print('[asyncio.wait -------------------- started]')
    res, _ = loop.run_until_complete(wait_coro)
    print('[asyncio.wait -------------------- end]')
    loop.close()
    return len(res)


if __name__ == '__main__':
    main(download_many)
