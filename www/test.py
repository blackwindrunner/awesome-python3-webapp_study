import asyncio,logging,os
import orm
from models import User, Blog, Comment
async def test(loop):

    await orm.create_pool(loop=loop, user='www-data', password='www-data',db='awesome')
    u = User(name='Test', email='14@example.com', passwd='1234567890', image='about:blank')

    await u.save()
    await orm.close_pool()


FILE = os.getcwd()
logging.basicConfig(filename=os.path.join(FILE, 'log.txt'), level=logging.DEBUG)



loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()