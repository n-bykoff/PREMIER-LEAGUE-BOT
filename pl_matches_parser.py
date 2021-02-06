from selenium import webdriver
import pickle
import time


def upadate_results_data():
    # go to Premier League page
    wb = webdriver.Chrome()
    wb.get('https://www.premierleague.com/results')

    time.sleep(1)

    # accept coockies
    btn = wb.find_elements_by_class_name('btn-primary')[1]
    btn.click()

    SCROLL_PAUSE_TIME = 1

    # Get scroll height
    last_height = wb.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        wb.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = wb.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

    time.sleep(2)

    match_days = wb.find_elements_by_class_name('fixtures__matches-list')
    match_days_dic = {}

    for match_day in match_days:
        date = match_day.get_attribute('data-competition-matches-list')
        match_day_list = match_day.text.split('\n')
        match_days_dic[date] = []

        for i in range(0, len(match_day_list), 3):
            match_days_dic[date].append(' '.join(match_day_list[i:i + 3]))

    with open('data.pickle', 'wb') as f:
        pickle.dump(match_days_dic, f)

    wb.close()


if __name__ == '__main__':
    upadate_results_data()

    with open('data.pickle', 'rb') as f:
        data_new = pickle.load(f)

    print(data_new)
