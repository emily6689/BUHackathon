#__author__ Emily Williams, ecwilliams66@gmail.com

import json
import nltk
import pdb

json_data = open('/Users/emily6689/hackathonpython/neurotalk-emails.json').read()
json_emails = json.loads(json_data)

food_terms_list = ["refreshments", "pizza", "food", "snacks", "breakfast", "lunch", "dinner"]

def simple_food_identifier():
    for email in json_emails:
        email_content = nltk.clean_html(email["bodyHtml"]).lower()
        if any(food_term in email_content for food_term in food_terms_list):
            print "There will be food!"
            #------or assign some sort of food_tag to event here.--------#


#'advanced' for lack of a better term....
def advanced_food_identifier():
    for email in json_emails:
        present_food_terms = []
        email_body = nltk.clean_html(email["bodyHtml"]).lower()
        for food_term in food_terms_list:
            if food_term in email_body:
                if "light {}".format(food_term) in email_body:
                    present_food_terms.append("light " + food_term)
                else:
                    present_food_terms.append(food_term)
        if len(present_food_terms) > 1 and "food" in present_food_terms:
            present_food_terms.remove("food")
        if len(present_food_terms) > 2:
            food_string = ", ".join(present_food_terms)
        elif len(present_food_terms) >= 1:
            food_string = " and ".join(present_food_terms)
        #print "Talk#{}: ".format(json_emails.index(email)) #<---- in case you'd like to see which email it's referring to.
        print "There will be: " + food_string
#i.e. "There will be: light refreshments and dinner."



#TESTING/EVALUATING CODE
#returns a list of food_terms and how many times each appears in the json emails.
#use this to see if adding a word to food_terms_list is worth it.....
def count_instances_of_each_food_term():
    food_term_count = dict((food_term, 0) for food_term in food_terms_list)
    for email in json_emails:
        email_body = nltk.clean_html(email["bodyHtml"]).lower()
        for food_term in food_terms_list:
            if food_term in email_body:
                food_term_count[food_term] += 1
                dictionary[key] += 1
    print food_term_count


