
# LumiaFaucet

**LumiaFaucet** is a Python automation tool for claiming tokens from the [Alchemy Lumia Testnet Faucet](https://www.alchemy.com/faucets/lumia-testnetwith).  
It uses browser automation to interact with the faucet page, making it easy to schedule regular claims for development and testing.

---

## Features

- Automates Lumia Testnet token claims from the Alchemy Faucet
- Runs headlessly for efficient, unattended operation
- Easy to schedule with cronjob or task scheduler
- Written in Python for easy customization

---

## Requirements

- Python 3.7+
- [pyppeteer](https://github.com/pyppeteer/pyppeteer) (browser automation)

Install dependencies:
```bash
pip install pyppeteer
```

---

## Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/AndreiPlazzaSouza/LumiaFaucet.git
    cd LumiaFaucet
    ```

2. **Edit the script:**
    - Open `lumia.py`
    - Replace `'0xYourLumiaTestnetAddressHere'` with your Lumia testnet wallet address.

3. **Run the script:**
    ```bash
    python lumia.py
    ```

---

## Scheduling with Cronjob

To automate claims, add a cronjob entry (Linux/macOS):

```cron
0 2 * * * /usr/bin/python3 /path/to/LumiaFaucet/lumia.py
```
This example runs the script every day at 2:00 AM.

---

## Example Script

```python
import asyncio
from pyppeteer import launch

async def claim_lumia(wallet_address):
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto('https://www.alchemy.com/faucets/lumia-testnetwith', {'waitUntil': 'networkidle2'})
    await page.waitForSelector('input[type="text"]')
    await page.type('input[type="text"]', wallet_address)
    await page.waitForSelector('button[type="submit"]')
    await page.click('button[type="submit"]')
    await page.waitFor(5000)
    await browser.close()

if __name__ == '__main__':
    wallet_address = '0xYourLumiaTestnetAddressHere'
    asyncio.get_event_loop().run_until_complete(claim_lumia(wallet_address))
```

---

## Notes

- **Selectors may need adjustment:** If the faucet page changes, update the input and button selectors in the script.
- **CAPTCHA Handling:** The script cannot bypass CAPTCHAs. Manual intervention may be required.
- **Respect faucet rules:** Do not abuse the faucet. Use only for testnet and development purposes.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---
