
from datetime import datetime
datas = ['31-03-2000', '15-03-2000', '22-02-2000', '30-01-2000']

#datas yyyy/mm/dd
# datas = ['1990-05-10', '1985-12-25', '1998-02-15', '1976-08-01']

datas_formatadas = [datetime.strptime(data, '%d-%m-%Y') for data in datas] # se quiser mudar a formatação da data mude '%Y-%m-%d'

datas_formatadas.sort(reverse=False) # se quiser descrescente mude para True

print('\n')

for data in datas_formatadas:

    print(data.strftime('%d-%m-%Y')) # print(data.strftime('%d-%m-%Y'))
    # ou
    print(data.strftime('%Y-%m-%d')) # print(data.strftime('%Y-%m-%d'))
    print("\n")

