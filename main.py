from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def search_wikipedia(query):
    driver = webdriver.Chrome()

    driver.get("https://ru.wikipedia.org/")

    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    print("Название статьи:", driver.find_element(By.ID, "firstHeading").text)

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")

        choice = input("Введите номер действия: ")

        if choice == '1':

            paragraphs = driver.find_elements(By.TAG_NAME, "p")
            for idx, paragraph in enumerate(paragraphs, start=1):
                print(f"Параграф {idx}:\n{paragraph.text}\n")
        elif choice == '2':

            related_links = driver.find_elements(By.XPATH, "//div[@id='mw-content-text']//a[contains(@href, '/wiki/')]")
            print("Связанные статьи:")
            for idx, link in enumerate(related_links, start=1):
                print(f"{idx}. {link.text}")

            link_choice = input("Введите номер связанной статьи для перехода (или '0' для выхода): ")
            if link_choice == '0':
                continue
            try:
                link_choice = int(link_choice)
                if link_choice < 1 or link_choice > len(related_links):
                    raise ValueError
            except ValueError:
                print("Некорректный выбор. Пожалуйста, выберите номер из списка.")
                continue

            selected_link = related_links[link_choice - 1]
            selected_link.click()
            print("\nВы перешли на страницу:", driver.find_element(By.ID, "firstHeading").text)
        elif choice == '3':

            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите номер действия из списка.")


    driver.quit()

if __name__ == "__main__":

    user_query = input("Введите запрос для поиска на Википедии: ")
    search_wikipedia(user_query)
