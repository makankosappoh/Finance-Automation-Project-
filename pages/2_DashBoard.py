import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import json
import os
import time

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Unauthorized access. Please login first.")
    time.sleep(1)
    st.switch_page("pages/1_Login.py")

st.set_page_config(
    page_title="Finance-Automation DashBoard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)
st.markdown(
    """
    <style>
        body {
            background-image: url('https://wallpapercave.com/wp/wp1960402.jpg'); 
            background-size: cover;
            background-position: center center;
            background-attachment: fixed;  
            opacity: 1; 
        .stApp {
            background-color: rgba(255, 255, 255, 0); 
        }
    </style>
    """,
    unsafe_allow_html=True
)

category_file = "categories.json"

if "categories" not in st.session_state: #to not lose information of categories 
    st.session_state.categories = {      #we create a thing called session/state in stremlit
        "Uncategorized": []             #once rerun , it will store info easy for analysis
    }
    
if os.path.exists(category_file):         #json file to put dummy categories that are uncategorized 
    with open(category_file , "r") as f:
        st.session_state.categories = json.load(f)
        
def save_categories():                    #every time enete rnew category it should be save for future refernce 
    with open(category_file, "w") as f:
        json.dump(st.session_state.categories, f)

def categorize_transactions(df):
    df["Category"] = "Uncategorized"
    
    for category , keywords in st.session_state.categories.items():
        if category == "Uncategorized" or not keywords:
            continue
        
        lowered_keywords = [keyword.lower().strip() for keyword in keywords]
        
        
        for index, row in df.iterrows():
            details = row["Details"].lower().strip()
            if details in lowered_keywords:
                df.at[index, "Category"] = category
            
    return df

def load_transactions(file):
    try:
        df = pd.read_csv(file)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df.columns = [colvalues.strip() for colvalues in df.columns]
        df["Amount"] = df["Amount"].str.replace(",", "").astype(float)
        df["Date"] = pd.to_datetime(df["Date"], format="%d %b %Y") 
        st.write(df)
        return categorize_transactions(df)
    
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None

def add_keyword_to_category(category, keyword):
    keyword = keyword.strip()
    if keyword and keyword not in st.session_state.categories[category]:
        st.session_state.categories[category].append(keyword)
        save_categories()
        return True
    return False

def main():
    st.title("Finance Dashboard: Bank Statement Analyze")
    uploaded_file = st.file_uploader("Upload your CSV format file", type=["csv"])
    if uploaded_file is not None:
        df = load_transactions(uploaded_file)
        df = categorize_transactions(df)
        
        if df is not None:
            
            Debits_df = df[df["Debit/Credit"] == "Debit"].copy()
            Credits_df = df[df["Debit/Credit"] == "Credit"].copy()
            
            st.session_state.Debits_df = Debits_df.copy()
            
            tabs1, tabs2 = st.tabs(["Expenses (DEBIT)" , "Payments (CREDIT)"])
            
            with tabs1:
                st.subheader("Expenses Summary")
                st.metric("Total Spent", f"{Debits_df['Amount'].sum():,.2f} Rs")
                new_category = st.text_input("New Category Name")
                add_button = st.button("Add Category")
                
                if add_button and new_category:
                    if new_category not in st.session_state.categories:
                        st.session_state.categories[new_category] = []
                        save_categories()
                        st.rerun()
                        if "category_added" in st.session_state:
                            st.success(f"{st.session_state.category_added} : Category added successfully ✅")
                            del st.session_state.category_added
                    else:
                        st.info(f"{new_category} already exists.")
                
                
            #edit some dataframes 
                st.subheader("Your expenses")
                edit_df = st.data_editor(
                st.session_state.Debits_df[["Date", "Details" , "Amount", "Category"]],
                column_config={
                    "Date": st.column_config.DateColumn("Date", format="DD/MM/YYYY"),
                        "Amount": st.column_config.NumberColumn("Amount", format="%.2f Rs"),
                        "Category": st.column_config.SelectboxColumn(
                            "Category",
                            options=list(st.session_state.categories.keys())
                        )
                },
                hide_index=True,
                use_container_width=True,
                key="category_editor"
            )
                save_button = st.button("Apply Changes", type="primary")
                if save_button:
                    for index, row in edit_df.iterrows():
                        new_category = row["Category"]
                        if new_category == st.session_state.Debits_df.at[index, "Category"]:
                            continue
                    
                        details = row["Details"]
                        st.session_state.Debits_df.at[index, "Category"] = new_category
                        add_keyword_to_category(new_category, details)
                        
                    st.success("Changes applied successfully!")
                    
                    csv = st.session_state.Debits_df.to_csv(index=False).encode('utf-8')
                    st.download_button("📥Download Updated CSV", csv, "updated_statement.csv", "text/csv")
                    
                st.markdown("---")
            
                st.markdown("Breakdown of Expenses")
                category_totals = st.session_state.Debits_df.groupby("Category")["Amount"].sum().reset_index()
                category_totals = category_totals.dropna()
                category_totals = category_totals.sort_values("Amount", ascending=False)
                st.dataframe(
                        category_totals, 
                        column_config={
                        "Amount": st.column_config.NumberColumn("Amount", format="%.2f Rs")   
                        },
                        use_container_width=True,
                        hide_index=True
                    )
                fig = px.pie(
                        category_totals,
                        values="Amount",
                        names="Category",
                        title="Expenses by Category"
                    )
                st.plotly_chart(fig, use_container_width=True)
                
                
                Debits_df['Month'] = Debits_df['Date'].dt.to_period('M').astype(str)
                trend = Debits_df.groupby('Month')['Amount'].sum().reset_index()
                fig = px.line(trend, x='Month', y='Amount', title="Monthly Expenses Trend")
                st.plotly_chart(fig, use_container_width=True)
                
        with tabs2:
            st.subheader("Payment Summary")
            st.metric("Total Received", f"{Credits_df['Amount'].sum():,.2f} Rs")
            st.write(Credits_df)
            
            csv = Credits_df.to_csv(index=False).encode('utf-8')
            st.download_button("📥Download Payment Report", csv, "payment_report.csv", "text/csv")
            
            Credits_df['Month'] = Credits_df['Date'].dt.to_period('M').astype(str)
            payment_by_month = Credits_df.groupby(['Month', 'Category'])['Amount'].sum().unstack().fillna(0)
            fig = px.imshow(
            payment_by_month.T,  
                color_continuous_scale='Blues',
                labels={'x': 'Month', 'y': 'Category', 'color': 'Amount'},
                title="Monthly Payments Heatmap"
            )
            st.plotly_chart(fig, use_container_width=True)
            
            
            
        
main()