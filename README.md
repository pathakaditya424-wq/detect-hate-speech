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
<img width="1920" height="896" alt="Screenshot (56)" src="https://github.com/user-attachments/assets/39b76956-7a27-4c49-a1bd-15b3aac39a02" />
<img width="1920" height="893" alt="Screenshot (55)" src="https://github.com/user-attachments/assets/8a02d6ee-19ab-4580-bf3a-ed89d3b1501c" />
