
# 🍴 RecipeQuest  

**RecipeQuest** is a Streamlit-based web app that helps users explore recipes, watch cooking videos, and interact with a chatbot for personalized recipe suggestions. The project leverages the Spoonacular API to fetch real-time data about cuisines, meal types, and dietary preferences.

---

## Features  
1. **Search Recipes:**  
   - Filter recipes by cuisines, diets, intolerances, and meal types.  
   - View recipe details such as preparation and cooking time, servings, and ingredients.

2. **Search Suggestion Videos:**  
   - Watch cooking videos tailored to your preferences.  
   - Discover new recipes with video tutorials.

3. **Chatbot Interaction:**  
   - Get personalized recipe suggestions from a conversational chatbot.  
   - Continue existing conversations using unique session IDs.

---

## Technologies Used  
- **Streamlit:** For building the interactive web application.  
- **Spoonacular API:** For accessing recipe data, video suggestions, and chatbot functionality.  
- **Python:** To integrate API requests and handle application logic.

---

## What I Learned  
1. **Making API Requests:**  
   - Learned how to use the `requests` library to fetch data from an API.  
   - Gained experience in managing query parameters and handling API responses.  

2. **Building Interactive Apps with Streamlit:**  
   - Learned to create dynamic forms, manage user inputs, and display rich content such as images and videos.  

3. **Error Handling and Data Parsing:**  
   - Managed edge cases, such as empty responses or invalid user inputs.  
   - Parsed and displayed complex JSON responses from the API effectively.


## Setup Instructions

Follow these steps to set up and run the **RecipeQuest** project on your local machine:

### 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/your-username/RecipeQuest.git
cd RecipeQuest
```

### 2. Create and Activate a Virtual Environment
Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```

Activate the virtual environment:
- **On Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install the Requirements
Install the necessary dependencies from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App
Start the Streamlit app by running the following command:
```bash
streamlit run spoonacular_project.py
```

### 5. Set Up Your API Key
To use the Spoonacular API, you will need an API key. Follow these steps:  
1. Go to the [Spoonacular API Documentation](https://spoonacular.com/food-api/docs).  
2. Sign up and obtain your API key.  
3. Replace `API_KEY="your api key"` in your code with your actual API key.




