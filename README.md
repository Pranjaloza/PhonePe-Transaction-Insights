# 📲 PhonePe Transaction Insights Dashboard

An end-to-end data analysis and visualization project based on PhonePe Pulse data. This project explores regional transaction dynamics, user behavior, device dominance, and provides strategic recommendations using interactive dashboards and machine learning.

---

## 🔍 Project Highlights

- 📊 Dashboard with dynamic filters (state, year, quarter, device, etc.)
- 📍 Choropleth map for geo-level insights
- 📈 ML regression model to predict transaction amounts
- ✅ Business scenario analysis with recommendations

---

## 📁 Folder Structure

├── notebooks/ # Jupyter notebook with EDA, modeling
├── src/ # Streamlit dashboard and model files
├── reports/ # Visual assets and summary documents
├── sql/ # MySQL schema

---

## 📦 Installation & Setup

1. **Clone the repo:**
```bash
git clone https://github.com/your-username/phonepe-transaction-insights.git
cd phonepe-transaction-insights
```

2.  **Clone the repo:**
   ```pip install -r requirements.txt ```
3. **Set up MySQL database:**
- Run create_table.sql in your MySQL to create necessary tables.
- Load JSON data into MySQL from the data/pulse/ directory using Python or CLI.

4. **Run streamlit app:**
   ```cd src
   streamlit run phonepe_dashboard.py```
---

## 📊 Technologies Used
1. Python, Pandas, MySQL
2. Streamlit (for dashboard)
3. Plotly (for visuals)
4. GeoJSON (for maps)
5. Scikit-learn (for ML regression model)

---

## 📈 Business Scenarios Covered
- Transaction Dynamics

- Device Engagement Trends

- State-Wise User Registrations

- District-Level Growth

- Strategic Expansion Recommendations

  

