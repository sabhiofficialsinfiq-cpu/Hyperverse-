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
import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Hyperverse", page_icon="🌌", layout="centered")

# 2. Custom CSS for Mobile Look & Dark Mode
st.markdown("""
    <style>
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* App Background */
        .stApp { background-color: #0a0a0a; }
        
        /* Mobile Container */
        .block-container {
            max-width: 400px !important;
            padding-top: 1rem !important;
            padding-bottom: 6rem !important; /* Space for bottom nav */
            margin: auto;
            border: 1px solid #222;
            border-radius: 20px;
            background-color: #000000;
        }
        
        /* Global Text */
        h1, h2, h3, p, span, div {
            color: #ffffff !important;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        /* Top Navigation Bar (Instagram Style) */
        .top-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 0px;
            border-bottom: 1px solid #222;
            margin-bottom: 15px;
        }
        .top-nav h2 { margin: 0; font-size: 22px; font-weight: 700; }

        /* Streamlit Tabs Styling (The Toggle) */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            background-color: #1a1a1a;
            padding: 5px;
            border-radius: 20px;
            justify-content: center;
            margin-bottom: 15px;
        }
        .stTabs [data-baseweb="tab"] {
            height: 35px;
            border-radius: 15px;
            padding: 0px 20px;
            background-color: transparent;
            color: gray;
            font-weight: bold;
        }
        .stTabs [aria-selected="true"] {
            background-color: #e1306c !important; /* Instagram Pink */
            color: white !important;
        }

        /* Chat List Item Styling */
        .chat-row {
            display: flex;
            align-items: center;
            padding: 10px 0;
            border-bottom: 1px solid #111;
        }
        .avatar {
            width: 50px; height: 50px;
            border-radius: 50%;
            background-color: #333;
            margin-right: 15px;
            object-fit: cover;
        }
        .chat-info { flex-grow: 1; }
        .chat-name { font-weight: 600; font-size: 15px; margin-bottom: 3px; }
        .chat-msg { color: #888 !important; font-size: 13px; }
        
        /* IG Blue Dot */
        .blue-dot {
            width: 8px; height: 8px;
            background-color: #0095f6;
            border-radius: 50%;
            margin-left: 10px;
        }
        
        /* WhatsApp Green Ticks & Time */
        .wa-msg { display: flex; align-items: center; color: #888 !important; font-size: 13px; }
        .green-tick { color: #25D366; font-size: 14px; margin-right: 4px; }
        
        /* Filter Pills (WhatsApp) */
        .filter-pill {
            background-color: #1a1a1a;
            color: #ccc !important;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 12px;
            margin-right: 8px;
            display: inline-block;
        }
        .filter-pill.active { background-color: #25D366; color: black !important; font-weight: bold; }

        /* Bottom Nav */
        .bottom-nav {
            position: fixed; bottom: 15px; 
            width: 100%; max-width: 380px; 
            display: flex; justify-content: space-around; 
            padding: 15px 0; background-color: #000000; 
            border-top: 1px solid #222; border-radius: 20px;
        }
        .nav-icon { font-size: 22px; cursor: pointer; }
    </style>
""", unsafe_allow_html=True)

# 3. TOP HEADER
st.markdown("""
    <div class="top-nav">
        <h2>Hyperverse</h2>
        <div style="font-size: 20px; cursor: pointer;">✏️</div> <!-- Pencil Icon -->
    </div>
""", unsafe_allow_html=True)

# 4. TABS
tab1, tab2 = st.tabs(["💬 Chat", "▶️ Preview"])

with tab1:
    # --- TOP HALF: INSTAGRAM DM STYLE ---
    st.markdown("<div style='font-size: 14px; color: gray; margin-bottom: 5px;'>Notes</div>", unsafe_allow_html=True)
    # Notes Row (Placeholder)
    st.markdown("""
        <div style="display: flex; gap: 15px; margin-bottom: 20px;">
            <div style="text-align: center;">
                <img src="https://i.pravatar.cc/150?img=11" class="avatar" style="border: 2px solid #555;">
                <div style="font-size: 11px; margin-top: 5px;">Your note</div>
            </div>
            <div style="text-align: center;">
                <img src="https://i.pravatar.cc/150?img=5" class="avatar" style="border: 2px solid #e1306c;">
                <div style="font-size: 11px; margin-top: 5px;">Dvi</div>
            </div>
            <div style="text-align: center;">
                <img src="https://i.pravatar.cc/150?img=12" class="avatar" style="border: 2px solid #e1306c;">
                <div style="font-size: 11px; margin-top: 5px;">Map</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='display: flex; justify-content: space-between; align-items: center;'><h3>Messages</h3><span style='color: #0095f6; font-size: 14px;'>Requests</span></div>", unsafe_allow_html=True)
    
    # IG Message List
    st.markdown("""
        <div class="chat-row">
            <img src="https://i.pravatar.cc/150?img=33" class="avatar">
            <div class="chat-info">
                <div class="chat-name">alex_dev <span style="color:gray; font-size:11px;">· 12h</span></div>
                <div class="chat-msg">Sent 4+ new messages</div>
            </div>
            <div class="blue-dot"></div>
        </div>
        <div class="chat-row">
            <img src="https://i.pravatar.cc/150?img=47" class="avatar">
            <div class="chat-info">
                <div class="chat-name">sarah_smith <span style="color:gray; font-size:11px;">· 1d</span></div>
                <div class="chat-msg">Loved your recent reel!</div>
            </div>
            <div class="blue-dot"></div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><hr style='border-color: #333;'><br>", unsafe_allow_html=True) # Divider

    # --- BOTTOM HALF: WHATSAPP STYLE ---
    st.markdown("<h3>Hyper Chat</h3>", unsafe_allow_html=True)
    
    # Filter Pills
    st.markdown("""
        <div style="margin-bottom: 15px;">
            <span class="filter-pill active">All</span>
            <span class="filter-pill">Unread 21</span>
            <span class="filter-pill">Favourites</span>
            <span class="filter-pill">Groups</span>
        </div>
    """, unsafe_allow_html=True)

    # WA Message List (Green Ticks)
    st.markdown("""
        <div class="chat-row">
            <img src="https://i.pravatar.cc/150?img=60" class="avatar">
            <div class="chat-info">
                <div class="chat-name">mike_tyson <span style="float:right; color:gray; font-size:11px;">11:42 AM</span></div>
                <div class="wa-msg"><span class="green-tick">✓✓</span> Sent the project files</div>
            </div>
        </div>
        <div class="chat-row">
            <img src="https://i.pravatar.cc/150?img=59" class="avatar">
            <div class="chat-info">
                <div class="chat-name">dev_team <span style="float:right; color:gray; font-size:11px;">Yesterday</span></div>
                <div class="wa-msg"><span class="green-tick">✓✓</span> Meeting at 10 AM tomorrow</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with tab2:
    st.write("### Feed / Reels")
    st.info("Coming Soon: Reels and Video Streaming Feed!")

# 5. BOTTOM NAVIGATION
st.markdown("""
    <div class="bottom-nav">
        <span class="nav-icon">🏠</span>
        <span class="nav-icon">🔍</span>
        <span class="nav-icon">🎬</span>
        <span class="nav-icon">👤</span>
    </div>
""", unsafe_allow_html=True)
import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Hyperverse", page_icon="🌌", layout="centered")

# 2. Custom CSS for Mobile Look & Dark Mode
st.markdown("""
    <style>
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* App Background */
        .stApp { background-color: #0a0a0a; }
        
        /* Mobile Container */
        .block-container {
            max-width: 400px !important;
            padding-top: 1rem !important;
            padding-bottom: 6rem !important;
            margin: auto;
            border: 1px solid #222;
            border-radius: 20px;
            background-color: #000000;
        }
        
        /* Global Text */
        h1, h2, h3, p, span, div {
            color: #ffffff !important;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        /* Top Navigation Bar */
        .top-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 0px;
            border-bottom: 1px solid #222;
            margin-bottom: 15px;
        }
        .top-nav h2 { margin: 0; font-size: 22px; font-weight: 700; }

        /* Tabs Styling (The Toggle) */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            background-color: #1a1a1a;
            padding: 5px;
            border-radius: 20px;
            justify-content: center;
            margin-bottom: 15px;
        }
        .stTabs [data-baseweb="tab"] {
            height: 35px;
            border-radius: 15px;
            padding: 0px 20px;
            background-color: transparent;
            color: gray;
            font-weight: bold;
        }
        .stTabs [aria-selected="true"] {
            background-color: #e1306c !important; /* Instagram Pink */
            color: white !important;
        }

        /* Chat List Item Styling */
        .chat-row {
            display: flex;
            align-items: center;
            padding: 10px 0;
            border-bottom: 1px solid #111;
        }
        .avatar {
            width: 50px; height: 50px;
            border-radius: 50%;
            background-color: #333;
            margin-right: 15px;
            object-fit: cover;
        }
        .chat-info { flex-grow: 1; }
        .chat-name { font-weight: 600; font-size: 15px; margin-bottom: 3px; }
        .chat-msg { color: #888 !important; font-size: 13px; }
        
        /* IG Blue Dot */
        .blue-dot {
            width: 8px; height: 8px;
            background-color: #0095f6;
            border-radius: 50%;
            margin-left: 10px;
        }
        
        /* WhatsApp Green Ticks & Time */
        .wa-msg { display: flex; align-items: center; color: #888 !important; font-size: 13px; }
        .green-tick { color: #25D366; font-size: 14px; margin-right: 4px; }
        
        /* Filter Pills */
        .filter-pill {
            background-color: #1a1a1a;
            color: #ccc !important;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 12px;
            margin-right: 8px;
            display: inline-block;
        }
        .filter-pill.active { background-color: #25D366; color: black !important; font-weight: bold; }

        /* --- NEW: FEED CARD STYLING (INSTAGRAM) --- */
        .feed-card {
            background-color: #111;
            border-radius: 15px;
            margin-bottom: 20px;
            overflow: hidden;
            border: 1px solid #222;
        }
        .feed-header {
            display: flex;
            align-items: center;
            padding: 10px 15px;
        }
        .feed-header img { width: 35px; height: 35px; margin-right: 10px; }
        .feed-header-text { font-weight: 600; font-size: 14px; }
        .feed-header-text span { color: #888; font-size: 12px; font-weight: normal; }
        .feed-media {
            width: 100%;
            height: 350px;
            background-color: #222;
            object-fit: cover;
        }
        .feed-actions {
            padding: 10px 15px;
            font-size: 22px;
            display: flex;
            gap: 15px;
        }
        .feed-likes {
            padding: 0 15px;
            font-weight: 600;
            font-size: 14px;
        }
        .feed-caption {
            padding: 5px 15px 15px 15px;
            font-size: 14px;
        }

        /* Bottom Nav */
        .bottom-nav {
            position: fixed; bottom: 15px; left: 50%; transform: translateX(-50%);
            width: 100%; max-width: 380px; 
            display: flex; justify-content: space-around; align-items: center;
            padding: 15px 0; background-color: #000000; 
            border-top: 1px solid #222; border-radius: 20px;
            box-shadow: 0 -5px 15px rgba(0,0,0,0.5);
        }
        .nav-icon { font-size: 22px; cursor: pointer; }
        
        /* Create (+) Button */
        .create-btn {
            background-color: #e1306c;
            color: white;
            width: 40px; height: 40px;
            border-radius: 12px;
            display: flex; justify-content: center; align-items: center;
            font-size: 24px; font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# 3. TOP HEADER
st.markdown("""
    <div class="top-nav">
        <h2>Hyperverse</h2>
        <div style="font-size: 20px; cursor: pointer;">✏️</div>
    </div>
""", unsafe_allow_html=True)

# 4. TABS
tab1, tab2 = st.tabs(["💬 Chat", "▶️ Preview"])

with tab1:
    # (Existing Chat UI code remains the same)
    st.markdown("<div style='font-size: 14px; color: gray; margin-bottom: 5px;'>Notes</div>", unsafe_allow_html=True)
    st.markdown("""
        <div style="display: flex; gap: 15px; margin-bottom: 20px;">
            <div style="text-align: center;"><img src="https://i.pravatar.cc/150?img=11" class="avatar" style="border: 2px solid #555;"><div style="font-size: 11px; margin-top: 5px;">Your note</div></div>
            <div style="text-align: center;"><img src="https://i.pravatar.cc/150?img=5" class="avatar" style="border: 2px solid #e1306c;"><div style="font-size: 11px; margin-top: 5px;">Dvi</div></div>
            <div style="text-align: center;"><img src="https://i.pravatar.cc/150?img=12" class="avatar" style="border: 2px solid #e1306c;"><div style="font-size: 11px; margin-top: 5px;">Map</div></div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='display: flex; justify-content: space-between; align-items: center;'><h3>Messages</h3><span style='color: #0095f6; font-size: 14px;'>Requests</span></div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="chat-row">
            <img src="https://i.pravatar.cc/150?img=33" class="avatar">
            <div class="chat-info">
                <div class="chat-name">alex_dev <span style="color:gray; font-size:11px;">· 12h</span></div>
                <div class="chat-msg">Sent 4+ new messages</div>
            </div>
            <div class="blue-dot"></div>
        </div>
        <div class="chat-row">
            <img src="https://i.pravatar.cc/150?img=47" class="avatar">
            <div class="chat-info">
                <div class="chat-name">sarah_smith <span style="color:gray; font-size:11px;">· 1d</span></div>
                <div class="chat-msg">Loved your recent reel!</div>
            </div>
            <div class="blue-dot"></div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><hr style='border-color: #333;'><br>", unsafe_allow_html=True)

    st.markdown("<h3>Hyper Chat</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div style="margin-bottom: 15px;">
            <span class="filter-pill active">All</span>
            <span class="filter-pill">Unread 21</span>
            <span class="filter-pill">Favourites</span>
            <span class="filter-pill">Groups</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="chat-row">
            <img src="https://i.pravatar.cc/150?img=60" class="avatar">
            <div class="chat-info">
                <div class="chat-name">mike_tyson <span style="float:right; color:gray; font-size:11px;">11:42 AM</span></div>
                <div class="wa-msg"><span class="green-tick">✓✓</span> Sent the project files</div>
            </div>
        </div>
        <div class="chat-row">
            <img src="https://i.pravatar.cc/150?img=59" class="avatar">
            <div class="chat-info">
                <div class="chat-name">dev_team <span style="float:right; color:gray; font-size:11px;">Yesterday</span></div>
                <div class="wa-msg"><span class="green-tick">✓✓</span> Meeting at 10 AM tomorrow</div>
            </div>
        </div>
    """, unsafe_allow_html=True)


# --- NEW: TAB 2 (PREVIEW/REELS FEED) ---
with tab2:
    # Feed Post 1
    st.markdown("""
        <div class="feed-card">
            <div class="feed-header">
                <img src="https://i.pravatar.cc/150?img=33" class="avatar">
                <div class="feed-header-text">aria.codes <span>· 34m</span></div>
            </div>
            <!-- Dummy Image for Feed -->
            <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=800&auto=format&fit=crop" class="feed-media">
            <div class="feed-actions">
                <span>❤️</span> <span>💬</span> <span>✈️</span>
            </div>
            <div class="feed-likes">1,245 likes</div>
            <div class="feed-caption"><b>aria.codes</b> Building the future of social media. 🚀 #Hyperverse #Tech</div>
        </div>
    """, unsafe_allow_html=True)

    # Feed Post 2 (Reel Style)
    st.markdown("""
        <div class="feed-card">
            <div class="feed-header">
                <img src="https://i.pravatar.cc/150?img=12" class="avatar">
                <div class="feed-header-text">leo.frames <span>· 2h</span></div>
            </div>
            <!-- Dummy Image for Reel -->
            <img src="https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?q=80&w=800&auto=format&fit=crop" class="feed-media">
            <div class="feed-actions">
                <span>❤️</span> <span>💬</span> <span>✈️</span>
            </div>
            <div class="feed-likes">852 likes</div>
            <div class="feed-caption"><b>leo.frames</b> Golden hour in the mountains. 🏔️✨</div>
        </div>
    """, unsafe_allow_html=True)


# 5. BOTTOM NAVIGATION (Updated with Create Button)
st.markdown("""
    <div class="bottom-nav">
        <span class="nav-icon">🏠</span>
        <span class="nav-icon">🔍</span>
        <div class="create-btn">+</div>
        <span class="nav-icon">🎬</span>
        <span class="nav-icon">👤</span>
    </div>
""", unsafe_allow_html=True)

import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Hyperverse", page_icon="🌌", layout="centered")

# 2. Session State for Navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# 3. Custom CSS for Mobile Look & Dark Mode
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        .stApp { background-color: #0a0a0a; }
        
        .block-container {
            max-width: 400px !important;
            padding-top: 1rem !important;
            padding-bottom: 6rem !important;
            margin: auto;
            border: 1px solid #222;
            border-radius: 20px;
            background-color: #000000;
        }
        
        h1, h2, h3, p, span, div {
            color: #ffffff !important;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        /* Top Nav */
        .top-nav {
            display: flex; justify-content: space-between; align-items: center;
            padding: 10px 0px; border-bottom: 1px solid #222; margin-bottom: 15px;
        }
        .top-nav h2 { margin: 0; font-size: 22px; font-weight: 700; }

        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px; background-color: #1a1a1a; padding: 5px;
            border-radius: 20px; justify-content: center; margin-bottom: 15px;
        }
        .stTabs [data-baseweb="tab"] {
            height: 35px; border-radius: 15px; padding: 0px 20px;
            background-color: transparent; color: gray; font-weight: bold;
        }
        .stTabs [aria-selected="true"] {
            background-color: #e1306c !important; color: white !important;
        }

        /* Chat Styles */
        .chat-row { display: flex; align-items: center; padding: 10px 0; border-bottom: 1px solid #111; }
        .avatar { width: 50px; height: 50px; border-radius: 50%; background-color: #333; margin-right: 15px; object-fit: cover;}
        .chat-info { flex-grow: 1; }
        .chat-name { font-weight: 600; font-size: 15px; margin-bottom: 3px; }
        .chat-msg { color: #888 !important; font-size: 13px; }
        .blue-dot { width: 8px; height: 8px; background-color: #0095f6; border-radius: 50%; margin-left: 10px; }
        .wa-msg { display: flex; align-items: center; color: #888 !important; font-size: 13px; }
        .green-tick { color: #25D366; font-size: 14px; margin-right: 4px; }
        .filter-pill { background-color: #1a1a1a; color: #ccc !important; padding: 5px 12px; border-radius: 15px; font-size: 12px; margin-right: 8px; display: inline-block;}
        .filter-pill.active { background-color: #25D366; color: black !important; font-weight: bold; }

        /* Feed Styles */
        .feed-card { background-color: #111; border-radius: 15px; margin-bottom: 20px; overflow: hidden; border: 1px solid #222; }
        .feed-header { display: flex; align-items: center; padding: 10px 15px; }
        .feed-header-text { font-weight: 600; font-size: 14px; }
        .feed-header-text span { color: #888; font-size: 12px; font-weight: normal; }
        .feed-media { width: 100%; height: 350px; background-color: #222; object-fit: cover; }
        .feed-actions { padding: 10px 15px; font-size: 22px; display: flex; gap: 15px; }
        .feed-likes { padding: 0 15px; font-weight: 600; font-size: 14px; }
        .feed-caption { padding: 5px 15px 15px 15px; font-size: 14px; }

        /* Profile Styles */
        .profile-header { text-align: center; padding: 20px 0; }
        .profile-avatar { width: 90px; height: 90px; border-radius: 50%; border: 3px solid #e1306c; margin-bottom: 15px; }
        .profile-stats { display: flex; justify-content: center; gap: 30px; margin-bottom: 15px; }
        .stat-item { text-align: center; }
        .stat-value { font-size: 18px; font-weight: bold; display: block; }
        .stat-label { font-size: 12px; color: #888 !important; }
        .profile-bio { font-size: 14px; padding: 0 20px; margin-bottom: 20px; }
        .grid-img { width: 100%; aspect-ratio: 1/1; object-fit: cover; border-radius: 5px; }

        /* Interactive Bottom Nav Buttons */
        .stButton > button {
            background-color: transparent !important;
            border: none !important;
            color: white !important;
            font-size: 20px !important;
            padding: 0 !important;
            box-shadow: none !important;
        }
        .stButton > button:hover { color: #e1306c !important; }
        
        /* Bottom Nav Container */
        div[data-testid="stHorizontalBlock"] {
            position: fixed; bottom: 0; left: 50%; transform: translateX(-50%);
            width: 100%; max-width: 400px; 
            background-color: #000000; 
            border-top: 1px solid #222; 
            padding: 10px 0px;
            z-index: 999;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================
if st.session_state.current_page == "Home":
    st.markdown("""
        <div class="top-nav">
            <h2>Hyperverse</h2>
            <div style="font-size: 20px; cursor: pointer;">✏️</div>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# PAGE CONTENT
# ==========================================

# --- HOME PAGE (Chat & Preview) ---
if st.session_state.current_page == "Home":
    tab1, tab2 = st.tabs(["💬 Chat", "▶️ Preview"])

    with tab1:
        # (Existing Chat UI)
        st.markdown("<div style='font-size: 14px; color: gray; margin-bottom: 5px;'>Notes</div>", unsafe_allow_html=True)
        st.markdown("""
            <div style="display: flex; gap: 15px; margin-bottom: 20px;">
                <div style="text-align: center;"><img src="https://i.pravatar.cc/150?img=11" class="avatar" style="border: 2px solid #555;"><div style="font-size: 11px; margin-top: 5px;">Your note</div></div>
                <div style="text-align: center;"><img src="https://i.pravatar.cc/150?img=5" class="avatar" style="border: 2px solid #e1306c;"><div style="font-size: 11px; margin-top: 5px;">Dvi</div></div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='display: flex; justify-content: space-between;'><h3>Messages</h3><span style='color: #0095f6; font-size: 14px;'>Requests</span></div>", unsafe_allow_html=True)
        st.markdown("""
            <div class="chat-row">
                <img src="https://i.pravatar.cc/150?img=33" class="avatar">
                <div class="chat-info">
                    <div class="chat-name">alex_dev <span style="color:gray; font-size:11px;">· 12h</span></div>
                    <div class="chat-msg">Sent 4+ new messages</div>
                </div>
                <div class="blue-dot"></div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<br><hr style='border-color: #333;'><br>", unsafe_allow_html=True)
        st.markdown("<h3>Hyper Chat</h3>", unsafe_allow_html=True)
        st.markdown("""
            <div style="margin-bottom: 15px;">
                <span class="filter-pill active">All</span>
                <span class="filter-pill">Unread 21</span>
            </div>
            <div class="chat-row">
                <img src="https://i.pravatar.cc/150?img=60" class="avatar">
                <div class="chat-info">
                    <div class="chat-name">mike_tyson <span style="float:right; color:gray; font-size:11px;">11:42 AM</span></div>
                    <div class="wa-msg"><span class="green-tick">✓✓</span> Sent the project files</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with tab2:
        # (Existing Feed UI)
        st.markdown("""
            <div class="feed-card">
                <div class="feed-header">
                    <img src="https://i.pravatar.cc/150?img=33" class="avatar">
                    <div class="feed-header-text">aria.codes <span>· 34m</span></div>
                </div>
                <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=800&auto=format&fit=crop" class="feed-media">
                <div class="feed-actions"><span>❤️</span> <span>💬</span> <span>✈️</span></div>
                <div class="feed-likes">1,245 likes</div>
                <div class="feed-caption"><b>aria.codes</b> Building the future of social media. 🚀</div>
            </div>
        """, unsafe_allow_html=True)


# --- PROFILE PAGE ---
elif st.session_state.current_page == "Profile":
    st.markdown("<h2 style='text-align: center; border-bottom: 1px solid #222; padding-bottom: 10px;'>bharat_1297</h2>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="profile-header">
            <img src="https://i.pravatar.cc/150?img=11" class="profile-avatar">
            <h3 style="margin: 0;">Bharat Kumar</h3>
            <p style="color: #888 !important; font-size: 14px;">@bharat_1297</p>
            
            <div class="profile-stats">
                <div class="stat-item"><span class="stat-value">120</span><span class="stat-label">Posts</span></div>
                <div class="stat-item"><span class="stat-value">15.4K</span><span class="stat-label">Followers</span></div>
                <div class="stat-item"><span class="stat-value">340</span><span class="stat-label">Following</span></div>
            </div>
            
            <div class="profile-bio">
                Building Hyperverse App 🌌 | Tech Enthusiast | UI/UX Designer
            </div>
        </div>
        <hr style='border-color: #222;'>
        <h4 style="margin-bottom: 10px;">My Posts</h4>
    """, unsafe_allow_html=True)
    
    # Grid of Images (Placeholder for Posts)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<img src='https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)
    with col2:
        st.markdown("<img src='https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)
    with col3:
        st.markdown("<img src='https://images.unsplash.com/photo-1511556820780-d912e42b4980?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)

# --- SEARCH PAGE ---
elif st.session_state.current_page == "Search":
    st.markdown("<h2 style='text-align: center;'>Search</h2>", unsafe_allow_html=True)
    st.text_input("Search users, reels, or music...", placeholder="Search...")
    st.info("Trending searches coming soon!")


# ==========================================
# BOTTOM NAVIGATION (Interactive)
# ==========================================
st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True) # Spacer

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🏠", key="nav_home", use_container_width=True):
        st.session_state.current_page = "Home"
        st.rerun()

with col2:
    if st.button("🔍", key="nav_search", use_container_width=True):
        st.session_state.current_page = "Search"
        st.rerun()

with col3:
    if st.button("➕", key="nav_create", use_container_width=True):
        st.toast("Create feature coming soon!")

with col4:
    if st.button("🎬", key="nav_reels", use_container_width=True):
        st.toast("Reels feature coming soon!")

with col5:
    if st.button("👤", key="nav_profile", use_container_width=True):
        st.session_state.current_page = "Profile"
        st.rerun()
import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Hyperverse", page_icon="🌌", layout="centered")

# 2. Session State for Navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# 3. Custom CSS
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        .stApp { background-color: #0a0a0a; }
        
        .block-container {
            max-width: 400px !important;
            padding-top: 1rem !important;
            padding-bottom: 6rem !important;
            margin: auto;
            border: 1px solid #222;
            border-radius: 20px;
            background-color: #000000;
        }
        
        h1, h2, h3, p, span, div {
            color: #ffffff !important;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        /* Top Nav */
        .top-nav {
            display: flex; justify-content: space-between; align-items: center;
            padding: 10px 0px; border-bottom: 1px solid #222; margin-bottom: 15px;
        }
        .top-nav h2 { margin: 0; font-size: 22px; font-weight: 700; }

        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px; background-color: #1a1a1a; padding: 5px;
            border-radius: 20px; justify-content: center; margin-bottom: 15px;
        }
        .stTabs [data-baseweb="tab"] {
            height: 35px; border-radius: 15px; padding: 0px 20px;
            background-color: transparent; color: gray; font-weight: bold;
        }
        .stTabs [aria-selected="true"] {
            background-color: #e1306c !important; color: white !important;
        }

        /* Chat Styles */
        .chat-row { display: flex; align-items: center; padding: 10px 0; border-bottom: 1px solid #111; }
        .avatar { width: 50px; height: 50px; border-radius: 50%; background-color: #333; margin-right: 15px; object-fit: cover;}
        .chat-info { flex-grow: 1; }
        .chat-name { font-weight: 600; font-size: 15px; margin-bottom: 3px; }
        .chat-msg { color: #888 !important; font-size: 13px; }
        .blue-dot { width: 8px; height: 8px; background-color: #0095f6; border-radius: 50%; margin-left: 10px; }
        .wa-msg { display: flex; align-items: center; color: #888 !important; font-size: 13px; }
        .green-tick { color: #25D366; font-size: 14px; margin-right: 4px; }
        .filter-pill { background-color: #1a1a1a; color: #ccc !important; padding: 5px 12px; border-radius: 15px; font-size: 12px; margin-right: 8px; display: inline-block;}
        .filter-pill.active { background-color: #25D366; color: black !important; font-weight: bold; }

        /* Feed Styles */
        .feed-card { background-color: #111; border-radius: 15px; margin-bottom: 20px; overflow: hidden; border: 1px solid #222; }
        .feed-header { display: flex; align-items: center; padding: 10px 15px; }
        .feed-header-text { font-weight: 600; font-size: 14px; }
        .feed-header-text span { color: #888; font-size: 12px; font-weight: normal; }
        .feed-media { width: 100%; height: 350px; background-color: #222; object-fit: cover; }
        .feed-actions { padding: 10px 15px; font-size: 22px; display: flex; gap: 15px; }
        .feed-likes { padding: 0 15px; font-weight: 600; font-size: 14px; }
        .feed-caption { padding: 5px 15px 15px 15px; font-size: 14px; }

        /* Profile Styles */
        .profile-header { text-align: center; padding: 20px 0; }
        .profile-avatar { width: 90px; height: 90px; border-radius: 50%; border: 3px solid #e1306c; margin-bottom: 15px; }
        .profile-stats { display: flex; justify-content: center; gap: 30px; margin-bottom: 15px; }
        .stat-item { text-align: center; }
        .stat-value { font-size: 18px; font-weight: bold; display: block; }
        .stat-label { font-size: 12px; color: #888 !important; }
        .profile-bio { font-size: 14px; padding: 0 20px; margin-bottom: 20px; }
        .grid-img { width: 100%; aspect-ratio: 1/1; object-fit: cover; border-radius: 5px; }

        /* Create Page Styles */
        .create-option {
            background-color: #1a1a1a;
            border: 1px solid #333;
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            margin-bottom: 15px;
            cursor: pointer;
        }
        .create-icon { font-size: 30px; margin-bottom: 10px; display: block; }
        .create-title { font-weight: bold; font-size: 16px; }

        /* Interactive Bottom Nav Buttons */
        .stButton > button {
            background-color: transparent !important;
            border: none !important;
            color: white !important;
            font-size: 20px !important;
            padding: 0 !important;
            box-shadow: none !important;
        }
        .stButton > button:hover { color: #e1306c !important; }
        
        /* Bottom Nav Container */
        div[data-testid="stHorizontalBlock"] {
            position: fixed; bottom: 0; left: 50%; transform: translateX(-50%);
            width: 100%; max-width: 400px; 
            background-color: #000000; 
            border-top: 1px solid #222; 
            padding: 10px 0px;
            z-index: 999;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================
if st.session_state.current_page == "Home":
    st.markdown("""
        <div class="top-nav">
            <h2>Hyperverse</h2>
            <div style="font-size: 20px; cursor: pointer;">✏️</div>
        </div>
    """, unsafe_allow_html=True)
elif st.session_state.current_page == "Create":
    st.markdown("<h2 style='text-align: center; border-bottom: 1px solid #222; padding-bottom: 10px;'>New Post</h2>", unsafe_allow_html=True)
elif st.session_state.current_page == "Discover":
    st.markdown("<h2 style='text-align: center; border-bottom: 1px solid #222; padding-bottom: 10px;'>Discover</h2>", unsafe_allow_html=True)

# ==========================================
# PAGE CONTENT
# ==========================================

# --- HOME PAGE (Chat & Preview) ---
if st.session_state.current_page == "Home":
    tab1, tab2 = st.tabs(["💬 Chat", "▶️ Preview"])

    with tab1:
        st.markdown("<div style='font-size: 14px; color: gray; margin-bottom: 5px;'>Notes</div>", unsafe_allow_html=True)
        st.markdown("""
            <div style="display: flex; gap: 15px; margin-bottom: 20px;">
                <div style="text-align: center;"><img src="https://i.pravatar.cc/150?img=11" class="avatar" style="border: 2px solid #555;"><div style="font-size: 11px; margin-top: 5px;">Your note</div></div>
                <div style="text-align: center;"><img src="https://i.pravatar.cc/150?img=5" class="avatar" style="border: 2px solid #e1306c;"><div style="font-size: 11px; margin-top: 5px;">Dvi</div></div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='display: flex; justify-content: space-between;'><h3>Messages</h3><span style='color: #0095f6; font-size: 14px;'>Requests</span></div>", unsafe_allow_html=True)
        st.markdown("""
            <div class="chat-row">
                <img src="https://i.pravatar.cc/150?img=33" class="avatar">
                <div class="chat-info">
                    <div class="chat-name">alex_dev <span style="color:gray; font-size:11px;">· 12h</span></div>
                    <div class="chat-msg">Sent 4+ new messages</div>
                </div>
                <div class="blue-dot"></div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<br><hr style='border-color: #333;'><br>", unsafe_allow_html=True)
        st.markdown("<h3>Hyper Chat</h3>", unsafe_allow_html=True)
        st.markdown("""
            <div style="margin-bottom: 15px;">
                <span class="filter-pill active">All</span>
                <span class="filter-pill">Unread 21</span>
            </div>
            <div class="chat-row">
                <img src="https://i.pravatar.cc/150?img=60" class="avatar">
                <div class="chat-info">
                    <div class="chat-name">mike_tyson <span style="float:right; color:gray; font-size:11px;">11:42 AM</span></div>
                    <div class="wa-msg"><span class="green-tick">✓✓</span> Sent the project files</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown("""
            <div class="feed-card">
                <div class="feed-header">
                    <img src="https://i.pravatar.cc/150?img=33" class="avatar">
                    <div class="feed-header-text">aria.codes <span>· 34m</span></div>
                </div>
                <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=800&auto=format&fit=crop" class="feed-media">
                <div class="feed-actions"><span>❤️</span> <span>💬</span> <span>✈️</span></div>
                <div class="feed-likes">1,245 likes</div>
                <div class="feed-caption"><b>aria.codes</b> Building the future of social media. 🚀</div>
            </div>
        """, unsafe_allow_html=True)

# --- CREATE PAGE (Place 4) ---
elif st.session_state.current_page == "Create":
    st.write("Choose what you want to create:")
    
    # 2 Columns for Create Options
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="create-option">
                <span class="create-icon">🖼️</span>
                <span class="create-title">New Post</span>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="create-option">
                <span class="create-icon">🎬</span>
                <span class="create-title">Reel</span>
            </div>
        """, unsafe_allow_html=True)
        
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("""
            <div class="create-option">
                <span class="create-icon">📸</span>
                <span class="create-title">Story</span>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
            <div class="create-option">
                <span class="create-icon">🔴</span>
                <span class="create-title">Live</span>
            </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.write("### Upload Media")
    
    # File Uploader
    uploaded_file = st.file_uploader("Choose a photo or video from your album", type=['png', 'jpg', 'jpeg', 'mp4'])
    
    if uploaded_file is not None:
        if uploaded_file.type.startswith('image'):
            st.image(uploaded_file, caption='Preview', use_column_width=True)
        elif uploaded_file.type.startswith('video'):
            st.video(uploaded_file)
            
    st.text_area("Write a caption...", placeholder="What's on your mind?")
    
    if st.button("Share Post", type="primary", use_container_width=True):
        st.success("Post Shared Successfully! (Mockup)")

# --- DISCOVER / SEARCH PAGE (Place 5) ---
elif st.session_state.current_page == "Discover":
    # Filter Pills
    st.markdown("""
        <div style="margin-bottom: 15px;">
            <span class="filter-pill active">Explore</span>
            <span class="filter-pill">Following</span>
            <span class="filter-pill">Nearby</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.text_input("Search users, reels, or music...", placeholder="Search...")
    
    # Explore Grid
    st.write("### Explore")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<img src='https://images.unsplash.com/photo-1511556820780-d912e42b4980?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)
        st.markdown("<br><img src='https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)
    with c2:
        st.markdown("<img src='https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)
        st.markdown("<br><img src='https://images.unsplash.com/photo-1506744626753-1fa6b6e9f6a5?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)
    with c3:
        st.markdown("<img src='https://images.unsplash.com/photo-1472214103451-9374bd1c798e?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)
        st.markdown("<br><img src='https://images.unsplash.com/photo-1518173946687-a4c8892bbd9f?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)


# --- PROFILE PAGE ---
elif st.session_state.current_page == "Profile":
    st.markdown("<h2 style='text-align: center; border-bottom: 1px solid #222; padding-bottom: 10px;'>bharat_1297</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="profile-header">
            <img src="https://i.pravatar.cc/150?img=11" class="profile-avatar">
            <h3 style="margin: 0;">Bharat Kumar</h3>
            <p style="color: #888 !important; font-size: 14px;">@bharat_1297</p>
            <div class="profile-stats">
                <div class="stat-item"><span class="stat-value">120</span><span class="stat-label">Posts</span></div>
                <div class="stat-item"><span class="stat-value">15.4K</span><span class="stat-label">Followers</span></div>
                <div class="stat-item"><span class="stat-value">340</span><span class="stat-label">Following</span></div>
            </div>
            <div class="profile-bio">Building Hyperverse App 🌌 | Tech Enthusiast</div>
        </div>
        <hr style='border-color: #222;'><h4>My Posts</h4>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown("<img src='https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)
    with col2: st.markdown("<img src='https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)
    with col3: st.markdown("<img src='https://images.unsplash.com/photo-1511556820780-d912e42b4980?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)


# ==========================================
# BOTTOM NAVIGATION (Interactive)
# ==========================================
st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🏠", key="nav_home", use_container_width=True):
        st.session_state.current_page = "Home"
        st.rerun()

with col2:
    if st.button("🔍", key="nav_search", use_container_width=True):
        st.session_state.current_page = "Discover"
        st.rerun()

with col3:
    if st.button("➕", key="nav_create", use_container_width=True):
        st.session_state.current_page = "Create"
        st.rerun()

with col4:
    if st.button("🎬", key="nav_reels", use_container_width=True):
        st.toast("Reels feature coming soon!")

with col5:
    if st.button("👤", key="nav_profile", use_container_width=True):
        st.session_state.current_page = "Profile"
        st.rerun()
import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Hyperverse", page_icon="🌌", layout="centered")

# 2. Session State Management
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"
if 'active_chat' not in st.session_state:
    st.session_state.active_chat = None
if 'messages' not in st.session_state:
    # Dummy chat history
    st.session_state.messages = {
        "alex_dev": [
            {"role": "user", "content": "Hey! Are we still on for the meeting?"},
            {"role": "assistant", "content": "Yes, absolutely. I'll send the link in a bit."},
            {"role": "user", "content": "Perfect. Thanks!"}
        ],
        "mike_tyson": [
            {"role": "user", "content": "Sent the project files."},
            {"role": "assistant", "content": "Got them. Reviewing now."}
        ]
    }

# 3. Custom CSS
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        .stApp { background-color: #0a0a0a; }
        
        .block-container {
            max-width: 400px !important;
            padding-top: 1rem !important;
            padding-bottom: 6rem !important;
            margin: auto;
            border: 1px solid #222;
            border-radius: 20px;
            background-color: #000000;
        }
        
        h1, h2, h3, p, span, div {
            color: #ffffff !important;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        /* Top Nav */
        .top-nav {
            display: flex; justify-content: space-between; align-items: center;
            padding: 10px 0px; border-bottom: 1px solid #222; margin-bottom: 15px;
        }
        .top-nav h2 { margin: 0; font-size: 22px; font-weight: 700; }

        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px; background-color: #1a1a1a; padding: 5px;
            border-radius: 20px; justify-content: center; margin-bottom: 15px;
        }
        .stTabs [data-baseweb="tab"] {
            height: 35px; border-radius: 15px; padding: 0px 20px;
            background-color: transparent; color: gray; font-weight: bold;
        }
        .stTabs [aria-selected="true"] {
            background-color: #e1306c !important; color: white !important;
        }

        /* Chat Styles */
        .chat-row { display: flex; align-items: center; padding: 10px 0; border-bottom: 1px solid #111; }
        .avatar { width: 50px; height: 50px; border-radius: 50%; background-color: #333; margin-right: 15px; object-fit: cover;}
        .chat-info { flex-grow: 1; }
        .chat-name { font-weight: 600; font-size: 15px; margin-bottom: 3px; }
        .chat-msg { color: #888 !important; font-size: 13px; }
        .blue-dot { width: 8px; height: 8px; background-color: #0095f6; border-radius: 50%; margin-left: 10px; }
        .wa-msg { display: flex; align-items: center; color: #888 !important; font-size: 13px; }
        .green-tick { color: #25D366; font-size: 14px; margin-right: 4px; }
        .filter-pill { background-color: #1a1a1a; color: #ccc !important; padding: 5px 12px; border-radius: 15px; font-size: 12px; margin-right: 8px; display: inline-block;}
        .filter-pill.active { background-color: #25D366; color: black !important; font-weight: bold; }

        /* Feed Styles */
        .feed-card { background-color: #111; border-radius: 15px; margin-bottom: 20px; overflow: hidden; border: 1px solid #222; }
        .feed-header { display: flex; align-items: center; padding: 10px 15px; }
        .feed-header-text { font-weight: 600; font-size: 14px; }
        .feed-header-text span { color: #888; font-size: 12px; font-weight: normal; }
        .feed-media { width: 100%; height: 350px; background-color: #222; object-fit: cover; }
        .feed-actions { padding: 10px 15px; font-size: 22px; display: flex; gap: 15px; }
        .feed-likes { padding: 0 15px; font-weight: 600; font-size: 14px; }
        .feed-caption { padding: 5px 15px 15px 15px; font-size: 14px; }

        /* Profile Styles */
        .profile-header { text-align: center; padding: 20px 0; }
        .profile-avatar { width: 90px; height: 90px; border-radius: 50%; border: 3px solid #e1306c; margin-bottom: 15px; }
        .profile-stats { display: flex; justify-content: center; gap: 30px; margin-bottom: 15px; }
        .stat-item { text-align: center; }
        .stat-value { font-size: 18px; font-weight: bold; display: block; }
        .stat-label { font-size: 12px; color: #888 !important; }
        .profile-bio { font-size: 14px; padding: 0 20px; margin-bottom: 20px; }
        .grid-img { width: 100%; aspect-ratio: 1/1; object-fit: cover; border-radius: 5px; }

        /* Create Page */
        .create-option { background-color: #1a1a1a; border: 1px solid #333; border-radius: 15px; padding: 20px; text-align: center; margin-bottom: 15px; cursor: pointer; }
        .create-icon { font-size: 30px; margin-bottom: 10px; display: block; }
        .create-title { font-weight: bold; font-size: 16px; }

        /* Chat Screen Specific */
        .chat-header { display: flex; align-items: center; padding-bottom: 15px; border-bottom: 1px solid #222; margin-bottom: 15px; }
        .chat-header img { width: 40px; height: 40px; border-radius: 50%; margin-right: 15px; }
        .chat-header-name { font-weight: bold; font-size: 16px; }
        
        /* Style Streamlit Buttons to look invisible for list items */
        .stButton > button {
            background-color: transparent !important;
            border: none !important;
            color: white !important;
            font-size: 20px !important;
            padding: 0 !important;
            box-shadow: none !important;
        }
        .stButton > button:hover { color: #e1306c !important; }

        /* List Item Button Override */
        div.stButton > button:first-child {
            text-align: left;
            background-color: #0a0a0a;
            border-bottom: 1px solid #222;
            border-radius: 0;
            padding: 10px 0px !important;
        }
        
        div.stButton > button:first-child:hover {
            background-color: #111;
        }

        /* Bottom Nav Container */
        div[data-testid="stHorizontalBlock"] {
            position: fixed; bottom: 0; left: 50%; transform: translateX(-50%);
            width: 100%; max-width: 400px; 
            background-color: #000000; border-top: 1px solid #222; padding: 10px 0px;
            z-index: 999;
        }
    </style>
""", unsafe_allow_html=True)


# ==========================================
# CONDITION 1: IF A CHAT IS OPENED
# ==========================================
if st.session_state.active_chat is not None:
    chat_user = st.session_state.active_chat
    
    # Header with Back Button
    col_back, col_title = st.columns([1, 4])
    with col_back:
        if st.button("⬅️", key="back_btn"):
            st.session_state.active_chat = None
            st.rerun()
    with col_title:
        st.markdown(f"<div class='chat-header-name'>{chat_user}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Display Chat Messages
    for msg in st.session_state.messages[chat_user]:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
    # Chat Input
    if prompt := st.chat_input("Type a message..."):
        # Add user message
        st.session_state.messages[chat_user].append({"role": "user", "content": prompt})
        # Add mock reply
        st.session_state.messages[chat_user].append({"role": "assistant", "content": "This is an automated reply from the prototype."})
        st.rerun()

# ==========================================
# CONDITION 2: NORMAL APP NAVIGATION
# ==========================================
else:
    # --- HEADERS ---
    if st.session_state.current_page == "Home":
        st.markdown("""
            <div class="top-nav">
                <h2>Hyperverse</h2>
                <div style="font-size: 20px; cursor: pointer;">✏️</div>
            </div>
        """, unsafe_allow_html=True)
    elif st.session_state.current_page == "Create":
        st.markdown("<h2 style='text-align: center; border-bottom: 1px solid #222; padding-bottom: 10px;'>New Post</h2>", unsafe_allow_html=True)
    elif st.session_state.current_page == "Discover":
        st.markdown("<h2 style='text-align: center; border-bottom: 1px solid #222; padding-bottom: 10px;'>Discover</h2>", unsafe_allow_html=True)
    elif st.session_state.current_page == "Profile":
        st.markdown("<h2 style='text-align: center; border-bottom: 1px solid #222; padding-bottom: 10px;'>bharat_1297</h2>", unsafe_allow_html=True)

    # --- PAGE CONTENT ---
    if st.session_state.current_page == "Home":
        tab1, tab2 = st.tabs(["💬 Chat", "▶️ Preview"])

        with tab1:
            st.markdown("<div style='font-size: 14px; color: gray; margin-bottom: 5px;'>Notes</div>", unsafe_allow_html=True)
            st.markdown("""
                <div style="display: flex; gap: 15px; margin-bottom: 20px;">
                    <div style="text-align: center;"><img src="https://i.pravatar.cc/150?img=11" class="avatar" style="border: 2px solid #555;"><div style="font-size: 11px; margin-top: 5px;">Your note</div></div>
                    <div style="text-align: center;"><img src="https://i.pravatar.cc/150?img=5" class="avatar" style="border: 2px solid #e1306c;"><div style="font-size: 11px; margin-top: 5px;">Dvi</div></div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<div style='display: flex; justify-content: space-between;'><h3>Messages</h3><span style='color: #0095f6; font-size: 14px;'>Requests</span></div>", unsafe_allow_html=True)
            
            # Interactive Chat Row (Instagram Style)
            if st.button("👤 alex_dev\nSent 4+ new messages · 12h", key="chat_alex"):
                st.session_state.active_chat = "alex_dev"
                st.rerun()

            st.markdown("<br><hr style='border-color: #333;'><br>", unsafe_allow_html=True)
            
            st.markdown("<h3>Hyper Chat</h3>", unsafe_allow_html=True)
            st.markdown("""
                <div style="margin-bottom: 15px;">
                    <span class="filter-pill active">All</span>
                    <span class="filter-pill">Unread 21</span>
                </div>
            """, unsafe_allow_html=True)
            
            # Interactive Chat Row (WhatsApp Style)
            if st.button("👤 mike_tyson\n✓✓ Sent the project files · 11:42 AM", key="chat_mike"):
                st.session_state.active_chat = "mike_tyson"
                st.rerun()

        with tab2:
            st.markdown("""
                <div class="feed-card">
                    <div class="feed-header">
                        <img src="https://i.pravatar.cc/150?img=33" class="avatar">
                        <div class="feed-header-text">aria.codes <span>· 34m</span></div>
                    </div>
                    <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=800&auto=format&fit=crop" class="feed-media">
                    <div class="feed-actions"><span>❤️</span> <span>💬</span> <span>✈️</span></div>
                    <div class="feed-likes">1,245 likes</div>
                    <div class="feed-caption"><b>aria.codes</b> Building the future of social media. 🚀</div>
                </div>
            """, unsafe_allow_html=True)

    elif st.session_state.current_page == "Create":
        st.write("Choose what you want to create:")
        col1, col2 = st.columns(2)
        with col1: st.markdown("<div class='create-option'><span class='create-icon'>🖼️</span><span class='create-title'>New Post</span></div>", unsafe_allow_html=True)
        with col2: st.markdown("<div class='create-option'><span class='create-icon'>🎬</span><span class='create-title'>Reel</span></div>", unsafe_allow_html=True)
        col3, col4 = st.columns(2)
        with col3: st.markdown("<div class='create-option'><span class='create-icon'>📸</span><span class='create-title'>Story</span></div>", unsafe_allow_html=True)
        with col4: st.markdown("<div class='create-option'><span class='create-icon'>🔴</span><span class='create-title'>Live</span></div>", unsafe_allow_html=True)
        st.write("---")
        st.write("### Upload Media")
        uploaded_file = st.file_uploader("Choose a photo or video from your album", type=['png', 'jpg', 'jpeg', 'mp4'])
        if uploaded_file is not None:
            if uploaded_file.type.startswith('image'): st.image(uploaded_file, caption='Preview', use_column_width=True)
            elif uploaded_file.type.startswith('video'): st.video(uploaded_file)
        st.text_area("Write a caption...", placeholder="What's on your mind?")
        if st.button("Share Post", type="primary", use_container_width=True):
            st.success("Post Shared Successfully! (Mockup)")

    elif st.session_state.current_page == "Discover":
        st.markdown("<div style='margin-bottom: 15px;'><span class='filter-pill active'>Explore</span><span class='filter-pill'>Following</span><span class='filter-pill'>Nearby</span></div>", unsafe_allow_html=True)
        st.text_input("Search users, reels, or music...", placeholder="Search...")
        st.write("### Explore")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("<img src='https://images.unsplash.com/photo-1511556820780-d912e42b4980?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)
            st.markdown("<br><img src='https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)
        with c2:
            st.markdown("<img src='https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)
            st.markdown("<br><img src='https://images.unsplash.com/photo-1506744626753-1fa6b6e9f6a5?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)
        with c3:
            st.markdown("<img src='https://images.unsplash.com/photo-1472214103451-9374bd1c798e?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)
            st.markdown("<br><img src='https://images.unsplash.com/photo-1518173946687-a4c8892bbd9f?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)

    elif st.session_state.current_page == "Profile":
        st.markdown("""
            <div class="profile-header">
                <img src="https://i.pravatar.cc/150?img=11" class="profile-avatar">
                <h3 style="margin: 0;">Bharat Kumar</h3>
                <p style="color: #888 !important; font-size: 14px;">@bharat_1297</p>
                <div class="profile-stats">
                    <div class="stat-item"><span class="stat-value">120</span><span class="stat-label">Posts</span></div>
                    <div class="stat-item"><span class="stat-value">15.4K</span><span class="stat-label">Followers</span></div>
                    <div class="stat-item"><span class="stat-value">340</span><span class="stat-label">Following</span></div>
                </div>
                <div class="profile-bio">Building Hyperverse App 🌌 | Tech Enthusiast</div>
            </div>
            <hr style='border-color: #222;'><h4>My Posts</h4>
        """, unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1: st.markdown("<img src='https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)
        with col2: st.markdown("<img src='https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)
        with col3: st.markdown("<img src='https://images.unsplash.com/photo-1511556820780-d912e42b4980?q=80&w=200&auto=format&fit=crop' class='grid-img'>", unsafe_allow_html=True)


    # ==========================================
    # BOTTOM NAVIGATION
    # ==========================================
    st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("🏠", key="nav_home"):
            st.session_state.current_page = "Home"
            st.rerun()
    with col2:
        if st.button("🔍", key="nav_search"):
            st.session_state.current_page = "Discover"
            st.rerun()
    with col3:
        if st.button("➕", key="nav_create"):
            st.session_state.current_page = "Create"
            st.rerun()
    with col4:
        if st.button("🎬", key="nav_reels"):
            st.toast("Reels feature coming soon!")
    with col5:
        if st.button("👤", key="nav_profile"):
            st.session_state.current_page = "Profile"
            st.rerun()