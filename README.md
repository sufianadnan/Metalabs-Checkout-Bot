# Metalabs-Checkout-Bot (Outdated)

## Disclaimer
***Please Note: These scripts are outdated and no longer functional. They were created for a specific purpose and may not work with the current versions of web applications or libraries. It's recommended to consult the official documentation and update the code accordingly if you intend to use automation for similar tasks with current web applications. The Company MetaLabs no longer exists. They are provided here for reference purposes only.***

---

## Freemeta: Automated Meta Checkout for free checkouts

### Description
This script was designed to automate the login process for a website using Selenium and Chrome WebDriver. It takes user input for a password and uses predefined elements and XPaths to fill in email and name fields before clicking the checkout button.

### Dependencies
- Selenium
- Chrome WebDriver
- A `config` module containing necessary keys

### Usage
1. Run the script.
2. Enter the checkout password once dropped.
3. The script will navigate to the product purchase page and attempt to complete the purchase process.

### Example Usage
```python
python freemeta.py
```

## Paidmeta: Automated Paid Product Purchase
### Description
This script was intended for automating the purchase process of a product on a website. It uses Selenium and Chrome WebDriver for headless browsing, fills in email and name fields, and completes the payment process by simulating keyboard input for card information, CVV, and zip code.


