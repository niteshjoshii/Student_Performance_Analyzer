import streamlit as st
import pandas as pd
import plotly.express as px
import os

# PAGE TITLE

st.title("Student Performance Analyzer")

# CSV FILE

file = "student_data.csv"

# LOAD DATA

if os.path.exists(file):

    df = pd.read_csv(file)

else:

    df = pd.DataFrame(columns=[
        "Name",
        "Math",
        "Science",
        "English",
        "Computer",
        "Total",
        "Percentage",
        "Result"
    ])

# FORM INPUT

st.subheader("Enter Student Details")

name = st.text_input("Student Name")

math = st.number_input("Math Marks", 0, 100)

science = st.number_input("Science Marks", 0, 100)

english = st.number_input("English Marks", 0, 100)

computer = st.number_input("Computer Marks", 0, 100)

# SUBMIT BUTTON

if st.button("Add Student"):

    total = math + science + english + computer

    percentage = total / 4

    result = "Pass" if percentage >= 40 else "Fail"

    new_data = {
        "Name": name,
        "Math": math,
        "Science": science,
        "English": english,
        "Computer": computer,
        "Total": total,
        "Percentage": percentage,
        "Result": result
    }

    df = pd.concat(
        [df, pd.DataFrame([new_data])],
        ignore_index=True
    )

    df.to_csv(file, index=False)

    st.success("Student Added Successfully!")

# SHOW DATA

st.subheader(" Student Records")

st.dataframe(df)

# SUBJECT AVERAGE

if not df.empty:

    st.subheader(" Subject-wise Average")

    subject_avg = df[
        ["Math","Science","English","Computer"]
    ].mean()

    st.write(subject_avg)

    # BAR CHART

    fig = px.bar(
        x=subject_avg.index,
        y=subject_avg.values,
        labels={
            "x":"Subjects",
            "y":"Average Marks"
        },
        title="Average Marks by Subject"
    )

    st.plotly_chart(fig)

    # TOPPER

    st.subheader("Top Performer")

    topper = df.loc[df["Total"].idxmax()]

    st.success(
        f'{topper["Name"]} scored {topper["Total"]}'
    )

    # RESULT COUNT

    st.subheader("Pass/Fail Analysis")

    result_chart = px.pie(
        df,
        names="Result",
        title="Pass vs Fail"
    )

    st.plotly_chart(result_chart)