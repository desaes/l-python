import asyncio
import aiofiles
import aiohttp
import bs4
import os

async def get_links():
    links = []
    async with aiofiles.open(os.getcwd() + '/dev/l-python/general/concurrency/async/' + 'links.txt') as fd:
        async for link in fd:
            links.append(link.strip())
    return links

async def get_html(link):
    print(f'Getting html of {link}')

    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            response.raise_for_status()

            return await response.text()

def get_page_title(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    title = soup.select_one('title')
    title = title.text.split('|')[0].strip()
    return title

async def print_tiles():
    links = await get_links()
    tasks = []
    for link in links:
        tasks.append(asyncio.create_task(get_html(link)))

    for task in tasks:
        html = await task

        title = get_page_title(html)

        print(f'Course: {title}')
"""
def main():
    el = asyncio.get_event_loop()    
    links = el.run_until_complete(get_links())
    for link in links:
        print(get_page_title(el.run_until_complete(get_html(link))))
    el.close()
"""

def main():
    el = asyncio.get_event_loop()
    el.run_until_complete(print_tiles())
    el.close()

main()
