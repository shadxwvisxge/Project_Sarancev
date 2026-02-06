s = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'

def process_temps(data_str):
    parts = data_str.split()
    year = parts[0]
    temps = list(map(int, parts[1:]))
    avg = sum(temps) / len(temps)
    min_temp = min(temps)
    return {year: temps}, avg, min_temp

temp_dict, average, minimum = process_temps(s)
print(f"Средняя температура: {average:.2f}")
print(f"Минимальная температура: {minimum}")