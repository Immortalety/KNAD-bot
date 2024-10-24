cat_names = [
    "Абрикос", "Авдей", "Аввакум", "Август", "Аверий", "Агафон", "Агафий", "Адам", "Адонис", "Адольф",
    "Адриан", "Азур", "Азазель", "Айзик", "Айдамир", "Айленд", "Акела", "Актавиан", "Аладдин", "Алмаз",
    "Али", "Алекс", "Альф", "Альфред", "Амадей", "Амур", "Ангел", "Антоний", "Аполлон", "Арчи", "Арамис",
    "Артур", "Аслан", "Астерикс", "Атаман", "Атилла", "Афоня", "Ахиллес", "Ашот",

    "Баритон", "Барбарис", "Бамбино", "Бандит", "Бармалей", "Барон", "Бантик", "Басик", "Бахус", "Барри",
    "Барни", "Бегемот", "Бетховен", "Билли", "Бишон", "Блум", "Блэк", "Богатырь", "Бодя", "Боксик",
    "Бостон", "Босс", "Болли", "Бобо", "Бонифаций", "Боня", "Бонапарт", "Бонд", "Борис", "Боцман",
    "Братан", "Браин", "Брэйв", "Брут", "Брэд", "Бусик", "Бука", "Бэмби", "Бэд",

    "Вагнер", "Вагабонд", "Валентин", "Варяг", "Ван Гог", "Вольдемар", "Василий", "Ватсон", "Валет",
    "Вакула", "Вампир", "Валли", "Велес", "Ветерок", "Везувий", "Версаль", "Викинг", "Винстон", "Вильям",
    "Виннер", "Вилли", "Виссарион", "Влас", "Володя", "Вурсик", "Вульф",

    "Габон", "Гай", "Гамлет", "Ганс", "Галилей", "Гарфилд", "Гарольд", "Гарри", "Гару", "Гаспар", "Гектор",
    "Генри", "Гермес", "Гелиос", "Гедонист", "Геракл", "Геркулес", "Геннадий", "Гефест", "Глазастик",
    "Гораций", "Гоген", "Голум", "Гоша", "Грегориан", "Гремлин", "Гриша", "Граф", "Гризли", "Грэй",
    "Гуляш", "Гунтер", "Гусар", "Гуччи",

    "Данила", "Дамир", "Дарий", "Дантес", "Данни", "Дасти", "Дайтон", "Дали", "Денди", "Декстер", "Денис",
    "Деймон", "Джордж", "Джин", "Джонни", "Джанни", "Джованни", "Джерри", "Джек", "Джеральд", "Дзен",
    "Диего", "Дилан", "Дик", "Дикси", "Дисней", "Дионис", "Добби", "Довлат", "Дог", "Додон", "Донжуан",
    "Добряк", "Дональд", "Дракон", "Драчун", "Дрим",

    "Евграф", "Евлампий", "Евстафий", "Евсей", "Евгений", "Егерь", "Елисей", "Елоша", "Емеля", "Енисей",
    "Енот", "Епифаний", "Ерофей", "Ермак", "Ерёма", "Ермолай", "Есенин", "Есаул", "Ефим", "Ефрем", "Еша",

    "Жак", "Жакки", "Жан", "Жанвьер", "Жангир", "Жасмин", "Жалимар", "Жармен", "Жерар", "Желток", "Жером",
    "Жермен", "Живчик", "Жирок", "Жозе", "Жозеф", "Жорик", "Жорж", "Жук", "Жулик", "Жульен", "Жужу",
    "Жучок",

    "Зак", "Захар", "Завьял", "Забияка", "Звоночек", "Зверь", "Звездочет", "Звонкий", "Зевс", "Зенит",
    "Зеро", "Зефир", "Зингер", "Зигфрид", "Зигмунд", "Зил", "Зизи", "Златан", "Златоуст", "Знахарь",
    "Зодиак", "Зорро", "Зонтик", "Зож", "Зулейман", "Зулик",

    "Иван", "Иванеус", "Ивашка", "Иврит", "Игнат", "Игорь", "Изюм", "Изя", "Икар", "Илларион", "Илья",
    "Иннокентий", "Индус", "Иной", "Иосиф", "Иолай", "Ирис", "Ирвин", "Ираклий", "Ирод", "Иртыш", "Иса",
    "Искандер", "Исмаил",

    "Йосик", "Йошка", "Йен",

    "Кавалер", "Казанова", "Казак", "Казбек", "Казимир", "Каир", "Калигула", "Кальмар", "Капитон", "Карабас",
    "Кардинал", "Карл", "Карен", "Карлос", "Каспер", "Касьян", "Кашалот", "Каштан", "Квентин", "Кексик",
    "Кент", "Кенни", "Кен", "Кенди", "Кентавр", "Керосин", "Кеша", "Кинг", "Кир", "Киплинг", "Клавдий",
    "Клаудио", "Клаус", "Клусик", "Князь", "Ковбой", "Кокос", "Командир", "Конан", "Коньяк", "Коперник",
    "Кореш", "Корсар", "Король", "Космос", "Кося", "Котя", "Котопес", "Котяо", "Крис", "Кристал", "Кроша",
    "Кронос", "Крэг", "Кристофер", "Ксавье", "Ксандер", "Кубик", "Кузьма", "Купидон", "Курт", "Кэт", "Кэнди",

    "Ладик", "Лаки", "Лакмус", "Ламар", "Ларри", "Ластик", "Лебовски", "Лев", "Леван", "Лео", "Леон",
    "Леопольд", "Лексус", "Леший", "Лёшка", "Лизун", "Лидер", "Лион", "Листик", "Лилу", "Лобстер",
    "Ловелас", "Ломтик", "Лорд", "Лотос", "Луис", "Луиджи", "Лукас", "Лунтик", "Любик", "Люис", "Люциус",
    "Лямур",

    "Магомет", "Мажор", "Майкл", "Малыш", "Максик", "Мамай", "Манфред", "Мао", "Марчелло", "Марсик",
    "Маркиз", "Мартин", "Матвей", "Маурицио", "Мартын", "Маус", "Мачо", "Мерлин", "Микки", "Милки",
    "Милан", "Минор", "Мирон", "Миф", "Микель", "Миха", "Модест", "Монстр", "Монтана", "Монсеньор",
    "Моисей", "Морзик", "Моцарт", "Мрак", "Мстислав", "Мурка", "Мускат", "Мук", "Мурад", "Мусор", "Муслин",
    "Муфаса", "Мухтар",

    "Назар", "Наоми", "Нарцисс", "Насир", "Натан", "Нарцисс", "Нейтан", "Нерон", "Ник", "Ника", "Николай",
    "Никсон", "Нильс", "Нистас", "Норд", "Нуар", "Нюша"
]