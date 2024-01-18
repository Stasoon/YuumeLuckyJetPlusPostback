from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from config import Config
from src.database.users import get_user_locale_or_none


class ACLMiddleware(I18nMiddleware):
    default_language_code = 'ru'

    async def get_user_locale(self, action, args):
        user = types.User.get_current()

        lang_code = None
        if user:
            lang_code = get_user_locale_or_none(user.id)

        if lang_code:
            return lang_code
        elif user and user.locale:
            return lang_code
        else:
            return self.default_language_code

    def change_locale_context(self, lang_code: str):
        if lang_code not in self.available_locales:
            return
        self.ctx_locale.set(lang_code)


def setup_middleware(dp):
    # Инициализируем механизм локализации
    i18n = ACLMiddleware(Config.I18N_DOMAIN, Config.LOCALES_DIR, default='ru')

    # Устанавливаем миддлварь
    dp.middleware.setup(i18n)
    return i18n
