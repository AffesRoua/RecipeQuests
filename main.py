import streamlit as st
import uuid
import re
from utils import (
    api_key, diets, cuisines, intolerances, meal_types,
    search_recipes, search_recipes_summarize, search_recipes_videos, talk_to_chatbot,show_details
)


# Sidebar navigation
st.sidebar.title("🍴 Navigation")
option = st.sidebar.radio("🤔 What do you feel like doing today?", ["Search Recipe", "search suggestions videos","talk to chatbot"])

# Display the relevant section based on the selected option
if option == "Search Recipe":
    st.header("🔍 Search Recipe")
    with st.form("search_recipe_form"):
        
        included_cuisines = st.multiselect("Select Cuisine(s) to include", options=cuisines)
        excluded_cuisines = st.multiselect("Select Cuisine(s) to exclude", options=cuisines)
        selected_diets = st.multiselect("Select Diet(s)", options=diets)
        selected_intolerances = st.multiselect("Select Intolerance(s)", options=intolerances)
        selected_meal_types = st.multiselect("Select Meal Type(s)", options=meal_types)

        submit_button = st.form_submit_button("Submit")

    # Call the search_recipes function with the provided parameters after the form
    if submit_button:
        recipes = search_recipes(api_key, 
                                 cuisine=', '.join(included_cuisines), 
                                 excludeCuisine=', '.join(excluded_cuisines), 
                                 diet=', '.join(selected_diets), 
                                 intolerances=', '.join(selected_intolerances), 
                                 type=', '.join(selected_meal_types))
        
        # Display the results outside the form frame
        if 'results' in recipes and len(recipes['results']) > 0:
            for recipe in recipes['results'] :
                # Create two columns for layout
                col1, col2 = st.columns([1, 2]) 
                # Display the image in the first column
                with col1:
                    st.markdown(
                        
                            f'<img src="{recipe['image']}" width="200" style="border-radius: 8px; margin-bottom: 15px;">'
                            ,
                            unsafe_allow_html=True
                        )
                    

                # Add the expander in the second column to the right of the image
                with col2:
                    st.write(f"**{recipe['title']}**")
                    with st.expander(label="Details"):
                        info=search_recipes_summarize(api_key, recipe['id'])
                        show_details(info)
        else:
            st.write("No recipes found. Please check if you have excluded and included the same cuisine.")

if option == "search suggestions videos":
    st.header("🎥 Search Suggestions Videos")
    with st.form("recipe_form"):
    # Multi-select fields
        st.write("You have to fill at least one of these fields to get a result ")
        types = st.multiselect("Select Type(s)", options=meal_types)
        cuisines = st.multiselect("Select Cuisine(s)", options=cuisines)
        diets = st.multiselect("Select Diet(s)", options=diets)

        submit_button = st.form_submit_button("Submit")
        
    if submit_button:
            response = search_recipes_videos(api_key, diets, types, cuisines)
            for video in response['videos']:
                # Create two columns for layout
                col1, col2 = st.columns([1, 2])

                # Extract YouTube video ID from thumbnail URL
                video_id = video['thumbnail'].split('/vi/')[1].split('/')[0]

                youtube_link = f"https://www.youtube.com/watch?v={video_id}"

                # Display the thumbnail as a clickable image
                with col1:
                    st.markdown(
                        f'<a href="{youtube_link}" target="_blank">'
                        f'<img src="{video["thumbnail"]}" width="200" style="border-radius: 8px;">'
                        f'</a>',
                        unsafe_allow_html=True
                    )

                # Display video details in the second column
                with col2:
                    # Main title and subheader for short title
                    st.markdown(
                        f'<a href="{youtube_link}" target="_blank" style="text-decoration: none; color: #2b7a78; font-size: 18px;">'
                        f'{video["title"]}'
                        f'</a>',
                        unsafe_allow_html=True
                    )
                    #display the length of the video
                    if(int(video['length']/60)!=0) : # case length under one minute
                        st.write(f"**Length:** {int(video['length']/60)} min {int(video['length']%60)} sec ")
                    else : # case length more than one minute
                         st.write(f"**Length:** {int(video['length']%60)} sec ")
                    
                    st.write(f"**Rating:** {video['rating']:.2f}")
                    st.write(f"**Views:** {video['views']:,}")  # Format views with commas 
                     
if option == "talk to chatbot" :
    st.header("💬 Talk to Chatbot")
    with st.form("recipe_form"):
    # Text input for recipe search (e.g., "donut recipes")
        prompt = st.text_input("Enter prompt ", value="i want a donut recipe")
        old_context_id = st.text_input("Enter conversion ID ")
        context_id = str(uuid.uuid4())
        # Submit button for the form
        submit_button = st.form_submit_button("Search")

    if submit_button:
        if not(old_context_id):
            st.markdown(
    f"""
    <div style="background-color: #ffcccc; padding: 10px; border-radius: 5px;">
        <strong>This is your conversation ID. Use it if you want to continue the current conversation:</strong> <br> 
        <span style="color: #b30000;">{context_id}</span>
    </div>
    """,
    unsafe_allow_html=True
)
            response=talk_to_chatbot(api_key,prompt,context_id)
        else :
            response=talk_to_chatbot(api_key,prompt,old_context_id)

        st.write(response["answerText"])
        if (len(response["media"])>0):
                
                for suggestion in response["media"] : 
                    col1, col2 = st.columns([1, 2])  

                    # Display the image in the first column
                    with col1:
                        st.markdown(
                        
                            f'<img src="{suggestion['image']}" width="200" style="border-radius: 8px; margin-bottom: 15px;">'
                            ,
                            unsafe_allow_html=True
                        )
    
                    with col2:
                        st.write(f"**{suggestion['title']}**")
                        match = re.search(r'-(\d+)$',suggestion['link'])
                        recipe_id = match.group(1)
                        st.write(recipe_id)
                        with st.expander(label="Details"):
                            info=search_recipes_summarize(api_key, recipe_id)
                            # Display preparation and cooking time
                            show_details(info)
        else :
             st.write("there is no suggestions for your request try another one")

        
