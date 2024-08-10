import io

import duckdb
import pandas as pd

import streamlit as st

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

# -------------------------------------------------------------------------------
# Exercices List
# -------------------------------------------------------------------------------

data = {
    "theme": ["cross_joins", "cross_joins"],
    "exercise_name": ["gold_and_silver", "prime_ministers_and_presidents"],
    "tables": [["gold", "silver"], ["prime_ministers", "presidents"]],
    "last_reviewed": ["1980-01-01", "1970-01-01"],
}
memory_state_df = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")
# -----------------------------------------------------------
# CROSS JOIN EXERCICES
# -----------------------------------------------------------
CSV = """
gold,number
Etats-unis,33
Chine,33
France,14
"""
gold = pd.read_csv(io.StringIO(CSV))
con.execute("CREATE TABLE IF NOT EXISTS gold AS SELECT * FROM gold")

CSV2 = """
silver,number
Etats-unis,39
Chine,27
France,20
"""
silver = pd.read_csv(io.StringIO(CSV2))
con.execute("CREATE TABLE IF NOT EXISTS silver AS SELECT * FROM silver")

prime_ministers = '''
prime_minister
Kamala Harris
Li Qiang
Gabriel Attal
'''
prime_ministers = pd.read_csv(io.StringIO(prime_ministers))
con.execute("CREATE TABLE IF NOT EXISTS prime_ministers AS SELECT * FROM prime_ministers")

presidents = '''
President
Joe Biden
Xi Jiping
Emmanuel macron
'''
presidents = pd.read_csv(io.StringIO(presidents))
con.execute("CREATE TABLE IF NOT EXISTS presidents AS SELECT * FROM presidents")