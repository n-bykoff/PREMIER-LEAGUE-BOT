from selenium import webdriver
import time


def get_last_table():
    # go to Premier League tables page
    wb = webdriver.Chrome()
    wb.get('https://www.premierleague.com/tables')

    time.sleep(1)

    # accept coockies
    btn = wb.find_elements_by_class_name('btn-primary')[1]
    btn.click()

    table = wb.find_element_by_class_name('table')
    final_data = make_final_data(table.text)

    wb.close()

    return final_data


def make_final_data(table):
    table_list = table.split('\n')[2:]
    header = ' '.join(table_list[:8])

    final_table = [header]

    for i in range(8, len(table_list), 3):
        final_table.append(' '.join(table_list[i:i + 3]))

    data = ''
    for x in final_table:
        data += x + '\n'

    return data


if __name__ == '__main__':
    get_last_table()
