from aiogram.utils.callback_data import CallbackData

buy_callback = CallbackData('buy', 'item_name', 'quantity')
buys_callback = CallbackData('buys', 'item_id', 'item_name')
sell_callback = CallbackData('sell', 'item_id', 'item_name')
up_callback = CallbackData('up', 'item_id', 'item_name')
down_callback = CallbackData('down', 'item_id', 'item_name')



