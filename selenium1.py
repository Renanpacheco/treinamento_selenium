from selenium.webdriver import Firefox #importa o navegador a ser utilizado
#from time import sleep deixado aqui por memorizaçao, ja que nao era garantido que atrasaria o processo o suficiente

elementos=[]#vetor para guardar os elementos lindos do navegador

url='https://curso-python-selenium.netlify.app/aula_03.html'
#url1='endereço da minha maquina' tentativa de abrir um arquivo html
navegador=Firefox()#instancia e abre o navegador
navegador.get(url)
navegador.implicitly_wait(10)# faz o navegador esperar antes de procurar os elementos pedidos, caso contrario ele procura antes de os elementos serem gerados
a=navegador.find_element_by_tag_name('a')
p=navegador.find_element_by_tag_name('p')#pega sempre o primeiro elemento

for click in range(10):#codigo do curso
    ps=navegador.find_elements_by_tag_name('p')
    a.click()
    print(f'valor do ultimo p: {ps[-1].text} ultimo click: {click}')
    print(f'os valores do ultimo p e ultimo click sao iguais: {ps[-1].text == str(click)}')


#meusps=navegador.find_elements_by_tag_name('p')#cria uma lista com todos os valores
#print(f'texto de a: {a.text}')
#print(f'texto de p: {p.text}')
#print(ps)
'''
for elemento in ps: #percorre a lista elemento por elemento, convertendo o conteudo para string
    elementos.append(elemento.text)

print(elementos) #imprime a lista

'''
navegador.quit() #comando para fechar o navegador