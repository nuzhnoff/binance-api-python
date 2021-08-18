from binance import Client
#временно вынес секретные ключи в отдельный файла
import config_binance_api
#TODO Необходимо разобраться с модулем configparser
'''import configparser
# Загрузка ключей из файла config
config = configparser.ConfigParser()
config.read_file(open('home/files-notes/config-binance-api.cfg'))
api_key = config.get('BINANCE', 'actual_api_key')
secret_key = config.get('BINANCE', 'actual_secret_key')'''
config_binance_api.init()
api_key = config_binance_api.actual_api_key
api_secret = config_binance_api.actual_secret_key
client = Client(api_key, api_secret)
candles = client.get_all_tickers()
print(candles)
