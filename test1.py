from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():

    # Применям опции, чтобы браузер не закрывался после выполнения программы
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=chrome_options)

    # Определяем переменную для адреса сайта
    main_url = 'http://www.siaxx.com/'

    # Открываем сайт в браузере 
    browser.get(main_url)

    # Ищем ссылочные элементы html-страницы, по селектору "href"
    elems = browser.find_elements_by_css_selector("[href]")

    # Помещаем в массив, значения ссылок, а именно url.
    links = [elem.get_attribute('href') for elem in elems]
    print(links) # Выводим массив url в консоль, для наглядности

    # Сортируем массив url по алфавиту
    myLinks = sorted(links) 
    print(myLinks) # Выводим массив url в консоль, для наглядности

    # Удаляем повторяющиеся пути
    myFinalLinks = list(dict.fromkeys(myLinks))
    print(myFinalLinks) # Выводим массив url в консоль, для наглядности

    # Определяем счетчики 
    i = 1 # для вкладок браузера
    j = 0 # для элементов массива 

    # Для каждого элемента(url) массива открываем новую вкладку в браузере
    for item in myFinalLinks:
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[i])
        browser.get(myFinalLinks[j])
        j+=1
        i+=1



    # Переходим на первую вкладку(исходный сайт)
    browser.switch_to.window(browser.window_handles[0])
    
    
    # Закрываем все вкладки, начиная с исходной и по порядку
    while 1:
        browser.close()   
        browser.switch_to.window(browser.window_handles[0]) 

# Точка входа в программу
if __name__ == "__main__":
    main()