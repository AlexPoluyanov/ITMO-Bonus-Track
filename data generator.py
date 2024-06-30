from datetime import datetime
from random import randint, choice, random
from random import randrange
from datetime import timedelta
import sys


with open('filename.txt', 'w') as f:
    print("Clear")

def log(*args):
    with open('filename.txt', 'a') as f:
        sys.stdout = f
        print(*args)
        
def log2(*args):
    with open('filename2.txt', 'a') as f:
        sys.stdout = f
        print(*args)

def create_insert(name: str, *args):
    sub = ", ".join(args)
    return log(f"\n\n\nINSERT INTO {name}({sub}) VALUES")

def random_date2():
    """
    This function will return a random datetime between two datetime 
    objects, with the time always being between 09:00 and 15:00.
    """
    # Define the date range
    start_date = datetime.strptime('6/1/2024', '%m/%d/%Y')
    end_date = datetime.strptime('6/30/2024', '%m/%d/%Y')
    
    # Generate a random date between the start and end date
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)
    
    # Define the time range (09:00 to 15:00)
    start_time = datetime.strptime('09:00', '%H:%M')
    end_time = datetime.strptime('17:00', '%H:%M')
    
    # Calculate the total number of half-hour periods between start and end time
    total_halfhours = int((end_time - start_time).total_seconds() // 1800)
    
    # Generate a random number of half-hour increments
    random_halfhours = random.randint(0, total_halfhours)
    
    # Generate the random time by adding the random number of half-hour increments
    random_time = start_time + timedelta(minutes=30 * random_halfhours)
    
    # Combine the random date and time
    final_datetime = datetime.combine(random_date, random_time.time())
    
    return final_datetime.strftime('%Y-%m-%d %H:%M')

def random_date():
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    start = datetime.strptime('1/1/2000 1:30 PM', '%m/%d/%Y %I:%M %p')
    end = datetime.strptime('12/31/2002 1:30 PM', '%m/%d/%Y %I:%M %p')
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    date = start + timedelta(seconds=random_second)
    return datetime.strftime(date, '%Y-%m-%d')
# create_insert("students", "first_name", "last_name",
#               "middle_name", "date_of_birth", "citizenship",
#               "contract", "group_id""students")





letters = ['N', 'M', 'P', 'R', 'Z']
create_insert("groups", "group_name")
group_list = ['N1101', 'N1102', 'N1103', 'N1104', 'N1105', 'N1106', 'N1107', 'N1108', 'N1201', 'N1202', 'N1203', 'N1204', 'N1205', 'N1206', 'N1301', 'N1302', 'N1303', 'N1304', 'N1305', 'N1401', 'N1402', 'N1403', 'M2101', 'M2102', 'M2103', 'M2104', 'M2105', 'M2106', 'M2107', 'M2108', 'M2109', 'M2201', 'M2202', 'M2203', 'M2204', 'M2205', 'M2206', 'M2301', 'M2302', 'M2303', 'M2304', 'M2305', 'M2401', 'P3101', 'P3102', 'P3103', 'P3104', 'P3105', 'P3106', 'P3107', 'P3108', 'P3109', 'P3110', 'P3201', 'P3202', 'P3203', 'P3204', 'P3205', 'P3301', 'P3302', 'P3303', 'P3401', 'R4101', 'R4102', 'R4103', 'R4104', 'R4105', 'R4106', 'R4107', 'R4108', 'R4109', 'R4201', 'R4202', 'R4203', 'R4204', 'R4205', 'R4301', 'R4302', 'R4303', 'R4401', 'R4402', 'Z5101', 'Z5102', 'Z5103', 'Z5104', 'Z5105', 'Z5106', 'Z5107', 'Z5108', 'Z5201', 'Z5202', 'Z5203', 'Z5204', 'Z5205', 'Z5206', 'Z5301', 'Z5302', 'Z5303', 'Z5304', 'Z5305', 'Z5401', 'Z5402', 'Z5403',  'Z5404']
for letter in letters:
    for course in range(1, 5):
        if course == 4:
            for num in range(1, randint(2, 4)):
                name = f"{letter}{letters.index(letter) + 1}{course}{num:02d}"
                group_list.append(name)
                log(f"(\'{name}\'),")
        elif course == 3:
            for num in range(1, randint(4, 6)):
                name = f"{letter}{letters.index(letter) + 1}{course}{num:02d}"
                group_list.append(name)
                log(f"(\'{name}\'),")
        elif course == 2:
            for num in range(1, randint(6, 8)):
                name = f"{letter}{letters.index(letter) + 1}{course}{num:02d}"
                group_list.append(name)
                log(f"(\'{name}\'),")
        elif course == 1:
            for num in range(1, randint(8, 11)):
                name = f"{letter}{letters.index(letter) + 1}{course}{num:02d}"
                group_list.append(name)
                log(f"(\'{name}\'),")

log(group_list)


exam_types = ['Зачёт', 'Экзамен', 'Дифференцированный зачёт']
exam_names = [['Математика', 'Экзамен'],
              ['Хранение и обработка данных', 'Зачёт'], 
              ['Английский язык', 'Зачёт'], 
              ['Физкультура', 'Зачёт'],
              ['Основы профессиональной деятельности', ''],
              ['Машинное обучение', ''],
              ['Статистика', '']]
exam_places = ['Кронверкский пр., 49, Аудитория ', 'Ломоносова, 9, Аудитория ', 'Online ZoomRoom #']
create_insert("exams", "name,type,place,date")
log2("INSERT INTO group_exams(group_id, exam_id, required) VALUES")
exam_count = 0
for num, group in enumerate(group_list):
    for i in range(random.randrange(1, 7)):
        if exam_names[i][1] != "":
            log(f"(\'{exam_names[i][0]}\', \'{exam_types[randint(1,10) % 3 ]}\', \'{exam_places[randint(1,10) % 3 ]}{randint(101, 420)}\', \'{random_date()}\'),")        
        else:
            log(f"(\'{exam_names[i][0]}\', \'{exam_types[randint(1,10) % 3 ]}\', \'{exam_places[randint(1,10) % 3 ]}{randint(101, 420)}\', \'{random_date()}\'), ")
        exam_count += 1
        log2(f"({num+1}, {exam_count}, {random.choice([True, False])}),")

male_names = ['Иван', 'Александр', 'Михаил', 'Сергей', 'Дмитрий', 'Андрей', 'Евгений', 'Артем', 'Николай', 'Павел',
              'Алексей', 'Игорь', 'Владимир', 'Денис', 'Олег', 'Георгий', 'Максим', 'Виктор', 'Юрий', 'Антон',
              'Василий', 'Вячеслав', 'Валентин', 'Геннадий', 'Тимур', 'Илья', 'Федор', 'Вадим', 'Семен',
              'Роман', 'Константин', 'Валерий', 'Борис', 'Валентин', 'Даниил', 'Руслан', 'Степан', 'Григорий',
              'Аркадий', 'Тимофей', 'Давид', 'Леонид', 'Олесь', 'Ростислав', 'Арсений', 'Савелий', 'Святослав',
              'Платон', 'Святослав', 'Марк', 'Мирон', 'Тихон', 'Дамир', 'Антонин', 'Артур', 'Глеб', 'Дмитриевич',
              'Филипп', 'Филимон', 'Георгий', 'Григорий', 'Иосиф', 'Илья', 'Иннокентий', 'Кирилл', 'Леонид',
              'Матвей', 'Михаил', 'Назар', 'Олег', 'Пётр', 'Сергей', 'Станислав', 'Филипп', 'Ярослав']

male_surnames = ['Иванов', 'Петров', 'Смирнов', 'Соколов', 'Кузнецов', 'Васильев', 'Попов', 'Семенов', 'Морозов',
                'Новиков', 'Федоров', 'Морозов', 'Козлов', 'Лебедев', 'Гаврилов', 'Захаров', 'Дмитриев', 'Калинин',
                'Баранов', 'Воробьев', 'Максимов', 'Белов', 'Кудрявцев', 'Котов', 'Сергеев', 'Завьялов', 'Тимофеев',
                'Логинов', 'Савельев', 'Панов', 'Колесников', 'Миронов', 'Романов', 'Селезнев', 'Сазонов', 'Беляков',
                'Гусев', 'Малинин', 'Лазарев', 'Исаев', 'Беляев', 'Титов', 'Игнатьев', 'Сорокин', 'Мельников',
                'Дорофеев', 'Суханов', 'Субботин', 'Суворов', 'Капустин', 'Филатов', 'Лукин', 'Тимошин', 'Мартынов',
                'Ефимов', 'Фролов', 'Цветков', 'Денисов', 'Ткачев', 'Донцов', 'Королев', 'Третьяков', 'Кулаков',
                'Абрамов', 'Воронов', 'Костин', 'Зуев', 'Козлов', 'Носков', 'Пестов', 'Уваров', 'Кабанов', 'Кравцов',
                'Зуев', 'Вишняков', 'Кириллов', 'Артемьев', 'Андреев', 'Александров', 'Геннадьев', 'Давыдов', 'Зайцев']

male_middle_names = ['Иванович', 'Александрович', 'Михайлович', 'Сергеевич', 'Дмитриевич', 'Андреевич', 'Евгеньевич',
                    'Артемович', 'Николаевич', 'Павлович', 'Алексеевич', 'Игоревич', 'Владимирович', 'Денисович',
                    'Олегович', 'Георгиевич', 'Максимович', 'Викторович', 'Юрьевич', 'Антонович', 'Васильевич',
                    'Вячеславович', 'Валентинович', 'Геннадьевич', 'Тимурович', 'Ильич', 'Федорович', 'Вадимович',
                    'Семенович', 'Романович', 'Константинович', 'Валерьевич', 'Борисович', 'Валентинович', 'Даниилович',
                    'Русланович', 'Степанович', 'Григориевич', 'Аркадиевич', 'Тимофейевич', 'Давидович', 'Леонидов']


# Генерация уникальных имен
female_names = ['Анна', 'Мария', 'Екатерина', 'Ольга', 'Татьяна', 'Ирина', 'Елена', 'Светлана', 'Наталья', 'Марина',
              'Алиса', 'София', 'Виктория', 'Ангелина', 'Анастасия', 'Дарья', 'Алина', 'Людмила', 'Евгения', 'Ксения',
              'Евдокия', 'Лариса', 'Надежда', 'Раиса', 'Зоя', 'Любовь', 'Ангелика', 'Юлия', 'Лилия', 'Кристина',
              'Валентина', 'Римма', 'Инесса', 'Тамара', 'Ия', 'Мирослава', 'Валерия', 'Милена', 'Вера', 'Инна',
              'Софья', 'Диана', 'Ева', 'Юлиана', 'Галина', 'Эльвира', 'Лидия', 'Анита', 'Снежана', 'Василиса',
              'Маргарита', 'Регина', 'Эвелина', 'Артемида', 'Валерия', 'Агния', 'Жанна', 'Карина', 'Лолита', 'Жанна',
              'Эльза', 'Ляля', 'Самира', 'Феруза', 'Милана', 'Валерия', 'Яна', 'Эльмира', 'Маргарита', 'Амелия']

# Генерация уникальных фамилий
female_surnames = ['Иванова', 'Петрова', 'Смирнова', 'Соколова', 'Кузнецова', 'Васильева', 'Попова', 'Семенова', 'Морозова',
                'Новикова', 'Федорова', 'Морозова', 'Козлова', 'Лебедева', 'Гаврилова', 'Захарова', 'Дмитриева', 'Калинина',
                'Баранова', 'Воробьева', 'Максимова', 'Белова', 'Кудрявцева', 'Котова', 'Сергеева', 'Завьялова', 'Тимофеева',
                'Логинова', 'Савельева', 'Панова', 'Колесникова', 'Миронова', 'Романова', 'Селезнева', 'Сазонова', 'Белякова',
                'Гусева', 'Малинина', 'Лазарева', 'Исаева', 'Беляева', 'Титова', 'Игнатьева', 'Сорокина', 'Мельникова',
                'Дорофеева', 'Суханова', 'Субботина', 'Суворова', 'Капустина', 'Филатова', 'Лукина', 'Тимошина', 'Мартынова',
                'Ефимова', 'Фролова', 'Цветкова', 'Денисова', 'Ткачева', 'Донцова', 'Королева', 'Третьякова', 'Кулакова',
                'Абрамова', 'Воронова', 'Костина', 'Зуева', 'Козлова', 'Носкова', 'Пестова', 'Уварова', 'Кабанова', 'Кравцова',
                'Зуева', 'Вишнякова', 'Кириллова', 'Артемьева', 'Андреева', 'Александрова', 'Геннадьева', 'Давыдова', 'Зайцева']



female_middle_names = ['Андреевна', 'Александровна', 'Михайловна', 'Сергеевна', 'Дмитриевна', 'Андреевна', 'Евгеньевна',
                    'Артемовна', 'Николаевна', 'Павловна', 'Алексеевна', 'Игоревна', 'Владимировна', 'Денисовна',
                    'Олеговна', 'Георгиевна', 'Максимовна', 'Викторовна', 'Юрьевна', 'Антоновна', 'Васильевна',
                    'Вячеславовна', 'Валентиновна', 'Геннадьевна', 'Тимуровна', 'Ильична', 'Федоровна', 'Вадимовна',
                    'Семеновна', 'Романовна', 'Константиновна', 'Валерьевна', 'Борисовна', 'Валентиновна', 'Данииловна',
                    'Руслановна', 'Степановна', 'Григориевна', 'Аркадиевна', 'Тимофеевна', 'Давидовна', 'Леонидовна', 'Олесьевна', 'Ростиславовна', 'Арсеньевна', 'Савельевна', 'Святославовна', 'Платоновна',
                    'Святославовна', 'Марковна', 'Мироновна', 'Тихоновна', 'Дамировна', 'Антониновна', 'Артуровна',
                    'Глебовна', 'Дмитриевна', 'Филипповна', 'Филимоновна', 'Георгиевна', 'Григориевна', 'Иосифовна']

countryes = ["Россия", "Украина", "Беларусь", "Казахстан", "Узбекистан", "Киргизия", "Таджикистан", "Молдова", "Армения", "Азербайджан", "Туркменистан", "Эстония", "Латвия", "Литва", "Грузия"]

create_insert("students", "first_name", "last_name", "middle_name", "date_of_birth", "citizenship", "contract", "group_id")

# 104 группы по 25 человек  = 2600
# Из них 9%(234) - девушки 91%(2366) - парни
for i in range(234):

    log(f"('{choice(female_names)}', '{choice(female_surnames)}', \
'{choice(female_middle_names)}', \
'{random_date()}', '{'Россия' if random() < 0.8 else choice(countryes)}', \
 {bool(randint(0,1))}, {randint(1, 104)}\
),")
    
for i in range(2366):

    log(f"('{choice(male_names)}', '{choice(male_surnames)}', \
'{choice(male_middle_names)}', \
'{random_date()}', '{'Россия' if random() < 0.8 else choice(countryes)}', \
 {bool(randint(0,1))}, {randint(1, 104)}\
),")
    
    