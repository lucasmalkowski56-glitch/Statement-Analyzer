# Credit Card Statement Analyser 

A personal finance tool that analyzes credit PDF statements and provides spending insights, visual breakdowns, and AI-powered budget predictions.

🔗 **[Live Demo](https://statement-analyzer-sgbrtd8kw4za2fw2ntyvfh.streamlit.app/)**

## Features
- 📂 **Multi-file upload** — upload multiple PDF statements at once with duplicate detection
- 📊 **Spending by Month** — interactive bar chart organized chronologically with monthly totals
- 🏷️ **Spending by Category** — breakdown across all uploaded statements
- 📋 **Monthly Summary** — for each month:
  - Rank by total spend
  - Total amount spent
  - Most expensive single purchase
  - Number of purchases
  - Top spending category
  - Average monthly spending across all months
- 🔮 **AI Predictions** — PyTorch model trained on your history predicts next month's total spending
- 💰 **Budget Recommendations** — splits the predicted total across categories based on your historical spending patterns

> **Tip:** The more statements you upload, the more accurate the predictions will be!

---

## Tech Stack 
| Tool | Purpose |
|------|---------|
| Python | Core language |
| Streamlit | Web UI and multi-page app |
| PyTorch | Neural network for spending predictions |
| pdfplumber | PDF text extraction |
| pandas | Data processing and CSV export |
| Plotly | Interactive charts |

---

## Run Localy
**1. Clone the repository**
```bash
git clone https://github.com/lucasmalkowski56-glitch/statement-analyzer.git
cd statement-analyzer
```

**2. Create a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the app**
```bash
streamlit run app.py
```

---

## Screenshots

### Home Page
![alt text](screenshot_home.png)

### Charts Page
![alt text](screenshot_charts.png)

### Summary Page 
![alt text](screenshot_summary.png)

### Prediction Page 
![alt text](screenshot_prediction.png)

## Notes 
 - Currently supports **CIBC Costco Mastercard** statements
 - Uploaded statements are processed in memory and never stored