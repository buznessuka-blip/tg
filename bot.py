from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters, CallbackQueryHandler
import random

TOKEN = "7876853359:AAG5nuDuuSXjKXBDHykVepqCAIVeZdqYkRk"
ADMIN_USERNAME = 280969220  # ID админа

keyboard = [
    ["Индивидуальная сессия", "Семейная терапия"],
    ["Стратегическая сессия", "Условия"],
    ["Обо мне"]
]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

session_keyboard = [
    ["🔙 Назад в меню", "📝 Оставить заявку"]
]
session_markup = ReplyKeyboardMarkup(session_keyboard, resize_keyboard=True)

applications = {}
application_counter = 1  # Счетчик заявок

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот психолог Евы Кулик выбери из меню что тебя интересует", reply_markup=markup)

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global application_counter
    text = update.message.text
    user_id = update.message.from_user.id

    if text in ["Индивидуальная сессия", "Семейная терапия", "Стратегическая сессия"]:
        if text == "Индивидуальная сессия":
            response = (
                "▫️ <b>Индивидуальная сессия — 50 мин.</b>\n\n"
                "Индивидуальная сессия на любой волнующий вас вопрос. Часто темы могут быть связаны и касаться нескольких областей жизни, можно затронуть любой интересующий аспект.\n\n"
                "<b>С чем я работаю:</b>\n"
                "• Личностный рост и развитие. Достижение целей, развитие личностных ресурсов.\n"
                "• Баланс жизненных целей. Оптимизация времени и сил.\n"
                "• Поиск себя. Предназначение.\n"
                "• Сексуальность и секс.\n"
                "• Коммуникационный коучинг.\n"
                "• Личные границы. Границы в отношениях.\n"
                "• Гармоничное развитие отношений, создание пары.\n"
                "• Семейные отношения. Работа с парой. Затяжные конфликты, острые ссоры.\n"
                "• Депрессии, низко-энергетические состояния.\n"
                "• Зависимости и пост-травматический синдром.\n\n"
                "В своей работе я использую современные и научно подтвержденные методы. Синтез психотерапевтических и коучинговых инструментов для максимально эффективной работы.\n\n"
                "Неукоснительно соблюдаю профессиональную этику и личную тайну клиента.\n\n"
                "Верю что человек может изменится здесь и сейчас. Любые сложности могут стать вашим ресурсом и потенциалом к росту и изменениям.\n\n"
                "В процессе работы обучу инструментам самопомощи."
            )
        elif text == "Семейная терапия":
            response = (
                "▫️ <b>Семейная терапия — 50 мин.</b>\n\n"
                "Семейная терапия проходит в формате парных и по необходимости индивидуальных сессий.\n"
                "Возможна медиация конфликтов в личностном поле, которая часто предотвращает эскалацию в юридическом.\n\n"
                "<b>Ключевые цели семейной терапии:</b>\n"
                "1. Улучшить коммуникацию\n"
                "2. Научиться конструктивно разрешать конфликты\n"
                "3. Укрепить эмоциональные связи и чувство принадлежности\n"
                "4. Прояснить роли, границы и ожидания\n"
                "5. Развить навыки совместного принятия решений\n"
                "6. Повысить эмпатию и взаимопонимание\n"
                "7. Снизить семейный стресс и улучшить способность к совладанию\n"
                "8. Скоординировать родительские подходы\n"
                "   • выработать единый стиль воспитания, правила и последствия\n"
                "9. Поисследовать и прекратить межпоколенческие сценарии\n"
                "10. Создать здоровые семейные ритуалы и позитивный опыт"
            )
        elif text == "Стратегическая сессия":
            response = (
                "▫️ <b>Стратегическая сессия — 50 мин.</b>\n\n"
                "Стратегическая сессия, чтобы сделать check-up кто я сейчас, где и куда иду. Осмотреться в своей жизни по всем направлениям или выбранному.\n\n"
                "<b>В ходе сессии:</b>\n"
                "• Сформулировать или обновить общее видение и цели\n"
                "• Оценить внешнюю среду и ключевые тренды\n"
                "• Диагностировать текущее состояние себя/своего бизнеса/карьерного трека\n"
                "• Определить 3–5 стратегических приоритетов на 1–3 года\n"
                "• Согласовать измеримые цели\n"
                "• Разработать дорожную карту и портфель инициатив\n"
                "• Распределить ресурсы и выявить критические зависимости\n"
                "• Определить метрики и механизм мониторинга прогресса\n"
                "• Усилить согласие и мотивацию с ключевыми фигурами на пути\n"
                "• Сформировать план коммуникации стратегии"
            )
        
        await update.message.reply_text(response, reply_markup=session_markup, parse_mode='HTML')
        context.user_data["session_type"] = text

    elif text == "Условия":
        conditions = (
            "📜 <b>Условия проведения сессий</b>\n\n"
            "⏳ Длительность — 50 минут.\n"
            "💳 Стоимость — 6000р\n\n"
            "💳 Запись по 100% предоплате, до внесения предоплаты оговоренное время за вами не забронировано.\n\n"
            "🔄 <b>Перенос или отмена:</b>\n"
            "• Если вы перенесли или отменили ранее, чем за 24 часа — предоплата сохраняется или возвращается в 100% объеме.\n"
            "• В случае отмены или переноса позже чем за 24 часа — возвращается 50% предоплаты.\n"
            "• Если вы не пришли в назначенное время без уведомления — предоплата не возвращается.\n\n"
            "📩 После внесения предоплаты вам приходит уведомление о записи и детали встречи.\n\n"
            "<b>Условия встречи:</b>\n"
            "• Мы созваниваемся в WhatsApp или Skype аудиозвонком\n"
            "• Важно иметь хороший интернет и быть хорошо слышным\n"
            "• Необходимо находиться в безопасном защищенном месте\n"
            "• В шумных местах (кафе, улица) работа затруднена\n"
            "• Рекомендуется использовать наушники\n"
            "• Приготовьте лист бумаги и ручку"
        )
        await update.message.reply_text(conditions, reply_markup=markup, parse_mode='HTML')

    elif text == "Обо мне":
        about = (
            "👩🏻‍💼 Я психолог-коуч, ведущий частную практику в Москве и онлайн по всему миру.\n\n"
            "Самопознание открывает человеку мир, в котором находится источник вдохновения жить и воплощать себя в реальности. Это большая лаборатория души, где познавая и смешивая ингредиенты своей внутренней реальности вы познаете и творите себя, self-made. Вы - главный продукт своей жизни. И важно чтобы вы были им довольны. Какой вы человек и каким хотите себя сделать.\n\n"
            "При этом решая задачи о том, как хорошо жить во внешней материальной реальности, как сбалансировать все сферы жизни, куда двигаться дальше и как во все преуспевать.\n\n"
            "Как согласовать свое внутреннее и внешнее, ничего важного не утратив, созидая это все в красивый жизненный путь.\n\n"
            "<b>Образование:</b>\n"
            "• Высшее профессиональное образование (специальность «психолог» и «преподаватель психологии») — диплом 2007 г.\n"
            "• \"Подготовка и проведение социологических и маркетинговых исследований\" 2006г.\n"
            "• Коучинг и практическое консультирование. Высшая школа практической психологии (Сочи) 2007-09гг\n"
            "• Нейропсихолог (диагностика, коррекция) НИИ цдн им Лурия 2016 г.\n"
            "• Проф переподготовка на специальность \"организационный психолог\", \"психологическое бизнес-консультирование\". - диплом 2024-25гг\n"
            "• И др обучения в сфере психологии в различных подходах.\n\n"
            "С 2007 года веду частную практику психолог-консультант."
        )
        await update.message.reply_text(about, reply_markup=markup, parse_mode='HTML')

    elif text == "🔙 Назад в меню":
        await update.message.reply_text("Вы вернулись в главное меню.", reply_markup=markup)

    elif text == "📝 Оставить заявку":
        await update.message.reply_text(
            "📩 Напишите ваше имя и удобное время для сессии. Я свяжусь с вами!"
        )
        context.user_data["awaiting_application"] = True

    elif context.user_data.get("awaiting_application"):
        session_type = context.user_data.get("session_type", "не указано")
        application_number = application_counter
        application_counter += 1
        
        user_info = (
            f"🔔 Новая заявка #{application_number}\n\n"
            f"Тип сессии: {session_type}\n"
            f"От пользователя: @{update.message.from_user.username or 'нет username'}\n"
            f"ID: {user_id}\n\n"
            f"Сообщение:\n{text}"
        )

        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("✅ Подтвердить", callback_data=f"confirm_{user_id}_{application_number}")],
            [InlineKeyboardButton("🕒 Предложить другое время", callback_data=f"reschedule_{user_id}_{application_number}")],
            [InlineKeyboardButton("❌ Отклонить", callback_data=f"cancel_{user_id}_{application_number}")]
        ])

        applications[application_number] = {
            "user_id": user_id,
            "type": session_type,
            "message": text,
            "status": "pending"
        }

        admin_message = await context.bot.send_message(
            chat_id=ADMIN_USERNAME,
            text=user_info,
            reply_markup=reply_markup
        )

        applications[application_number]["admin_message_id"] = admin_message.message_id

        await update.message.reply_text(
            "✅ Ваша заявка отправлена! Я скоро свяжусь с вами.", 
            reply_markup=markup
        )
        context.user_data.clear()

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    action, user_id, app_number = query.data.split('_')
    user_id = int(user_id)
    app_number = int(app_number)
    
    if query.from_user.id != ADMIN_USERNAME:
        await query.answer("Вы не админ!")
        return

    application = applications.get(app_number)
    if not application:
        await query.answer("Заявка не найдена!")
        return

    if action == "confirm":
        await context.bot.send_message(
            chat_id=user_id,
            text=f"🎉 Ваша заявка #{app_number} подтверждена! Жду вас в указанное время."
        )
        application["status"] = "confirmed"
        await query.edit_message_text(
            text=f"✅ Заявка #{app_number} подтверждена\n\n{query.message.text}"
        )

    elif action == "reschedule":
        await context.bot.send_message(
            chat_id=user_id,
            text=f"🕒 По заявке #{app_number}: пожалуйста, укажите удобное для вас время из предложенных вариантов:"
        )
        application["status"] = "rescheduling"
        await query.edit_message_text(
            text=f"⏳ Запрос на изменение времени для заявки #{app_number}\n\n{query.message.text}"
        )

    elif action == "cancel":
        await context.bot.send_message(
            chat_id=user_id,
            text=f"❌ Ваша заявка #{app_number} была отклонена. Пожалуйста, попробуйте выбрать другое время."
        )
        application["status"] = "canceled"
        await query.edit_message_text(
            text=f"❌ Заявка #{app_number} отклонена\n\n{query.message.text}"
        )

    await query.answer()

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
app.add_handler(CallbackQueryHandler(button_callback))

app.run_polling()
