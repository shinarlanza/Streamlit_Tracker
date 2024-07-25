import streamlit as st
import time

with st.container(border=True):
    with st.container():
        title, month = st.columns([3,1])
        with title:
            st.subheader("SAVINGS TRACKER")
        with month:
            st.subheader("August")

    st.divider()

    with st.container():
        st.subheader("Save Before You Spend")
        st.write("Shift the way you save! When you receive your income, save for yourself first by setting aside at least 20% before spending on expenses. Let's start saving for ourselves first today!")

    st.divider()

    with st.container():
        label, money, space = st.columns([1,2,4])
        with label:
            st.write("Income")
        with money:
            st.text_input(label="Income", label_visibility="collapsed", placeholder="PHP")

    with st.container(border=True):
        save_note, total =st.columns(2)
        with save_note:
            with st.container():
                with st.container():
                    st.subheader("Save For Yourself")
                
            with st.container():
                st.text_area(label="Note")
        with total:
            with st.container():
                title, money = st.columns([1,2])
                with title:
                    st.subheader("Total")
                with money:
                    st.text_input(label="money", label_visibility="collapsed", placeholder="PHP")
            with st.container():
                st.text_area(label="Amount Save")

    with st.container(border=True):
        save_note, total =st.columns(2)
        with save_note:
            with st.container():
                with st.container():
                    st.subheader("Manage your Expenses")
                
            with st.container():
                st.text_area(label="Note", key="expense_note")
        with total:
            with st.container():
                title, expense = st.columns([1,2])
                with title:
                    st.subheader("Total")
                with expense:
                    st.text_input(label="total expense", label_visibility="collapsed", placeholder="PHP")
            with st.container():
                st.text_area(label="Expense Amount")

    with st.container():
        income, total_savings, total_expenses, extra_savings = st.columns(4)
        with income:
            st.text_input(label="Income")
        with total_savings:
            st.text_input(label="Total Savings")
        with total_expenses:
            st.text_input(label="Total Expenses")
        with extra_savings:
            st.text_input(label="Extra Savings")

    with st.container():
        st.text_area(label="Note", key="extra_notes")

    if st.button('Save'):
        st.toast('Hip!')
        time.sleep(.5)
        st.toast('Hip!')
        time.sleep(.5)
        st.toast('Hooray!', icon='🎉')