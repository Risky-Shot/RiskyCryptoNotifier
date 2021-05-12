# Risky Crypto Notifier

## USAGE : 

If you don't already have Python and do not know how to set it up, instructions are at the bottom. It's not complicated at all and takes literally 5 minutes. Please do that and come back here.

Download this code as zip, and extract it to some folder like `C:\temp\RiskyCryptoNotifier`. Going by this structure, the py files should be in `C:\temp\RiskyCryptoNotifier`.

Open command prompt and run cd `C:\temp\RiskyCryptoNotifier`

Install all the dependencies with the below. This is a one-time activity (for anyone not familiar with Python)

```sh
pip install -r requirements.txt
```
Change `owned_coins` value in `config.py` with your invested amount of coins

Finally, run the script file as shown below:

```sh
python application.py
```

You can make changes in `config.py` for other crypto currencies, different localizations 

## Python 3.7.3 Installation in Windows

* Check if Python is already installed by opening command prompt and running `python --version`.
* If the above command returns `Python <some-version-number>` you're probably good - provided version number is above 3.6
* If Python's not installed, command would say something like: `'python' is not recognized as an internal or external command, operable program or batch file`.
* If so, download the installer from: https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe
* Run that. In the first screen of installer, there will be an option at the bottom to "Add Python 3.7 to Path". Make sure to select it.
* Open command prompt and run `python --version`. If everything went well it should say `Python 3.7.3`
* You're all set!

## CREDITS :
API : [CoinGecko](https://www.coingecko.com)
