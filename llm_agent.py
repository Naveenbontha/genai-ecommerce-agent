import google.generativeai as genai
import re

# 🔑 Replace with your actual Gemini API key
GEMINI_API_KEY = "AIzaSyBJftSBdA17bSKiNdEgYt_QXM6n5Y_Y6_Y"
genai.configure(api_key=GEMINI_API_KEY)

# ✅ Use the right Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")

def get_sql_from_question(question: str) -> str:
    prompt = f"""
You are a helpful assistant that converts user questions into valid **SQLite SQL queries**.

🎯 Tables and Columns:

📊 ad_sales_metrics:
- date
- item_id
- ad_sales
- impressions
- ad_spend
- clicks
- units_sold

📦 total_sales_metrics:
- eligibility_datetime_utc
- item_id
- eligibility
- message

✅ eligibility_table:
- date
- item_id
- total_sales
- total_units_ordered

🧠 Special Instructions:
- To calculate **RoAS (Return on Ad Spend)**:
    SELECT SUM(eligibility_table.total_sales) / SUM(ad_sales_metrics.ad_spend)
    FROM ad_sales_metrics
    JOIN eligibility_table ON ad_sales_metrics.item_id = eligibility_table.item_id
- Use only the columns listed above.
- Do NOT divide ad_spend by itself.
- Return only raw SQL. No markdown. No explanation. No comments.

Question: {question}
SQL:
"""

    response = model.generate_content(prompt)
    sql = response.text.strip()

    # ✅ Remove markdown wrappers if present
    sql = re.sub(r"^```sql\s*|```$", "", sql, flags=re.IGNORECASE).strip()

    return sql
