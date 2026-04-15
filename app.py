import streamlit as st
import pickle
import numpy as np
import random
import matplotlib.pyplot as plt

# Load model
try:
    model = pickle.load(open("model.pkl", "rb"))
except FileNotFoundError:
    model = None

# Page config
st.set_page_config(page_title="Product Success Pro", layout="centered")

# 🎨 UI CUSTOMIZATION
st.markdown("""
    <style>
    .stApp { background-color: #F3E8FF; }
    h1, h2, h3, p, label { color: #1F2937 !important; }
    
    /* Center the Title */
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        padding-bottom: 0.5rem;
    }

    .stButton>button {
        background-color: #A78BFA;
        color: white;
        border-radius: 12px;
        height: 3.5em;
        font-weight: bold;
        width: 100%;
        border: none;
    }
    .stButton>button:hover { background-color: #7C3AED; color: white; }
    
    /* Hide the numeric spinners */
    input[type=number]::-webkit-inner-spin-button, 
    input[type=number]::-webkit-outer-spin-button {
        -webkit-appearance: none; margin: 0;
    }
    </style>
""", unsafe_allow_html=True)

# Centered Title
st.markdown('<h1 class="main-title">Product Success Predictor</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Advanced Market Analytics & Strategic Growth Forecasting</p>", unsafe_allow_html=True)
st.markdown("---")

# 🧱 STRUCTURED INPUTS
st.subheader("📦 Product Parameters")
col1, col2 = st.columns(2)

with col1:
    price_raw = st.text_input("💰 Unit Price (₹)", value="500")
    rating = st.slider("⭐ Consumer Rating", 1.0, 5.0, step=0.1, value=4.0)

with col2:
    discount = st.slider("🏷️ Promotional Discount (%)", 0, 100, step=1, value=10)
    category = st.selectbox("📂 Market Segment", ["Electronics", "Fashion", "Beauty", "Home Decor", "Fitness"])

# --- PROFESSIONAL DATA POOLS ---

excellent_suggestions = [
    "Scale performance marketing across high-intent social channels immediately.",
    "Implement a 'Premium Tier' version to capitalize on high brand equity.",
    "Initiate international logistics expansion to capture global market share.",
    "Develop a high-tier influencer partnership program for long-term brand advocacy.",
    "Launch a tiered loyalty program to increase Customer Lifetime Value (CLV).",
    "Optimise supply chain efficiency to maintain margins during high-volume scaling.",
    "Execute a 'Flash Sale' strategy for complementary products to cross-sell.",
    "Invest in 4K video marketing assets to further enhance product perceived value.",
    "Secure retail distribution partnerships with premium physical department stores.",
    "Apply for industry-specific design or innovation awards to solidify market authority."
]

moderate_suggestions = [
    "Conduct rigorous A/B testing on primary product imagery to improve Click-Through Rates.",
    "Optimize SEO metadata and long-tail keywords to capture organic search traffic.",
    "Deploy 'Scarcity Marketing' tactics such as limited-stock countdown timers.",
    "Introduce a free shipping threshold to increase Average Order Value (AOV).",
    "Revise product descriptions to focus on 'Benefits' rather than just technical 'Features'.",
    "Request video testimonials from existing customers to build stronger social proof.",
    "Bundle this product with a high-margin accessory to increase total transaction value.",
    "Retarget abandoned cart users with a personalized 5% incentive discount.",
    "Evaluate competitor pricing models to ensure price-point competitiveness.",
    "Improve the unboxing experience to drive organic social media 'unboxing' shares."
]

low_suggestions = [
    "Perform a comprehensive pivot of the core marketing angle and target persona.",
    "Execute an aggressive 'Buy One Get One' (BOGO) campaign to clear existing inventory.",
    "Conduct deep-dive customer surveys to identify fundamental product-market friction.",
    "Complete a brand identity refresh including logo and packaging aesthetics.",
    "Temporarily reduce pricing to the 'Low-Entry' bracket to stimulate initial velocity.",
    "Shift focus to micro-niche markets where competition is significantly lower.",
    "Audit technical specifications against the top 3 market competitors for gaps.",
    "Invest in higher quality customer support to mitigate the impact of low ratings.",
    "Incentivize honest reviews by offering future store credits to verified buyers.",
    "Consider white-labeling or rebranding the product for a different demographic."
]

excellent_insights = [
    "Market data suggests your product is currently in the 'High-Growth' quadrant.",
    "Current price-to-rating ratio indicates strong consumer psychological value.",
    "The product displays high viral potential within the chosen market segment.",
    "Low price sensitivity detected; you may have room for a 5-10% price increase.",
    "Your metrics align with the top 5% of successful launches in this category."
]

moderate_insights = [
    "The product is hovering at 'Market Average'; minor UX tweaks could trigger a breakout.",
    "Conversion friction is likely occurring at the consideration stage, not the interest stage.",
    "Your rating is stable, but your discount strategy is slightly below the market competitive edge.",
    "Growth is currently linear; non-linear growth requires a shift in visual storytelling.",
    "Increasing your rating by just 0.4 points could double your predicted success rate."
]

low_insights = [
    "Current market fit is misaligned; the price point exceeds the perceived utility.",
    "High bounce rates are predicted based on the current rating-to-price correlation.",
    "Consumer trust appears to be the primary bottleneck for this specific SKU.",
    "The 'Value Proposition' is not currently clear enough to compete with market leaders.",
    "Significant 'Friction Points' detected in the current promotional structure."
]

st.markdown("---")

if st.button("Predict"):
    try:
        price = float(price_raw)
    except ValueError:
        st.error("Please enter a valid numeric price.")
        st.stop()

    if price <= 0:
        st.warning("Price must be greater than zero.")
    elif model is None:
        st.error("Model file 'model.pkl' not found!")
    else:
        # Prediction logic
        input_data = np.array([[price, rating, discount]])
        prediction = model.predict(input_data)
        result = round(float(prediction[0]), 2)

        # 📊 RESULTS DASHBOARD
        st.subheader("📊 Strategic Analysis Results")
        m_col1, m_col2 = st.columns([1, 1.5])
        
        with m_col1:
            st.metric(label="Predicted Success Probability", value=f"{result}%")
            if result > 70:
                st.success("Status: High Potential")
                s_pool, i_pool = excellent_suggestions, excellent_insights
            elif result > 40:
                st.warning("Status: Moderate Fit")
                s_pool, i_pool = moderate_suggestions, moderate_insights
            else:
                st.error("Status: Low Traction")
                s_pool, i_pool = low_suggestions, low_insights

        with m_col2:
            st.write("**💡 AI Strategic Insights:**")
            selected_insights = random.sample(i_pool, 3)
            for insight in selected_insights:
                st.write(f"• {insight}")

        # 📉 VISUAL CHART (BOX STYLE)
        # Success Rate vs Market Gap comparison
        fig, ax = plt.subplots(figsize=(6, 2.5))
        fig.patch.set_facecolor('#F3E8FF')
        ax.set_facecolor('#F3E8FF')
        
        labels = ['Success Score', 'Market Gap']
        values = [result, 100 - result]
        # Success is Purple, Gap is Slate Gray (No green used)
        colors = ['#7C3AED', '#64748B'] 
        
        ax.barh(labels, values, color=colors)
        ax.set_xlim(0, 100)
        
        # Adding labels on the bars for clarity
        for i, v in enumerate(values):
            ax.text(v + 1, i, f"{v}%", color='#1F2937', fontweight='bold', va='center')

        st.pyplot(fig)

        st.markdown("Strategic Roadmap")
        selected_suggestions = random.sample(s_pool, 3)
        for tip in selected_suggestions:
            st.info(f"**Action Item:** {tip}")
