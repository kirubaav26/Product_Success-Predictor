import streamlit as st
import pickle

# Page config
st.set_page_config(page_title="Product Predictor", page_icon="🚀", layout="centered")

# Custom styling (Minimal Tech Theme)
st.markdown("""
    <style>
    body {
        background-color: #ffffff;
    }
    h1 {
        color: #111827;
        text-align: center;
        font-weight: 700;
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-size: 16px;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #1e40af;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.markdown("<h1>Product Success Predictor 🚀</h1>", unsafe_allow_html=True)

# Subtitle
st.markdown("### Predict product success based on key business factors 📊")

st.markdown("---")

# Section heading
st.subheader("Enter Product Details")

# Inputs
price = st.number_input("Enter Price (₹)", min_value=0, step=1)

rating = st.slider("Rating", 1.0, 5.0, step=0.5)

discount = st.slider("Discount (%)", 0, 100, step=5)

st.markdown("---")

# Prediction
if st.button("Predict"):

    # Validation
    if price == 0:
        st.warning("Please enter a valid price ⚠️")

    else:
        input_data = [[price, rating, discount]]

        prediction = model.predict(input_data)

        result = round(prediction[0], 2)

        st.write(f"### Predicted Success: {result}%")

        # Progress bar
        st.progress(int(result))

        # Insights
        if result > 70:
            st.success("🔥 Excellent product! High chance of success")
        elif result > 40:
            st.warning("⚠️ Moderate success — consider improving pricing or discount")
        else:
            st.error("❌ Low success — rethink strategy (price/discount/rating)")
