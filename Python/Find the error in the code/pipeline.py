# Contributor: Jeffrey Romero
# Date: 2/10/2021

# FIXED
# - Improper indentation on lines 12, 15, 16, 17
# - os module was not imported
# - datetime module was not imported
# - "start" variable is not in correct scope
# - "time_elapsed" was calculated incorrectly - was originally (start - end)
# - Debug prints did not follow consistent code style

import asyncio
import logging
import os
from datetime import datetime # Program will access the datetime class from the datetime module

logger = logging.getLogger(__name__)
# Uncomment line below to get debug log
# logger.basicConfig(filename="debug.log", level=logging.DEBUG)
SLEEP_DURATION = os.getenv("SLEEP_DURATION")

class Pipeline:
    start = datetime.now() # Get current date and time now to keep "start" in scope
    async def __init__(*args, **kwargs): 
        default_sleep_duration = kwargs["default_sleep_duration"]
    async def sleep_for(coro, sleep_duration, *args, **kwargs): 
        asyncio.sleep(sleep_duration)
        logger.debug(f"Slept for {sleep_duration} seconds")        
        start = datetime.now()
        await coro(*args, **kwarg) 
    end = datetime.now()
    time_elapsed = (end - start).total_seconds()
    logger.debug(f"Executed the coroutine for {time_elapsed} seconds")
