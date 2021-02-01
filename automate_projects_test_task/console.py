import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from automate_projects_test_task.selenium import get_driver

logger = logging.getLogger(__name__)


def post_user_review(url, nickname, review_datetime, loading_timeout=20):
    driver = get_driver()
    driver.get(url)

    # Open two tabs in order to bypass Cloudflare antibot protection.
    driver.execute_script('''window.open("$url");''')
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    try:
        element = WebDriverWait(driver, loading_timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, "active-tab-content"))
        )
        logger.debug("Page is ready!")
    except TimeoutException:
        logger.error("Loading took to much time!")
        raise

    time.sleep(10)

    # Parse all thread items.
    for thread_item in element.find_elements_by_class_name('thread-item'):
        thread_item_element = thread_item.text.split('\n')
        thread_data_id = thread_item.get_attribute('data-id')

        # Match thread item with user input <nickname> and <review_date>
        if (thread_item_element[0] == nickname and thread_item_element[1] == review_datetime):
            print(thread_item_element[3][0:31])

            print ("Please rate thread information...")
            user_review = input()
            # user_review = ':('

            # I know this code must be moved inside a function. Is closing the window that apears when mooving the cursor inside the page.
            close_button = element.find_element_by_xpath('//*[@id="dont-go-yet-modal"]/div/div/div[1]/button')
            if (close_button.is_displayed()):
                ActionChains(driver).move_to_element(close_button).click(close_button).perform()

            # Positive negative review scores.
            if user_review == ':)':
                positive_review = thread_item.find_element_by_xpath('//*[@id="scroll%s"]/div[2]/div/div/footer/span[1]/a[1]' % thread_data_id)
                if (positive_review.get_attribute('data-post-id') == thread_data_id and positive_review.is_displayed() and positive_review.is_enabled()):
                    ActionChains(driver).move_to_element(positive_review).click(positive_review).perform()

            elif user_review == ':(':
                negative_review = thread_item.find_element_by_xpath('//*[@id="scroll%s"]/div[2]/div/div/footer/span[1]/a[2]' % thread_data_id)
                if (negative_review.get_attribute('data-post-id') == thread_data_id and negative_review.is_displayed() and negative_review.is_enabled()):
                    ActionChains(driver).move_to_element(negative_review).click(negative_review).perform()

        else:
            close_button = element.find_element_by_xpath('//*[@id="dont-go-yet-modal"]/div/div/div[1]/button')
            if (close_button.is_displayed()):
                ActionChains(driver).move_to_element(close_button).click(close_button).perform()

            time.sleep(3)
            # Expand review trees, maybe the <nickname> and <review_data> compination is there.
            expand_replies = thread_item.find_element_by_class_name('thread-replies-%s' % thread_data_id)
            if expand_replies.is_displayed():
                ActionChains(driver).move_to_element(expand_replies).click(expand_replies).perform()

            review_replies_container_list = thread_item.find_element_by_class_name('review-replies-list__container')
            reviews = review_replies_container_list.find_elements_by_class_name('review')

            for review in reviews:
                review_data_id = review.get_attribute('data-id')
                review_element = review.text.split('\n')

                if (review_element[0] == nickname and review_element[1] == review_datetime):
                    print(review_element[5][0:31])

                    print ("Please rate review information...")
                    user_review = input()
                    # user_review = ':)'

                    close_button = element.find_element_by_xpath('//*[@id="dont-go-yet-modal"]/div/div/div[1]/button')
                    if (close_button.is_displayed()):
                        ActionChains(driver).move_to_element(close_button).click(close_button).perform()

                    time.sleep(2)
                    if user_review == ':)':
                        positive_review = thread_item.find_element_by_xpath('//*[@id="scroll%s"]/div[2]/div/div/footer/span[1]/a[1]' % review_data_id)
                        if (positive_review.get_attribute('data-post-id') == review_data_id and positive_review.is_displayed() and positive_review.is_enabled()):
                            ActionChains(driver).move_to_element(positive_review).click(positive_review).perform()

                    elif user_review == ':(':
                        negative_review = thread_item.find_element_by_xpath('//*[@id="scroll%s"]/div[2]/div/div/footer/span[1]/a[2]' % review_data_id)
                        if (negative_review.get_attribute('data-post-id') == review_data_id and negative_review.is_displayed() and negative_review.is_enabled()):
                            ActionChains(driver).move_to_element(negative_review).click(negative_review).perform()

    driver.quit()
