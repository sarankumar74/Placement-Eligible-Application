import streamlit as st
import mysql.connector
import pandas as pd
# my first github code
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="placement"
    )

def function_filter(top_problems_solved, placement_status):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    query = f"""
        SELECT s.student_id, s.name, s.age, s.course_batch, p.problems_solved, 
               pl.placement_status, pl.company_name
        FROM Student_table AS s
        INNER JOIN Programming_table AS p ON s.student_id = p.student_id
        LEFT JOIN Placement_table AS pl ON s.student_id = pl.student_id
        WHERE p.problems_solved > {top_problems_solved}
    """
    if placement_status != "All":
        query += f" AND pl.placement_status = '{placement_status}'"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def run_query(query):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return pd.DataFrame(result)

st.set_page_config(page_title="GUVI Placement Dashboard", layout="wide")
st.title("Placement Eligible App")
st.subheader("Problems Solved and Placement Status")

top_problems_solved = st.selectbox("Problems Solved Greater Than", [250, 290, 320, 350, 390, 400])
placement_ready = st.selectbox("Placement Status", ["All", "Ready", "Placed", "Not Placed"])

if st.button("Get All"):
    data = function_filter(top_problems_solved, placement_ready)
    if data:
        st.dataframe(pd.DataFrame(data))

st.markdown("## Predefined Insights")

if st.button("1️⃣ High Problem Solvers & Placed"):
    df = run_query("""
        SELECT s.student_id, s.name, p.problems_solved, pl.placement_status, pl.company_name
        FROM Student_table AS s
        INNER JOIN Programming_table AS p ON s.student_id = p.student_id
        INNER JOIN Placement_table AS pl ON s.student_id = pl.student_id
        WHERE p.problems_solved > 360 AND pl.placement_status = 'Placed';
    """)
    st.dataframe(df)

if st.button("2️⃣ Soft Skills above 70%"):
    df = run_query("""
        SELECT s.student_id, s.name,
               (sf.communication + sf.teamwork + sf.presentation + sf.leadership +
                sf.critical_thinking + sf.interpersonal_skills)/6 AS avg_soft_skills
        FROM Student_table AS s
        INNER JOIN Soft_skill AS sf ON s.student_id = sf.student_id
        WHERE (sf.communication + sf.teamwork + sf.presentation + sf.leadership +
               sf.critical_thinking + sf.interpersonal_skills)/6 > 70;
    """)
    st.dataframe(df)

if st.button("3️⃣ Average Mock interview & Internship"):
    df = run_query("""
        SELECT s.student_id, s.name, pl.mock_interview_score, pl.internship_completed,
               (pl.mock_interview_score + pl.internship_completed)/2 AS average_score
        FROM Student_table AS s
        INNER JOIN Placement_table AS pl ON s.student_id = pl.student_id
        WHERE (pl.mock_interview_score + pl.internship_completed)/2 > 50;
    """)
    st.dataframe(df)

if st.button("4️⃣ Certificates & Mini Projects"):
    df = run_query("""
        SELECT s.student_id, s.name, p.mini_project, p.certificate_earned
        FROM Student_table AS s
        INNER JOIN Programming_table AS p ON s.student_id = p.student_id
        WHERE p.certificate_earned > 5 AND p.mini_project > 4;
    """)
    st.dataframe(df)

if st.button("5️⃣ Male Students"):
    df = run_query("""
        SELECT s.student_id, s.name, s.gender, p.problems_solved, p.language
        FROM Student_table AS s
        INNER JOIN Programming_table AS p ON s.student_id = p.student_id
        WHERE s.gender = 'male';
    """)
    st.dataframe(df)

if st.button("6️⃣ Female Students"):
    df = run_query("""
        SELECT s.student_id, s.name, s.gender, p.problems_solved, p.language
        FROM Student_table AS s
        INNER JOIN Programming_table AS p ON s.student_id = p.student_id
        WHERE s.gender = 'female';
    """)
    st.dataframe(df)

if st.button("7️⃣ Graduating in 2025 - 2027"):
    df = run_query("""
        SELECT student_id, name, age, enrollment_year, graduation_year
        FROM Student_table
        WHERE enrollment_year = 2025 AND graduation_year = 2027;
    """)
    st.dataframe(df)

if st.button("8️⃣ Age Between 30 and 40"):
    df = run_query("""
        SELECT student_id, name, age, gender, enrollment_year, course_batch, graduation_year
        FROM Student_table
        WHERE age BETWEEN 30 AND 40;
    """)
    st.dataframe(df)

if st.button("9️⃣ Interpersonal & Critical Skills Above 50 to 70"):
    df = run_query("""
        SELECT s.name, s.student_id, sf.interpersonal_skills, sf.critical_thinking
        FROM Student_table AS s
        INNER JOIN Soft_skill AS sf ON s.student_id = sf.student_id
        WHERE sf.interpersonal_skills BETWEEN 50 AND 70 
          AND sf.critical_thinking BETWEEN 50 AND 70;
    """)
    st.dataframe(df)

if st.button("🔟 Placement Placed Student List"):
    df = run_query("""
        SELECT s.name, s.student_id, p.placement_status, p.company_name
        FROM Student_table AS s
        INNER JOIN Placement_table AS p ON s.student_id = p.student_id
        WHERE p.placement_status = 'Placed';
    """)
    st.dataframe(df)

