# import aiohttp
# import asyncio
# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text(), response.status
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         html, status = await fetch(session, 'https://cuiqingcai.com')
#         print(f'html: {html[:100]}...')
#         print(f'status: {status}')
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())


# asyncio 的 Semaphore 来控制并发量
# CONCURRENCY = 5
# URL = 'https://www.baidu.com'
# semaphore = asyncio.Semaphore(CONCURRENCY)
# session = None
# async def scrape_api():
#     async with semaphore:
#         print('scraping', URL)
#         async with session.get(URL) as response:
#             await asyncio.sleep(1)
#             return await response.text()
#
# async def main():
#     global session
#     session = aiohttp.ClientSession()
#     scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(10000)]
#     await asyncio.gather(*scrape_index_tasks)
#
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(main())



import asyncio
import aiohttp
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

INDEX_URL = 'https://dynamic5.scrape.cuiqingcai.com/api/book/?limit=18&offset={offset}'
DETAIL_URL = 'https://dynamic5.scrape.cuiqingcai.com/api/book/{id}'
PAGE_SIZE = 18
PAGE_NUMBER = 100
CONCURRENCY = 5

semaphore = asyncio.Semaphore(CONCURRENCY)
session = None
async def scrape_api(url):
    async with semaphore:
        try:
            logging.info('scraping %s', url)
            async with session.get(url) as response:
                return await response.json()
        except aiohttp.ClientError:
            logging.error('error occurred while scraping %s', url, exc_info=True)

async def scrape_index(page):
    url = INDEX_URL.format(offset=PAGE_SIZE * (page-1))
    return await scrape_api(url)


from motor.motor_asyncio import AsyncIOMotorClient
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'books'
MONGO_COLLECTION_NAME = 'books'
client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

async def save_data(data):
    logging.info('saving data %s', data)
    if data:
        return await collection.update_one({
            'id': data.get('id')
        }, {
            '$set': data
        }, upsert=True)

async def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    data = await scrape_api(url)
    await save_data(data)

import json
async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, PAGE_NUMBER + 1)]
    results = await asyncio.gather(*scrape_index_tasks)
    logging.info('results %s', json.dumps(results, ensure_ascii=False, indent=2))
    ids = []
    for index_data in results:
        if not index_data: continue
        for item in index_data.get('results'):
            ids.append(item.get('id'))

    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in ids]
    await asyncio.wait(scrape_detail_tasks)
    await session.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())