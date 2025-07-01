import streamlit as st
import pandas as pd
df=pd.read_csv("ifood_new.csv")
st.markdown(
    """
    <style>
    /* Change Sidebar Background */
    [data-testid="stSidebar"] {
        background-color: #0a0a0a;
        padding: 20px;
    }

    /* Increase size of Sidebar Title */
    .sidebar-title {
        font-size: 30px;
        font-weight: bold;
        text-align: center;
        color: #FF5733;
    }

    /* Increase size of Sidebar Radio Button Options */
    section[data-testid="stSidebar"] label {
        font-size: 24px !important;
        font-weight: bold;
    }

    /* Increase spacing between radio options */
    div[data-testid="stRadio"] > div {
        gap: 20px !important;
    }

    /* Increase size of Sidebar Selectbox */
    div[data-testid="stSelectbox"] label {
        font-size: 24px !important;
        font-weight: bold;
    }
    div[data-testid="stSelectbox"] select {
        font-size: 22px !important;
        padding: 10px;
    }

    /* Make Sidebar Buttons Larger */
    .big-button {
        width: 100%;
        height: 70px;
        font-size: 24px;
        font-weight: bold;
        border-radius: 10px;
        margin: 10px 0;
        background-color: #FF5733;
        color: white;
        border: none;
    }
    .big-button:hover {
        background-color: #E14D2A;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Title

st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://as2.ftcdn.net/jpg/02/62/69/89/1000_F_262698994_fCURbbW76EHXZu7P17CsU4lc6XnsVRs0.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        height: 100vh;
    }
    </style>
    """, unsafe_allow_html=True)
st.markdown("""                           
    <style>
    /* Custom button styling */
    .custom-button {
        background-color: #63dbeb;
        color: white;
        font-weight: bold;
        border: 2px solid #ffa500;        
        border-radius: 12px;
        padding: 1em 2em; /* Larger padding for bigger button */
        margin: 10px 5px;
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 20px; /* Set font size to 50px */
    }
    
    
    .custom-button:hover {
        background-color: #63dbeb;
        color: white;
        box-shadow: 0 0 10px #ff9900, 0 0 20px #ff9900, 0 0 30px #ff9900;
    }

    /* Streamlit button styling */
    div.stButton > button:first-child {
        background-color: #f56b53;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        padding: 2px 2px; /* Larger padding for bigger button */
        margin: 5px;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        font-size: 20px; /* Increase font size for larger text */
        width: 170px;
        height: 60px;
    }

    div.stButton > button:first-child:hover {
        background-color: #63dbeb;
        color: white;
        box-shadow: 0 0 15px #45a049, 0 0 25px #45a049, 0 0 35px #45a049;
    }
    .st-emotion-cache-atejua egexzqm0>{
      font-size:100px;
            }
    </style>
""", unsafe_allow_html=True)
# st.sidebar.markdown("<p class='sidebar-title'>🍴 FlavourMania</p>", unsafe_allow_html=True)

# # Bigger Sidebar Radio Button Options
# options =(
    
#     "🏠 Home","🍛 Main Course", "🍕 Snacks", "🍰 Desserts", "🍹 Shakes"
# )
# option=st.sidebar.radio("What you want to explore?:",options)

# query_params = st.query_params()
recipe_name = st.session_state.get("recipe_name", None)
ing=st.session_state.get("ing_name", None)
# dess=st.session_state.get("dess",None)
# if not st.session_state.get("navigated", False):
#     st.switch_page("home.py")
# else:
#     st.session_state.navigated = False

# if recipe_name:
#     recipe_data = df[df['name']==recipe_name].iloc[0]
#     st.title(f":red[Recipe of {recipe_data['name']}]")
#     st.write(recipe_data['procedure'])

# else:
#     st.write("")

if not recipe_name:
    st.warning("No recipe selected.")
    st.switch_page("new.py")

recipe_data = df[df['name'] == recipe_name].iloc[0]
ing_data=df[df['ingredients'] == ing].iloc[0]
# dess=df[df==dess].iloc[0]
# Show recipe and ingr
st.title(f":blue[{recipe_data['name']}]")
st.subheader(":red[Ingredients Required:]")
st.write(ing_data['ingredients'])
st.subheader(f":red[Recipe:]")
st.write(recipe_data['procedure'])
# st.button("⬅️ Back",on_click=go_back )

# Reset navigation flag
st.session_state.navigated = False
# if options=='🍰 Desserts':
#    st.session_state.navigated = True
#    st.switch_page("pages/dessert.py") 
# if st.button("⬅️ Back",key='back'):
#     st.session_state.navigated = True
#     st.switch_page("pages/dessert.py") 