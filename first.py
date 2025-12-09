import csv
import random
from faker import Faker

fake = Faker('uk_UA')

names = {
    'Ч': (['Олександр', 'Андрій', 'Михайло', 'Іван', 'Василь', 'Петро', 'Сергій', 'Дмитро', 'Віктор', 'Володимир'],
          ['Олександрович', 'Андрійович', 'Михайлович', 'Іванович', 'Васильович', 'Петрович', 'Сергійович', 'Дмитрович'],
          'Чоловіча'),
    'Ж': (['Олена', 'Марія', 'Наталія', 'Тетяна', 'Ірина', 'Оксана', 'Світлана', 'Катерина', 'Анна', 'Юлія'],
          ['Олександрівна', 'Андріївна', 'Михайлівна', 'Іванівна', 'Василівна', 'Петрівна', 'Сергіївна', 'Дмитрівна'],
          'Жіноча')
}

genders = ['Ж'] * 200 + ['Ч'] * 300
random.shuffle(genders)

with open('people_data.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['Прізвище', 'Ім\'я', 'По батькові', 'Стать', 'Дата народження',
                     'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'])

    for g in genders:
        n, p, s = names[g]

        while True:
            try:
                birth = fake.date_of_birth(minimum_age=16, maximum_age=86).replace(year=random.randint(1938, 2008))
                break
            except ValueError:
                continue
        writer.writerow([
            fake.last_name(),
            random.choice(n),
            random.choice(p),
            s,
            birth.strftime('%d.%m.%Y'),
            fake.job(),
            fake.city(),
            fake.address(),
            fake.phone_number(),
            fake.email()
        ])

print('Файл people_data.csv створено')