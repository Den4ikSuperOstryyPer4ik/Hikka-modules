#                _             __  __           _       _                
#      /\       | |           |  \/  |         | |     | |               
#     /  \   ___| |_ _ __ ___ | \  / | ___   __| |_   _| | ___  ___      
#    / /\ \ / __| __| '__/ _ \| |\/| |/ _ \ / _` | | | | |/ _ \/ __|     
#   / ____ \\__ \ |_| | | (_) | |  | | (_) | (_| | |_| | |  __/\__ \     
#  /_/    \_\___/\__|_|  \___/|_|  |_|\___/ \__,_|\__,_|_|\___||___/     
#                                                                        
#                         © Copyright 2023                             
#                                                                        
#                https://t.me/Den4ikSuperOstryyPer4ik                    
#                              and                                       
#                      https://t.me/ToXicUse                             
#                                                                         
#                 🔒 Licensed under the GNU AGPLv3                       
#             https://www.gnu.org/licenses/agpl-3.0.html                 
#   
# meta developer: @AstroModules

from .. import loader, utils
from datetime import datetime
from datetime import timedelta

class SummerMod(loader.Module):
    '''Сколько осталось дней до лета?)'''

    strings = {'name': 'SummerTimer'}

    @loader.command()
    async def st(self, message):
        """- вывести таймер"""
        now = datetime.now()
        summer = datetime(now.year, 6, 1)

        if now.month > 6 or (now.month == 6 and now.day > 1):
            summer = datetime(now.year + 1, 6, 1)

        time_to_summer = abs(summer - now)

        await utils.answer(
            message, 
            (
                '<b><emoji document_id=6334560373387036241>🏝️</emoji> '
                f'До <u>лета</u> осталось {time_to_summer.days} дней, '
                f'{time_to_summer.seconds // 3600} часов, {time_to_summer.seconds // 60 % 60}'
                f' минут, {time_to_summer.seconds % 60} секунд.\n<b><emoji '
                'document_id=5393226077520798225>🥰</emoji> Жди лето вместе '
                'с <u>AstroModules</u></b>'
            )
        )