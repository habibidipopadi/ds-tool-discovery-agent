import asyncio
import time
from src.agent.crawl_all import crawl_all

INTERVAL_SECONDS = 60 * 30  # every 30 minutes

async def main():
    while True:
        print("Starting crawl cycle...")
        try:
            await crawl_all()
        except Exception as e:
            print(f"Error during crawl: {e}")
        print(f"Cycle done, sleeping {INTERVAL_SECONDS} seconds")
        await asyncio.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    asyncio.run(main())