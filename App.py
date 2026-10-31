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
