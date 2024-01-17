from aiogram import I18nMiddleware
from aiogram import types

from bot.config import Config
from bot.src.database.users import get_user_locale_or_none


class ACLMiddleware(I18nMiddleware):
    default_language_code = 'ru'

    # Каждый раз, когда нужно узнать язык пользователя - выполняется эта функция
    async def get_user_locale(self, action, args):
        user = types.User.get_current()

        lang_code = None
        if user:
            lang_code = get_user_locale_or_none(user.id)

        # Возвращаем язык из базы, если он есть
        if lang_code:
            return lang_code
        # Иначе язык из телеграма
        elif user and user.locale:
            return lang_code
        # Иначе дефолтный
        else:
            return self.default_language_code

    def change_locale_context(self, lang_code: str):
        if lang_code not in self.available_locales:
            return
        self.ctx_locale.set(lang_code)


def setup_middleware(dp):
    # Устанавливаем миддлварь
    i18n = ACLMiddleware(Config.I18N_DOMAIN, Config.LOCALES_DIR, default='ru')
    dp.middleware.setup(i18n)
    return i18n