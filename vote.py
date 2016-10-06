from selenium import webdriver
import sys
from time import sleep

def main():
    ''' 南雲穂波さんに投票する '''
    url = 'https://misscolle.com/todai2016/vote'
    entry_no = 4
    vote(url, entry_no)

def vote(url, entry_no):
    '''
    Firefoxを操作して投票する
    @param {str} url
    @param {int} entry_no
    '''
    # Firefox を起動
    browser = webdriver.Firefox()
    browser.get(url)

    # 要素を取得
    entry = browser.find_elements_by_css_selector('#entries .entry')[entry_no - 1]
    entry_no = entry.find_element_by_css_selector('.info .entry_no').text
    name = entry.find_element_by_css_selector('.info h3').text

    try:
        # 投票ボタンをクリック
        vote_btn = entry.find_element_by_css_selector('.vote-box a')
        vote_btn.click()
    except:
        # 投票できなければ終了
        print ('現在投票は受け付けられておりません。')
        browser.close()
        sys.exit(1)

    # 確認ボタンをクリック
    sleep(1)
    confirm_btn = browser.find_element_by_css_selector('.ui-dialog .ui-dialog-buttonset button')
    confirm_btn.click()

    print ('{0}:\n{1}さんに投票しました！'.format(entry_no, name))

    # Firefox を終了
    sleep(1)
    browser.close()

if __name__ == '__main__':
    main()
