#               _             __  __           _       _
#     /\       | |           |  \/  |         | |     | |
#    /  \   ___| |_ _ __ ___ | \  / | ___   __| |_   _| | ___  ___
#   / /\ \ / __| __| '__/ _ \| |\/| |/ _ \ / _` | | | | |/ _ \/ __|
#  / ____ \\__ \ |_| | | (_) | |  | | (_) | (_| | |_| | |  __/\__ \
# /_/    \_\___/\__|_|  \___/|_|  |_|\___/ \__,_|\__,_|_|\___||___/
#
#               © Copyright 2022
#
#      https://t.me/Den4ikSuperOstryyPer4ik
#                      and
#             https://t.me/ToXicUse
#
#       🔒 Licensed under the GNU AGPLv3
#    https://www.gnu.org/licenses/agpl-3.0.html
#
# meta developer: @AstroModules
# meta pic: https://img.icons8.com/bubbles/500/000000/messages-mac.png
# meta banner: https://i.imgur.com/6iLFm51.jpeg
# scope: hikka_only
# scope: inline
# scope: hikka_min 1.3.0

from .. import loader
from ..inline.types import InlineCall

import random
import requests
import logging
from bs4 import BeautifulSoup
import grapheme

from telethon.tl.types import Message
from telethon.tl.functions.account import UpdateProfileRequest

logger = logging.getLogger(__name__)


@loader.tds
class RandomStatusesMod(loader.Module):
    '''Рандомные статусы для описания аккаунта в ТГ/Вацап/ВК и т.д.'''

    strings = {
        "name": "RandomStatuses",
        "generate_st": "✨ Рандомный статус 🌺",
        "support_chat_btn": "🎩 Чат поддержки 🎓",
        "more_modules_btn": "🌌 Больше Модулей ✨",
        "set_status": "⚙️ Сохранить в био 📥",
    }

    @loader.command()
    async def rstatuscmd(self, message: Message):
        """Рандомный статус на описание аккаунта в ТГ/ВК/Вацап и т.д."""
        await self.inline.form(
            text="Привет! Нажми кнопку ниже, чтобы получить рандомный статус!",
            reply_markup=[
                [{"text": self.strings("generate_st"), "callback": self.random_status}],
                [
                    {
                        "text": self.strings("support_chat_btn"),
                        "url": "https://t.me/AstroModulesChat",
                    }
                ],
                [
                    {
                        "text": self.strings("more_modules_btn"),
                        "url": "https://t.me/AstroModules",
                    }
                ],
                [{"text": "🚫 Закрыть", "action": "close"}],
            ],
            message=message,
        )

    async def client_ready(self, client, db):
        logger.info("Привет от t.me/AstroModules :)")

    async def random_status(self, call: InlineCall):
        q = ["list", "parser"]
        rand1 = random.choice(q)
        if rand1 == "list":
            statuses = [
                "Расходовать оптимизм нужно умеренно, чтобы хватило до конца жизни",
                "Когда кажется что в жизни все рушится, начинайте думать о том, что"
                " построите на освободившемся месте",
                "Ребенок — гость в твоем доме - накорми, выучи и отпусти",
                "Чем меньше ты будешь задавать вопросов, тем меньше ты услышишь лжи",
                "Побеждающий других силен, а побеждающий самого себя могуществен",
                "Никогда не знаешь, что придёт завтра — следующее утро или следующая"
                " жизнь",
                "Дни жизни даже горькие цени, ведь навсегда уходят и они",
                "Тот кто хранит молчанье в шумных спорах, мудрее болтунов, на слово"
                " скорых",
                "Дурак спорит с каждым, умный — с равным, а мудрый — лишь с самим"
                " собой",
                "Лучше прожить день львом, чем сто лет овцой.",
                "Гости, как рыба: через три дня воняют",
                "Хорошее употребление времени делает время ещё более драгоценным, будь"
                " счастлив в этот миг, этот миг и есть твоя жизнь.",
                "Великие дела нужно совершать, а не бесконечно обдумывать",
                "Счастье — это когда ты нашёл человека, который искал тебя",
                "Преодолевая трудности, мы приобретаем мудрость",
                "Не огорчайся по поводу того, чего у тебя нет. Радуйся по поводу того,"
                " что у тебя есть",
                "Хочешь узнать человека? Тогда задень его. Человек — это сосуд. Чем"
                " наполнен, то и начнёт выплёскиваться",
                "Нажить много денег — храбрость. Сохранить их — мудрость. Умело"
                " расходовать — искусство",
                "Слабые мстят, сильные прощают, счастливые забывают",
                "Бога мы сердим нашими грехами, людей — достоинствами",
                "Пусть о нас говорят плохо. А мы будем делать хорошо.",
                "Мудр не тот, кто знает много, а тот, чьи знания полезны",
                "Оставь мутную воду в покое — и она станет чистой",
                "Шипы из сердца может вытащить только друг",
                "Кто после трёх шагов начал жалеть что пошёл в гору, тот не поднимется"
                " и на маленький холм",
                "Ночь - время дел мировой важности",
                "Я как кабриолет, такая классная, а крыши нет…",
                "Рай был переполнен… Я вернулся!",
                "Не бойся медлить, бойся остановиться",
                "То что случается, случается вовремя",
                "Тот, кто хорош для всех, для всех и плох",
                "Родившийся ослом не умрёт лошадью",
                "Никто не спотыкается лёжа в постели",
                "Победа над слабым подобна поражению",
                "Лучше хранить тот секрет, который никому не раскрыт",
                "Неспешная старость — залог долголетия",
                "Много обещаний уменьшают доверие",
                "Никто не хочет быть одиноким, даже в раю",
                "Никто не возвращался из путешествий таким, каким он был раньше",
                "Забытая мысль всегда кажется важной",
                "Сон не спасёт тебя, если у тебя устала душа",
                "Будь словно лотос: он цветёт даже в мутной воде",
                "Дающий нищему не обеднеет",
                "Заботься о себе, но не забудь оставить что-нибудь потомкам",
                "Человек без воли что нож без стали",
                "Когда ваши дела идут плохо — не ходите за ними",
                "Если хочешь увидеть радугу, будь готов попасть под дождь",
                "Хорошие друзья достаются тому кто сам умеет быть хорошим другом",
                "Бог дал тебе лицо, но тебе выбирать его выражение",
                "Люди не хотят быть богатыми — люди хотят быть богаче других",
                "Утром когда восходит солнце позвольте ему взойти и в вас тоже",
                "Твой дом там, где спокойны твои мысли",
                "Горе, как рваное платье, надо оставлять дома",
                "Как басня так и жизнь — ценится не за длину, но за содержание",
                "Победа показывает, что человек может, а поражение — чего он стоит",
                "Сильный преодолевает преграду. Мудрый — весь путь",
                "Если ты ненавидишь — значит тебя победили",
                "Если ты не признаешь свою ошибку, значит, ты совершаешь вторую",
                "Возлюбите врагов своив и они сойдут с ума, пытаясь понять, что вы"
                " задумали",
                "Сильные люди говорят в лицо, слабые люди — за спиной",
                "Тихие речи мудрых слышнее крика властелина глупцов",
                "Когда человеку кажется что все идет наперекосяк, в его жизнь пытается"
                " войти нечто чудесное",
                "Почему с точки зрения законов аэродинамики шмель летать не способен,"
                " но он этого не знает и продолжает летать",
                "Человек, который смог сдвинуть гору, начинал с того, что перетаскивал"
                " с места на место мелкие камешки",
                "Как бы сильно не дул ветер, гора перед ним не склонится",
                "Не жалей о своих ошибках, ведь не сделав их, ты никогда не узнаешь,"
                " как делать правильно",
                "Бриллиант упавший в грязь так и останется бриллиантом, а пыль"
                " поднявшаяся до небес, так и остаётся пылью",
                "Мудрый человек помнит своих друзей всегда, а глупец — только когда"
                " нуждается в них",
                "Кто малым недоволен, тот большего не достоин",
                "Лучше спросить и выглядеть глупым в течении нескольких минут, чем"
                " промолчать и оставаться им всю жизнь",
                "Высшая наука: быть мудрым, а высшая мудрость: быть добрым",
                "Если не хочешь, чтобы враг раскрыл твою тайну, то не открывай её даже"
                " другу",
                "Для того, чтобы услышать себя, нужны молчаливые дни",
                "Стремись к мудрости, а не к знаниям. Знания — это прошлое, а мудрость"
                " — это будущее",
                "Ты хозяин своих слов, пока не высказал их. Когда же их высказал то они"
                " — твои хозяева",
                "Не суди чужое прошлое, не зная своего будущего",
                "Враг опасен, когда кажется побеждённым",
                "Иди против ветра и пусть тебе плюют в спину",
                "Прежде чем любить, научись ходить по снегу, не оставляя следов",
                "Хижина, где смеются, богаче дворца, где скучают",
                "Если вы уходите и вас никто не зовет обратно — вы идёте в верном"
                " направлении",
                "Верить людям не сложно, сложно поверить заново",
                "Если ты споткнулся и упал, это ещё не значит, что ты идёшь не туда",
                "Оскорбить женщину может только униженный судьбой мужчина",
                "Чтобы победить противника, не стремись стать сильнее его, а сделай его"
                " слабее себя",
                "Советы мы принимаем каплями, зато даём вёдрами",
                "Хочешь победить врага — воспитай его детей",
                "Чтобы получить знания — нужна мудрость. Чтобы получить мудрость —"
                " нужно наблюдать",
                "Не гонись за счастьем — оно всегда в тебе",
                "Помни, что бы ты не делал за спиной у людей, ты делаешь это на глазах"
                " у Бога.",
                """Часто мы говорим «Не люблю», а в душе у нас текут слёзы. 
                Часто мы говорим «Ненавижу» только для того, чтобы мы сами поверили в это. 
                Часто мы говорим «Прощай» в надежде увидеть человека ещё раз. 
                Мы говорим «Уйди», чтобы человек не видел наших слёз. 
                Мы говорим «Никогда», когда знаем, что это случится вновь. 
                Мы говорим «Разлюбил(а)»когда боимся признаться в своих чувствах. 
                Мы говорим «Я тебя забыл(а)» когда мысль о человеке не выходит из головы. 
                Мы говорим «Я удалила его(ее) номер» когда помним его наизусть. 
                Мы говорим «Между нами все кончено» когда все только начинается. 
                Иногда мы не можем сказать «Люблю» когда боимся услышать ответ. 
                Мы просим чтобы нас «Оставили одних», когда нуждаемся в чьей-то поддержке. 
                Мы «Надеемся», когда нет никаких шансов. 
                Мы «Ждём», когда знаем, что о нас уже забыли. 
                Мы «Мечтаем» зная, что это никогда не случится.....""",
                "Я буду тянуться туда, где меня ждут, но останусь там, где меня ценят!",
                "Когда появляются парни, исчезают подруги… Даже самые лучшие…",
                "С некоторыми людьми встреча в этой жизни была лишней.",
                "Настоящая подруга — это не телочка, которая вытирает твои сопли, когда"
                " тебя бросил мальчик. Настоящая подруга — это та, кто искренне рада"
                " видеть тебя красивой!",
                "Вернется тот, кто сильно любит. Дождется тот, кто сильно ждет.",
                "Я и не стремлюсь быть идеальной,мне нравится всех раздражать.",
                "Твоя подруга забыла о тебе и у неё появился парень? Поставь статус"
                " «Чёрт! Кажется, я влюбилась в парня лучшей подруги…»",
                "лучшая подруга это та которая за тебя заступится! потом отведёт в"
                " сторонку и скажет что ты была не права!",
                "Иногда так хочется немного вернуть время назад и исправить те ошибки,"
                " которые были допущены раньше",
            ]
            self.mn = random.choice(statuses)
        elif rand1 == "parser":
            urls = [f"https://status69.ru/page/{i}" for i in range(2, 96 + 1)]
            url = random.choice(urls)
            request = requests.get(url)
            soup = BeautifulSoup(request.text, "html.parser")
            nm = soup.find_all("div", class_="entry")
            f = random.choice(nm)
            self.mn = f.find("p").text

        emoji = list(grapheme.graphemes("🍇🍉🥝🥑🥥🍓🍍🎆🎇✨🎊🎉🎈🎁🎀🏆🌋📱🆒️🦄🐾🍟🍔🧀🍕🌭🥪🎂🍫🍬🍭🥧🍮🍡🥟🍥☕️🍹🥂🍺🍪"))

        emoj = random.choice(emoji)

        rst = (
            f"<b>{emoj} Ваш новый рандомный статус на"
            f' сегодня:</b>\n"<code>{self.mn}</code>"'
        )
        await call.edit(
            f"{rst}",
            reply_markup=[
                [{"text": self.strings("generate_st"), "callback": self.random_status}],
                [{"text": self.strings("set_status"), "callback": self.set_status}],
                [
                    {
                        "text": self.strings("support_chat_btn"),
                        "url": "https://t.me/AstroModulesChat",
                    }
                ],
                [
                    {
                        "text": self.strings("more_modules_btn"),
                        "url": "https://t.me/AstroModules",
                    }
                ],
                [{"text": "🚫 Закрыть ", "action": "close"}],
            ],
        )

    async def set_status(self, call: InlineCall):
        await self.client(UpdateProfileRequest(about=self.mn))
        await call.edit(
            f"Био(Обо мне в профиле) изменено успешно на:\n«<code>{self.mn}</code>»",
            reply_markup=[
                [{"text": self.strings("generate_st"), "callback": self.random_status}],
                [
                    {
                        "text": self.strings("support_chat_btn"),
                        "url": "https://t.me/AstroModulesChat",
                    }
                ],
                [
                    {
                        "text": self.strings("more_modules_btn"),
                        "url": "https://t.me/AstroModules",
                    }
                ],
                [{"text": "🚫 Закрыть ", "action": "close"}],
            ],
        )
