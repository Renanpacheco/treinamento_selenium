from selenium.webdriver import Firefox #importa o naveador a ser utilizado
from time import sleep

url='https://curso-python-selenium.netlify.app/exercicio_02.html' #seria bom verificar o link para entender como o jogo funciona
navegador=Firefox()
navegador.get(url)
navegador.implicitly_wait(10)# faz o navegador esperar antes de procurar os elementos pedidos, caso contrario ele procura antes de os elementos serem gerados

p=navegador.find_elements_by_tag_name('p')
controle=p[-1].text#obter o valor de controle do site
controle_int=int(controle[-1])

valor=0
click_a=navegador.find_element_by_tag_name('a')
while(controle_int!=valor):#laço para clicar e veficar os valores ate obter a vitoria
    click_a.click()
    p=navegador.find_elements_by_tag_name('p')
    pv=p[-1].text
    valor=int(pv[-1])


#sleep(4) colocado aqui apenas para observar a pagina depois da vitoria
navegador.quit()