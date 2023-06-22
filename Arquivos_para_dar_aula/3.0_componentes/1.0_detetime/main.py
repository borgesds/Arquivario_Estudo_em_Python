from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays

data = datetime(2023, 5, 8, 15, 25, 8)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

print(data.strptime('20/04/2023', '%d/%m/%Y'))

data2 = datetime.strptime('20/04/2023 10:00:00', '%d/%m/%Y %H:%M:%S')
data3 = data2 + timedelta(days=5, hours=11, minutes=15, seconds=21)
data4 = datetime.strptime('29/04/2023 20:55:40', '%d/%m/%Y %H:%M:%S')

dif = data4 - data2

print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(dif)

# formatar
setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
formatacao1 = dt.strftime('%A, %d de %B de %Y')
formatacao2 = data.strftime('%d/%m/%Y %H:%M:%S')

print(formatacao1)
print(formatacao2)
print(mes_atual, mdays[mes_atual])
