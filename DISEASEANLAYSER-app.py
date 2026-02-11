import streamlit as st

# Data Dictionary: Symptoms, Disease, and Home Treatment
disease_data = {
    "Influenza (Flu)": {
        "symptoms": ["Fever", "Chills", "Sore throat", "Cough", "Body aches", "Fatigue"],
        "treatment": "Rest, stay hydrated, and take over-the-counter pain relievers (paracetamol). Keep warm."
    },
    "COVID-19": {
        "symptoms": ["Fever", "Cough", "Shortness of breath", "Fatigue", "Loss of taste/smell"],
        "treatment": "Isolate, monitor oxygen levels, stay hydrated, and rest. Use a pulse oximeter."
    },
    "Common Cold": {
        "symptoms": ["Runny nose", "Stuffy nose", "Sneezing", "Sore throat", "Mild cough"],
        "treatment": "Drink warm fluids, gargle with salt water, and use nasal decongestants."
    },
    "Typhoid Fever": {
        "symptoms": ["High fever", "Weakness", "Stomach pain", "Headache", "Diarrhea"],
        "treatment": "Drink plenty of boiled water/ORS and consume light, easily digestible food."
    },
    "Cholera": {
        "symptoms": ["Severe diarrhea", "Vomiting", "Dehydration"],
        "treatment": "Immediate Oral Rehydration Solution (ORS) and drink clean, safe water."
    },
    "Conjunctivitis (Eye Flu)": {
        "symptoms": ["Red eyes", "Itchy eyes", "Watery eyes", "Sensitivity to light"],
        "treatment": "Apply cool compresses, avoid rubbing eyes, and use clean washcloths."
    },
    "Dengue": {
        "symptoms": ["High fever", "Severe headache", "Joint pain", "Muscle pain", "Rash"],
        "treatment": "Drink plenty of fluids (coconut water/juice) and rest. Avoid aspirin/ibuprofen."
    },
    "Diabetes": {
        "symptoms": ["Increased thirst", "Frequent urination", "Fatigue", "Blurred vision"],
        "treatment": "Monitor blood sugar levels and stay hydrated. Avoid sugary foods immediately."
    },
    "Hypertension": {
        "symptoms": ["Headaches", "Dizziness", "Often asymptomatic"],
        "treatment": "Reduce salt intake, practice deep breathing, and rest in a quiet place."
    },
    "Asthma": {
        "symptoms": ["Wheezing", "Shortness of breath", "Chest tightness", "Coughing"],
        "treatment": "Sit upright, stay calm, and use your rescue inhaler if available."
    },
    "Anaemia": {
        "symptoms": ["Fatigue", "Weakness", "Pale skin", "Shortness of breath"],
        "treatment": "Eat iron-rich foods (spinach, beans, red meat) and Vitamin C to aid absorption."
    },
    "Fatty Liver": {
        "symptoms": ["Abdominal pain", "Fatigue", "Yellowing of skin (jaundice)"],
        "treatment": "Avoid alcohol and fatty foods; focus on a plant-based diet."
    },
    "Thyroid Disorders": {
        "symptoms": ["Weight changes", "Fatigue", "Mood swings"],
        "treatment": "Maintain a regular sleep schedule and reduce stress through meditation."
    },
    "Depression": {
        "symptoms": ["Persistent sadness", "Loss of interest", "Insomnia", "Fatigue"],
        "treatment": "Reach out to a trusted friend or family member; practice light physical activity."
    }
}

# --- Streamlit UI ---
st.set_page_config(page_title="AI Disease Analyzer", layout="centered")

st.title("🩺 Disease Symptom Analyzer")
st.write("Select the symptoms you are experiencing to find potential matches.")

# Create a unique list of all symptoms for the dropdown
all_symptoms = sorted(list(set(s for d in disease_data.values() for s in d["symptoms"])))

# User input: Multi-select symptoms
user_symptoms = st.multiselect("Select your symptoms:", all_symptoms)

if st.button("Analyze Symptoms"):
    if user_symptoms:
        found = False
        st.subheader("Results:")
        
        for disease, info in disease_data.items():
            # Check if any user symptoms match the disease symptoms
            matches = set(user_symptoms).intersection(set(info["symptoms"]))
            
            if len(matches) >= 2: # Match if at least 2 symptoms overlap
                found = True
                with st.expander(f"Potential Match: {disease}"):
                    st.write(f"**Common Symptoms:** {', '.join(info['symptoms'])}")
                    st.success(f"**First Aid/Home Treatment:** {info['treatment']}")
        
        if not found:
            st.warning("No specific match found. If symptoms persist, please see a doctor.")
    else:
        st.info("Please select at least one symptom.")

st.divider()
st.caption("⚠️ **Disclaimer:** This tool is for educational purposes only and is not a substitute for professional medical advice.")
