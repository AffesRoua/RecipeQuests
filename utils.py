import requests
import streamlit as st 
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get the API key
api_key = os.getenv("API_KEY")


diets = [
            "Gluten Free", "Ketogenic", "Vegetarian", "Lacto-Vegetarian",
            "Ovo-Vegetarian", "Vegan", "Pescetarian", "Paleo", 
            "Primal", "Low FODMAP", "Whole30"
        ]
cuisines = [
            "African", "Asian", "American", "British", "Cajun", "Caribbean",
            "Chinese", "Eastern European", "European", "French", "German",
            "Greek", "Indian", "Irish", "Italian", "Japanese", "Jewish",
            "Korean", "Latin American", "Mediterranean", "Mexican", 
            "Middle Eastern", "Nordic", "Southern", "Spanish", "Thai", "Vietnamese"
        ]
intolerances = [
            "Dairy", "Egg", "Gluten", "Grain", "Peanut", "Seafood", 
            "Sesame", "Shellfish", "Soy", "Sulfite", "Tree Nut", "Wheat"
        ]
meal_types = [
            "Main Course", "Side Dish", "Dessert", "Appetizer", "Salad", 
            "Bread", "Breakfast", "Soup", "Beverage", "Sauce", 
            "Marinade", "Fingerfood", "Snack", "Drink"
        ]
def search_recipes(api_key, cuisine=None, excludeCuisine=None, diet=None, intolerances=None, type=None):
    url = "https://api.spoonacular.com/recipes/complexSearch"

    # Parameters dictionary with all specified options
    params = {
        "apiKey": api_key,
        "cuisine": cuisine,
        "excludeCuisine": excludeCuisine,
        "diet": diet,
        "intolerances": intolerances,
        "type": type
    }

    # Making the request
    response = requests.get(url, params=params)
    return response.json()

def search_recipes_summarize(api_key, id):
    url = f"https://api.spoonacular.com/recipes/{id}/information?apiKey={api_key}"
    response = requests.get(url)
    return response.json()

def search_recipes_videos(api_key,diet,type,cuisine):
    url = f"https://api.spoonacular.com/food/videos/search"
    params = {
        "apiKey": api_key,
        "cuisine": cuisine,
        "diet": diet,
        "type": type
    }
    response = requests.get(url, params=params)
    return response.json()


def talk_to_chatbot(api_key,text,context_id):
    url=f"https://api.spoonacular.com/food/converse"
    params = {
        "apiKey": api_key,
        "text": text,
        "contextID": context_id
        
    }
    response = requests.get(url, params=params)
    return response.json()



def show_details(info):
                            st.subheader("Cooking Details and steps ")

                            #infos about the receipe
                            st.write(f"***Preparation Time:*** {info['preparationMinutes']} minutes")
                            st.write(f"***Cooking Time:*** {info['cookingMinutes']} minutes")
                            st.write(f"***Servings:*** {info['extendedIngredients'][0]['amount']} ")

                            #ingredients
                            st.subheader("Ingredients")
                            for ingredient in info['extendedIngredients'] : 
                                st.write(f'* {ingredient['originalName']}')
                            
                            #instructions 
                            st.subheader("Instructions")
                            if '<' in info['instructions'] and '>' in info['instructions']:  # Simple check for HTML
                                st.markdown(info['instructions'], unsafe_allow_html=True)
                            else: #instructions seprated by dots 
                                instruction_steps = info['instructions'].split('.')
                                for step in instruction_steps:
                                    step = step.strip()  # Remove leading/trailing whitespace
                                    if step:  # Only display non-empty steps
                                        st.write(f"- {step}.")  # Add the period back for each step

