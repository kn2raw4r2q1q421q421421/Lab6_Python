import csv
from datetime import datetime
import matplotlib.pyplot as plt

try:
    with open('people_data.csv', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    print("Ok")
except FileNotFoundError:
    print("Повідомлення про відсутність, або проблеми при відкритті файлу CSV")
    exit()

gc = {'Чоловіча': 0, 'Жіноча': 0}
categories = ['<18', '18-45', '45-70', '>70']
ac = {k: 0 for k in categories}
gac = {
    'Чоловіча': {k: 0 for k in categories},
    'Жіноча': {k: 0 for k in categories}
}

today = datetime.now()

for p in data:
    try:
        bd = datetime.strptime(p['Дата народження'], '%d.%m.%Y')
        age = today.year - bd.year - ((today.month, today.day) < (bd.month, bd.day))
    except ValueError:
        continue

    if age < 18: cat = '<18'
    elif age <= 45: cat = '18-45'
    elif age <= 70: cat = '45-70'
    else: cat = '>70'
    gc[p['Стать']] += 1
    ac[cat] += 1
    gac[p['Стать']][cat] += 1

print("\n=== За статтю ===")
for k, v in gc.items():
    print(f"{k}: {v}")

print("\n=== За віком ===")
for k, v in ac.items():
    print(f"{k}: {v}")

print("\n=== За статтю та віком ===")
for g in gac:
    print(f"\n{g}:")
    for k, v in gac[g].items():
        print(f"  {k}: {v}")
def plot_graph(vals, title, filename, colors, labels=None):
    plt.figure(figsize=(10, 6))
    
    if labels: 
        x = range(len(labels))
        plt.bar([i - 0.2 for i in x], vals[0], 0.4, label='Чоловіки', color='blue')
        plt.bar([i + 0.2 for i in x], vals[1], 0.4, label='Жінки', color='pink')
        plt.xticks(x, labels)
        plt.legend()
    else:
        plt.bar(range(len(vals)), list(vals.values()), color=colors)
        plt.xticks(range(len(vals)), vals.keys())
    
    plt.title(title)
    plt.ylabel('Кількість')
    plt.tight_layout()
    plt.savefig(filename)
    print(f"Графік збережено як {filename}")

plot_graph(gc, 'За статтю', 'gender.png', ['blue', 'pink'])
plot_graph(ac, 'За віком', 'age.png', ['green', 'orange', 'red', 'purple'])
plot_graph(
    [list(gac['Чоловіча'].values()), list(gac['Жіноча'].values())], 
    'За статтю та віком', 
    'gender_age.png', 
    None, 
    labels=list(ac.keys())
)