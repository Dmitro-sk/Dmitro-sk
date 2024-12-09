import telebot
from telebot import types

token = "7423715991:AAGP-mqLjGSjW91ENcQcVrre3NYR7nihNfM"
bot = telebot.TeleBot(token)

# Список ігор
games = [
    {"name": "The Witcher 3", "genre": "RPG", "platform": "PC", "description": "Фентезійна рольова гра."},
    {"name": "Cyberpunk 2077", "genre": "RPG", "platform": "PC", "description": "Гра у стилі кіберпанку."},
    {"name": "Minecraft", "genre": "Sandbox", "platform": "PC, Mobile", "description": "Гра-пісочниця для творчості."},
    {"name": "Among Us", "genre": "Party", "platform": "PC, Mobile", "description": "Гра про пошук зрадника в команді."},
    {"name": "DOOM Eternal", "genre": "Shooter", "platform": "PC", "description": "Динамічний шутер."},
    {"name": "Stardew Valley", "genre": "Simulation", "platform": "PC, Mobile", "description": "Фермерський симулятор."},
    {"name": "Hollow Knight", "genre": "Metroidvania", "platform": "PC", "description": "Атмосферна пригодницька гра."},
    {"name": "Terraria", "genre": "Sandbox", "platform": "PC, Mobile", "description": "Пісочниця з елементами виживання."},
    {"name": "Portal 2", "genre": "Puzzle", "platform": "PC", "description": "Гра-головоломка з фізичними задачами."},
    {"name": "Celeste", "genre": "Platformer", "platform": "PC", "description": "Платформер про подолання труднощів."},
    {"name": "Clash of Clans", "genre": "Strategy", "platform": "Mobile", "description": "Популярна стратегічна гра."},
    {"name": "PUBG Mobile", "genre": "Battle Royale", "platform": "Mobile", "description": "Королівська битва на мобільних."},
    {"name": "Genshin Impact", "genre": "RPG", "platform": "PC, Mobile", "description": "Популярна RPG-гра з відкритим світом."},
]

# Словник для збереження вибору платформи користувачем
user_platform_choice = {}

# Команда /start або /help
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pc_button = types.KeyboardButton("ПК")
    mobile_button = types.KeyboardButton("Мобільний телефон")
    both_button = types.KeyboardButton("Обидві платформи")
    markup.add(pc_button, mobile_button, both_button)
    bot.reply_to(
        message,
        "Привіт! Я бот для пошуку ігор. Оберіть платформу, для якої ви хочете знайти ігри:",
        reply_markup=markup,
    )

# Відправка списку жанрів
def send_genres(chat_id):
    genres_list = (
        "Ось приклади популярних жанрів ігор:\n\n"
        "🎭 **RPG (Role-Playing Game)** – Рольові ігри (The Witcher 3, Cyberpunk 2077)\n"
        "🔫 **Shooter** – Шутери (DOOM Eternal, Call of Duty)\n"
        "🎨 **Sandbox** – Пісочниці (Minecraft, Terraria)\n"
        "🚜 **Simulation** – Симулятори (Stardew Valley, The Sims)\n"
        "🧠 **Puzzle** – Головоломки (Portal 2, Tetris)\n"
        "🏰 **Strategy** – Стратегії (Clash of Clans, Age of Empires)\n"
        "🎉 **Party** – Вечіркові ігри (Among Us, Overcooked)\n"
        "🏆 **Battle Royale** – Королівські битви (PUBG Mobile, Fortnite)\n"
        "🎮 **Platformer** – Платформери (Celeste, Super Mario Bros)\n"
        "👾 **Metroidvania** – Метроїдвейнії (Hollow Knight, Ori and the Blind Forest)"
    )
    bot.send_message(chat_id, genres_list, parse_mode="Markdown")

# Обробка вибору платформи
@bot.message_handler(func=lambda message: message.text in ["ПК", "Мобільний телефон", "Обидві платформи"])
def platform_selection(message):
    user_platform_choice[message.chat.id] = message.text
    bot.reply_to(
        message,
        "Чудово! Тепер подивіться приклади жанрів, щоб визначитися із запитом.",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    send_genres(message.chat.id)  # Показ жанрів

# Пошук ігор за назвою, жанром і платформою
@bot.message_handler(func=lambda message: message.chat.id in user_platform_choice)
def search_game(message):
    platform = user_platform_choice.get(message.chat.id)
    query = message.text.lower()
    exact_match = None
    partial_matches = []

    # Перевірка повного та часткового збігу
    for game in games:
        if platform == "Обидві платформи" or platform in game["platform"]:
            if query == game["name"].lower():
                exact_match = game
                break
            elif query in game["name"].lower() or query in game["genre"].lower():
                partial_matches.append(game)

    # Відповідь на точний збіг
    if exact_match:
        bot.reply_to(
            message,
            f"🎮 Назва: {exact_match.get('name', 'Невідомо')}\n"
            f"📚 Жанр: {exact_match.get('genre', 'Невідомо')}\n"
            f"💻 Платформа: {exact_match.get('platform', 'Невідомо')}\n"
            f"ℹ️ Опис: {exact_match.get('description', 'Опис недоступний')}"
        )
    # Відповідь на часткові збіги
    elif partial_matches:
        reply = "Знайдено кілька ігор:\n\n" + "\n\n".join(
            [
                f"🎮 Назва: {game.get('name', 'Невідомо')}\n"
                f"📚 Жанр: {game.get('genre', 'Невідомо')}\n"
                f"💻 Платформа: {game.get('platform', 'Невідомо')}\n"
                f"ℹ️ Опис: {game.get('description', 'Опис недоступний')}"
                for game in partial_matches
            ]
        )
        bot.reply_to(message, reply)
    # Відповідь, якщо збігів немає
    else:
        bot.reply_to(
            message,
            "На жаль, я не знайшов ігор за вашим запитом. Спробуйте написати інший жанр або точну назву гри. 🎮",
        )

# Обробка повідомлень, якщо платформа ще не вибрана
@bot.message_handler(func=lambda message: message.chat.id not in user_platform_choice)
def no_platform_selected(message):
    bot.reply_to(
        message,
        "Спочатку оберіть платформу: ПК, Мобільний телефон або Обидві платформи. Використовуйте команду /start, щоб почати спочатку.",
    )

# Запуск бота
print("Бот запущено! Очікування повідомлень...")
bot.polling()