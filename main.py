import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe33147468c5c898cb87be16dcd2c12aa"
# Your Auth Token from twilio.com/console
auth_token  = "7bc7be35bb30f472f8d107b4fdd1d71c"

client = Client(account_sid, auth_token)

#abrir os 6 arquivos excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    #print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    #print(tabela_vendas)

    if (tabela_vendas['Vendas'] > 55000).any():
        
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        venda = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]

        print(f'No mes de {mes} encontrou alguem. Vendedor: {vendedor}. Vendas: {venda}')

        message = client.messages.create(
            to="+5511969807008", 
            from_="+18484045036",
            body=f'No mes de {mes} encontrou alguem. Vendedor: {vendedor}. Vendas: {venda}')




print(message.sid)


#verificar se alguma venda passou de 55,000 
#pra cada arquivo:
#se for maior entao mandar sms

#se n for, continua procurando
