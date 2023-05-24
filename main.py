import ccxt
import time
from dotenv import load_dotenv

load_dotenv()

exchange = ccxt.binance({
    'apiKey': 'Ваш_API_KEY',
    'secret': 'Ваш_SECRET_KEY',
    'enableRateLimit': True,
})

dict_binace = {
   "volume": 10000.0,  # Объем в долларах
   "number": 5,  # На сколько ордеров нужно разбить этот объем
   "amountDif": 50.0,  # Разброс в долларах, в пределах которого случайным образом выбирается объем в верхнюю и нижнюю сторону
   "side": "SELL",  # Сторона торговли (SELL или BUY)
   "priceMin": 200.0,  # Нижний диапазон цены, в пределах которого нужно случайным образом выбрать цену
   "priceMax": 300.0  # Верхний диапазон цены, в пределах которого нужно случайным образом выбрать цену
}
def order_f():

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
