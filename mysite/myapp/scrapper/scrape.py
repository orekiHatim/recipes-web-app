from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import datetime
import random
import re
import json


"""now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day

time_str = datetime.datetime(year, month, day).strftime("%H:%M:%S.%f")
random.seed(time_str)"""

def getLinks(recipeUrl):
    html = urlopen('https://www.allrecipes.com/{}'.format(recipeUrl))
    bs = BeautifulSoup(html.read(), 'html.parser')
    recipes_section = bs.find('section', {'id' : 'recirc-section_1-0'})
    recipes_list_div = recipes_section.find('div', {'class' : 'loc recirc-content'})
    links = []
    for child in recipes_list_div.children:
        if child.name == 'div' and child['class'][2] == 'card-list':
            a_tags = child.find_all('a', href=re.compile('\/recipe\/[0-9]+'))
            for ele in a_tags:
                links.append(ele['href'])
    
    return links

def scrape(firstUrl, numberOfRecipes):
    #url should be like this : 'recipe/26670/taylors-piroshki/'
    links = getLinks(firstUrl)
    #print(type(links[0]))
    recipes_list = []
    count = 0
    while len(links) > 0 and count <= numberOfRecipes:

        #print(count)
        try :
            url = links[random.randint(0, len(links)-1)]
            driver = webdriver.Firefox()
            driver.get(url)
            print('Scrapping the url : {}'.format(url))

            # Wait for the page to fully load
            isThereReviews = True
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".feedback-list__items"))) 
            
            
            """html = urlopen('https://www.allrecipes.com/recipe/238510/homemade-arepas/')"""
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)
        except TimeoutException as e:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".pushly_popover-box pushly-prompt-slide"))) 
            driver.find_element(By.CLASS, 'pushly_popover-buttons-dismiss pushly-prompt-buttons-dismiss').click()
            try :
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".feedback-list__items")))
            except TimeoutException as e:
                isThereReviews = False

        html = driver.page_source

        try:
            bs = BeautifulSoup(html, 'html.parser')
            """Scarpping recipe title"""
            recipe_heading = bs.find('h1' , {'id' : 'article-heading_1-0'}).text.strip()
            """Scarpping description"""
            recipe_description =  bs.find('p' , {'id' : 'article-subheading_1-0'}).text.strip()
            """Scarpping Category"""
            category_list_tag = bs.find('ul', {'id' : 'breadcrumbs__list_1-0'})
            category_list_li_tags = category_list_tag.find_all('li')
            category_tag = category_list_li_tags[-1]
            recipe_category = category_tag.find('span').text

            """Scrapping images"""
            many_images_indicator = driver.find_elements(By.ID, 'gallery-photos_1-0')
            recipe_images = []
            if len(many_images_indicator) == 0:
                image_div = bs.find('div', {'class' : 'primary-image__media'})
                image_tag = image_div.find('img', {'class' : 'primary-image__image'})
                image = image_tag.get('src')
                recipe_images.append(image)
            else :
                driver.find_element(By.ID, 'gallery-photos_1-0').click()
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#photo-dialog__item_1-2")))
                recipe_images_page = BeautifulSoup(driver.page_source, 'html.parser')
                recipe_images_container = recipe_images_page.find('div', {'id' : 'photo-dialog__page_1-0'})
                
                for child in recipe_images_container.children:
                    if child.name == 'div' :
                        image_tag = child.find('img')
                        image = image_tag.get('data-src')
                        recipe_images.append(image)

                driver.quit()

            """Scarpping recipe time related infos"""
            recipe_infos = []
            info_container = bs.find('div', {'id' : 'recipe-details_1-0'})
            info_parent = info_container.find('div', {'class' : 'mntl-recipe-details__content'})
            for child in info_parent.children:
                if child.name == 'div' :
                    label = child.find('div', {'class' : 'mntl-recipe-details__label'}).text
                    value = child.find('div', {'class' : 'mntl-recipe-details__value'}).text
                    recipe_infos.append({label : value})


            """Scrapping recipe ingrediants"""
            ingrediants_div = bs.find('div', {'id' : 'mntl-structured-ingredients_1-0'})
            ingrediants_list_headings = []
            ingrediants_lists = []
            for child in ingrediants_div.children:
                if child.name == 'p':
                    ingrediants_list_headings.append(child.text)
                if child.name == 'ul':
                    ingredients_items = []
                    for li in child.children:
                        if li.name == 'li':
                            ingrediant = li.find('p').text.strip()
                            ingredients_items.append(ingrediant)
                    ingrediants_lists.append(ingredients_items)


            recipe_ingrediants = []
            if len(ingrediants_list_headings) == 0:
                recipe_ingrediants.append(ingrediants_lists[0])
            else :
                for i in range(len(ingrediants_lists)):
                    if i >= len(ingrediants_list_headings):
                        ingrediants_list_headings.append('ingrediants')
                    recipe_ingrediants.append({ingrediants_list_headings[i] : ingrediants_lists[i]})


            """Scrapping recipe steps"""
            steps_div = bs.find('div', {'id' : 'recipe__steps-content_1-0'})
            steps_ul = steps_div.find('ol', {'id' : 'mntl-sc-block_2-0'})
            recipe_steps = []
            for child in steps_ul.children:
                if child.name == 'li':
                    step = child.find('p').text.strip()
                    recipe_steps.append(step)

            """Scrapping recipe reviews"""
            recipe_reviews = []
            recipe_rating = None
            if isThereReviews:
                """Scarpping over all rating"""
                recipe_rating = bs.find('div' , {'id' : 'mntl-recipe-review-bar__rating_1-0'}).text.strip()
                
                reviews_container = bs.find('div', {'id' : 'recipe-ugc-wrapper_1-0'})
                reviews_div = reviews_container.find('div', {'class' : 'feedback-list'})
                reviews_items = reviews_div.find('div', {'class' : 'feedback-list__items'})
                #print(type(reviews_items))
                for child in reviews_items.children:
                    if child.name == 'div' and child['class'][0] == 'feedback-list__item':
                        """Scrapping username"""
                        heading_tag = child.find('div', {'class' : 'feedback__heading'})
                        display_name = heading_tag.find('span', {'class' : 'feedback__display-name'})
                        display_name_a_tag = display_name.find('a', {'class' : 'feedback__display-name-link'})
                        dirty_username = display_name.text
                        if display_name_a_tag != None :
                            dirty_username = display_name_a_tag.text
                        recipe_username = dirty_username.strip()
                        #print(recipe_username)
                        """Scrapping note"""
                        note_div = child.find('div', {'class' : 'feedback__meta'})
                        stars_list = note_div.find('div', {'class' : 'feedback__stars'})
                        star_svg = stars_list.find_all('svg', {'class' : 'icon ugc-icon-star ugc-icon-avatar-null'})
                        recipe_note = len(star_svg)
                        """Scrapping comment"""
                        feedback_comment_container = child.find('div', {'class' : 'feedback__body-container'})
                        feedback_comment = feedback_comment_container.find('div', {'class' : 'feedback__body'})
                        recipe_comment = feedback_comment.find('p').text.strip()
                        """Fetching data to one object named recipe_reviews"""
                        recipe_reviews.append({'user' : recipe_username, 'note' : recipe_note, 'comment' : recipe_comment})
                    

            recipe = {'heading' : recipe_heading, 'category' : recipe_category,
                        'overall-rating' : recipe_rating, 'description' : recipe_description,
                        'images' : recipe_images, 'ingrediants' : recipe_ingrediants, 
                        'steps' : recipe_steps, 'infos' : recipe_infos, 'reviews' : recipe_reviews}
            
            
            #print(recipe)
            recipes_list.append(recipe)
            links = getLinks(url.replace('https://www.allrecipes.com/', ''))
            count = count + 1
        except AttributeError as e:
            print(e)
        except Exception as e:
            print(e)
    
    return recipes_list
      