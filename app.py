import streamlit as st
from crew import crew

# Streamlit UI
st.title('YouTube Latest Videos and Blogs Search')

# Input from the user
topic = st.text_input('Enter the topic you want the latest videos and blogs for:', '')

if topic:
    # Inform the user about the search for the latest video
    st.write(f"Searching for the latest YouTube videos and blogs related to '{topic}'...")
    ## start the task execution process with enhanced feedback
    result=crew.kickoff(inputs={'topic':topic})
    # Display the generated blog post
    st.markdown("### Results")
    st.write(result)

