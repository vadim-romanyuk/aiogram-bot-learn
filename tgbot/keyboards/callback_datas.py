from aiogram.utils.callback_data import CallbackData

buy_callback = CallbackData('buy', 'item_name', 'quantity')
buys_callback = CallbackData('buys', 'item_id')
sell_callback = CallbackData('sell', 'item_id')
up_callback = CallbackData('up', 'item_id')
down_callback = CallbackData('down', 'item_id')



