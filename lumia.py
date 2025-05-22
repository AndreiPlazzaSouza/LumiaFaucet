import asyncio
from pyppeteer import launch

async def claim_lumia(wallet_address):
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto('https://www.alchemy.com/faucets/lumia-testnetwith', {'waitUntil': 'networkidle2'})

    # Wait for the wallet address input field and enter wallet address
    await page.waitForSelector('input[type="text"]')
    await page.type('input[type="text"]', wallet_address)

    # Wait and click the "Send Me Tokens" button (update selector if needed)
    await page.waitForSelector('button[type="submit"]')
    await page.click('button[type="submit"]')

    # Wait for a while to allow the transaction to process
    await page.waitFor(5000)
    await browser.close()

if __name__ == '__main__':
    # Replace with your Lumia testnet wallet address
    wallet_address = '0xYourLumiaTestnetAddressHere'
    asyncio.get_event_loop().run_until_complete(claim_lumia(wallet_address))
