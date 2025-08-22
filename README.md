# Hate Speech Detection (Streamlit App)

This project is a **Streamlit-based web app** for detecting hate speech in text.  
The model classifies text into two categories:
- **1 = Toxic**  
- **2 = Neutral**

## 🚀 Features
- Simple and interactive Streamlit UI  
- Real-time text classification  
- Easy to run locally or deploy on Streamlit Cloud  

## ⚠️ Note on Accuracy
The dataset used contains some similarities between positive expressions (like *"love"*) and negative expressions (hate-related).  
Because of this, the model may **occasionally give incorrect results**.  
For example:
- "I love this" → might sometimes be predicted as hate speech.  
- Similar words across different contexts can confuse the model.  

This limitation exists due to dataset overlap and can be improved in the future with more refined data.  

## 🛠️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/detect-hate-speech.git
   cd detect-hate-speech
pip install -r requirements.txt
streamlit run app.py
<img width="1920" height="1080" alt="Screenshot (56)" src="https://github.com/user-attachments/assets/feb40800-dd4e-4b25-af89-b816d9b92e4c" />
<img width="1920" height="1080" alt="Screenshot (55)" src="https://github.com/user-attachments/assets/259d7e6c-720a-45a5-98d9-93754ac4063c" />
<img width="1920" height="1008" alt="Screenshot 2025-08-22 174832" src="https://github.com/user-attachments/assets/bb347cef-37e0-4f67-aac4-7e55178552e6" />
