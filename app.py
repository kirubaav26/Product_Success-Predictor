import streamlit as st
import pickle
import numpy as np
import random

# Load model
try:
    model = pickle.load(open("model.pkl", "rb"))
except FileNotFoundError:
    model = None

# Page config
st.set_page_config(page_title="Product Success Predictor", layout="centered")

# 💜 LIGHT VIOLET CLEAN UI
st.markdown("""
    <style>
    .stApp {
        background-color: #EEE6FF; 
    }
    h1, h2, h3, h4, h5, h6, p, label {
        color: black !important;
    }
    h1 {
        text-align: center;
        font-size: 38px;
        font-weight: bold;
    }
    .stNumberInput input {
        background-color: white;
        border-radius: 8px;
        color: black;
    }
    .stButton>button {
        background-color: #C5B3FF;
        color: black;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
        font-weight: 600;
        border: none;
    }
    .stButton>button:hover {
        background-color: #B19CFF;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Product Success Predictor")
st.markdown("---")

# Inputs
st.subheader("Enter Product Details")
price = st.number_input("💰 Price (₹)", min_value=0, step=1)
rating = st.slider("⭐ Rating", 1.0, 5.0, step=0.5)
discount = st.slider("🏷️ Discount (%)", 0, 100, step=5)

st.markdown("---")

# --- SUGGESTION POOLS (10 EACH) ---
excellent_tips = [
    "Scale your ads—this product is ready for a larger audience.",
    "Introduce a 'Premium Edition' to capture higher margins.",
    "Focus on inventory management to avoid 'Out of Stock' issues.",
    "Create high-quality video demos to boost conversions further.",
    "Encourage satisfied customers to leave detailed photo reviews.",
    "Partner with influencers in your niche for brand authority.",
    "Consider expanding to international shipping.",
    "Create a loyalty program for repeat buyers of this item.",
    "Use this product as a 'Hero' item in your homepage banners.",
    "Bundle this with slower-moving items to clear stock."
]

moderate_tips = [
    "A/B test your product images to see which gets more clicks.",
    "Respond to all 3-star reviews to show you care about quality.",
    "Offer 'Free Shipping' for a limited time to nudge buyers.",
    "Increase the discount by 5% and monitor the sales lift.",
    "Optimize your product description with better SEO keywords.",
    "Add a 'Limited Stock' tag to create a sense of urgency.",
    "Send a re-engagement email to users who added this to cart.",
    "Compare your price point with 3 top competitors.",
    "Add an FAQ section to address common customer hesitations.",
    "Ensure your lighting in product photos is bright and professional."
]

low_tips = [
    "Review the product quality; the current rating is a bottleneck.",
    "Consider a drastic price drop to find the market's 'sweet spot'.",
    "Pivot the marketing angle—try targeting a different demographic.",
    "Offer a 'Buy 1 Get 1' deal to gain initial traction.",
    "Pause ad spend until the product page conversion improves.",
    "Conduct a survey to find out why customers are leaving.",
    "Refresh the branding and packaging for a modern look.",
    "Check if the shipping costs are scaring customers away.",
    "Seek a co-branding opportunity to build trust.",
    "Launch a 'Beta' version at a lower cost to gather feedback."
]

# Prediction
if st.button("Predict"):
    if price == 0:
        st.warning("Please enter a valid price")
    elif model is None:
        st.error("Model file 'model.pkl' not found!")
    else:
        input_data = np.array([[price, rating, discount]])
        prediction = model.predict(input_data)
        result = round(float(prediction[0]), 2)

        st.write(f"### Predicted Success: {result}%")
        # Ensure progress bar stays between 0-100
        progress_val = max(0, min(100, int(result)))
        st.progress(progress_val)

        st.markdown("### 💡 Expert Suggestions")
        
        if result > 70:
            st.success("**Status: Excellent Potential**")
            pool = excellent_tips
        elif result > 40:
            st.warning("**Status: Moderate Performance**")
            pool = moderate_tips
        else:
            st.error("**Status: Low Market Fit**")
            pool = low_tips

        # Show 3 random suggestions from the correct pool
        selected_suggestions = random.sample(pool, 3)
        for tip in selected_suggestions:
            st.info(tip)
