{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f0dd3208-10c3-447f-81b7-d8f88d1b9e58",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-02-25 11:54:27.100 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.101 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.102 WARNING streamlit.runtime.state.session_state_proxy: Session state does not function when running a script without `streamlit run`\n",
      "2026-02-25 11:54:27.102 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.698 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\yogesh.km\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2026-02-25 11:54:27.698 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.699 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.701 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.701 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.701 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.705 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.705 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.707 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.707 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.709 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.711 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.711 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.713 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.713 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.717 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.719 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.720 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.721 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.722 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.724 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.724 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.726 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.726 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.728 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.728 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.731 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.731 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.733 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-25 11:54:27.734 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import datetime\n",
    "\n",
    "st.set_page_config(page_title=\"Wedding Invitation\", page_icon=\"💍\")\n",
    "\n",
    "# Get name from URL\n",
    "query_params = st.query_params\n",
    "guest_name = query_params.get(\"name\", \"Dear Guest\")\n",
    "\n",
    "st.title(\"💍 Wedding Invitation\")\n",
    "\n",
    "st.markdown(f\"## 💌 Dear {guest_name},\")\n",
    "\n",
    "st.write(\"You are cordially invited to the wedding of\")\n",
    "\n",
    "st.markdown(\"### Rama 💕 Seetha\")\n",
    "\n",
    "# Countdown\n",
    "wedding_date = datetime.datetime(2026, 5, 20)\n",
    "now = datetime.datetime.now()\n",
    "remaining = wedding_date - now\n",
    "\n",
    "st.subheader(\"⏳ Countdown\")\n",
    "st.write(f\"{remaining.days} days to go!\")\n",
    "\n",
    "st.subheader(\"📍 Venue\")\n",
    "st.write(\"Royal Palace Convention Hall, Bangalore\")\n",
    "\n",
    "st.balloons()\n",
    "\n",
    "st.success(\"We look forward to celebrating with you!\")"
   ]
  },
  {
   "cell_type": "code",
   "id": "9b5e5a44-d9a1-41f5-ad11-698b8486e3a7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
