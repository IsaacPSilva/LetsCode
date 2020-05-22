'''5. Faça uma função que recebe um nome e um horário e imprime “Bom
dia, [nome]”, caso seja antes de 12h, “Boa Tarde, [nome]”, caso seja
entre 12h e 18h e “Boa noite, [nome]” se for após às 18h.'''



#Definir função
def relogio(hora, nome):

    if hora >5 and hora<=12:
        print(f'Bom dia {nome}')
        
    if hora >12 and hora<=18:
        print(f'Boa tarde {nome}')
        
    if hora >18 and hora<=23:
        print(f'Boa noite {nome}')
        
    if hora<=5:
        print(f'Poxa vai dormir {nome} é madrugada')


relogio(4, 'Isaac')
relogio(11, 'Rafael')