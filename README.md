Call Analysis App

This Streamlit application analyzes collection call conversations (in YAML format) to:
1. Detect profanity
2. Check for privacy & compliance violations
3. Calculate silence and overtalk metrics
4. Generate visualizations for silence and overtalk
   
Setup Instructions
 1. Clone the Respository
    git clone https://github.com/anishimishra/call-analysis-app
    cd debt_call_analysis
    
 2. Create a virtual environment
    python3 -m venv venv
    source venv/bin/activate --Linux/Mac
    venv\Scripts\activate
    
 3. Install dependencies
    pip install -r requirements.txt
    or
    pip install streamlit pyyaml matplotlib scikit-learn pandas
    
 4. Create output folder
    mkdir output

Execution Instructions
1. Run the Streamlit App
   streamlit run app.py

Steps Inside the App
1. Upload your YAML conversation file
   
2. Select your analysis approach :
   1. Pattern Matching
   2. LLM/LM Model
      
3. Choose the Analysis Type :
   1. Profanity Detection
   2. Privacy & Compliance check
      
4. View Results :
   1. Profanity words flagged
   2. Compliance issues detected
   3. Overtalk and silence metrics with visual charts
