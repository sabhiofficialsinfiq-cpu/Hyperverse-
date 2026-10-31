import streamlit as st

# 1. Page Configuration (Browser tab title and layout)
st.set_page_config(page_title="Hyperverse", page_icon="🌌", layout="centered")

# 2. Custom CSS for Mobile Look & Dark Mode (UI/UX Magic)
st.markdown("""
    <style>
        /* Hide Streamlit default header, footer, and menu */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Set Dark Background for the whole app */
        .stApp {
            background-color: #0a0a0a;
        }
        
        /* Force Mobile Width (Like a Phone Screen) */
        .block-container {
            max-width: 400px !important; /* Mobile screen width */
            padding-top: 1rem !important;
            padding-bottom: 5rem !important; /* Space for bottom nav */
            margin: auto;
            border: 1px solid #222;
            border-radius: 20px;
            background-color: #000000;
            box-shadow: 0 4px 20px rgba(255, 255, 255, 0.05);
        }
        
        /* Text and Header Styling */
        h1, h2, h3, p, span, div {
            color: #ffffff !important;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        /* Top Navigation Bar Styling (Instagram Style) */
        .top-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 0px;
            border-bottom: 1px solid #222;
            margin-bottom: 15px;
        }
        .top-nav h2 {
            margin: 0;
            font-size: 22px;
            font-weight: 700;
            letter-spacing: 0.5px;
        }

        /* Streamlit Tabs Styling for the Chat/Preview Toggle */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            background-color: #1a1a1a;
            padding: 5px;
            border-radius: 20px;
            justify-content: center;
        }
        .stTabs [data-baseweb="tab"] {
            height: 35px;
            border-radius: 15px;
            padding: 0px 20px;
            background-color: transparent;
            color: gray;
        }
        .stTabs [aria-selected="true"] {
            background-color: #e1306c !important; /* Instagram Pink */
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3. TOP HEADER (Instagram Style)
st.markdown("""
    <div class="top-nav">
        <h2>Hyperverse</h2>
        <div style="font-size: 20px; cursor: pointer;">✉️</div>
    </div>
""", unsafe_allow_html=True)

# 4. CENTER TOGGLE (The Core Feature)
# We use tabs to create that toggle effect
tab1, tab2 = st.tabs(["💬 Chat", "▶️ Preview"])

# --- TAB 1: CHAT (WhatsApp + Instagram DM) ---
with tab1:
    st.write("### Direct Chats")
    
    # Placeholder for Chat List
    st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 15px;">
            <div style="width: 50px; height: 50px; border-radius: 50%; background-color: #333; margin-right: 15px;"></div>
            <div>
                <div style="font-weight: bold; font-size: 16px;">Aria Nakamura</div>
                <div style="color: gray; font-size: 14px;">Sent 4+ new messages</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 15px;">
            <div style="width: 50px; height: 50px; border-radius: 50%; background-color: #333; margin-right: 15px;"></div>
            <div>
                <div style="font-weight: bold; font-size: 16px;">Leo Grant</div>
                <div style="color: gray; font-size: 14px;">Sent you the raw shots</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- TAB 2: PREVIEW (The Reels/Feed) ---
with tab2:
    st.write("### Feed / Reels")
    st.info("Coming Soon: Reels and Video Streaming Feed!")

# 5. BOTTOM NAVIGATION (Mockup)
st.markdown("""
    <div style="position: fixed; bottom: 20px; width: 100%; max-width: 400px; display: flex; justify-content: space-around; padding: 10px; background-color: #000000; border-top: 1px solid #222;">
        <span style="font-size: 24px; cursor: pointer;">🏠</span>
        <span style="font-size: 24px; cursor: pointer;">🔍</span>
        <span style="font-size: 24px; cursor: pointer;">🎬</span>
        <span style="font-size: 24px; cursor: pointer;">👤</span>
    </div>
""", unsafe_allow_html=True)
