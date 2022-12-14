from aiogram.types import InlineKeyboardMarkup, inline_keyboard, InlineKeyboardButton


choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Русский",
                                          callback_data='Ru'
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="English",
                                          callback_data='Eng'
                                      )
                                  ]
                              ])