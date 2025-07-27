import streamlit as st
import requests
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="StratAGI Business Analyst",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Backend Configuration ---
# Assumes the FastAPI backend is running on the default host and port.
# When deploying with Docker, this might change to the service name (e.g., "http://backend:8000/analyze").
BACKEND_URL = "http://127.0.0.1:8000/analyze"

# --- Sidebar Content ---
with st.sidebar:
    st.title("🤖 StratAGI")
    st.markdown(
        "**StratAGI** is an autonomous AI agent crew designed to perform "
        "comprehensive business and market analysis on demand."
    )
    st.markdown(
        "Simply enter a company and a target market, and the AI agents will "
        "collaborate to research, analyze, and generate a professional-grade "
        "strategic report."
    )
    st.header("Tech Stack")
    st.markdown(
        """
        - **Agentic Framework:** `CrewAI`
        - **LLM:** `Groq (Llama4/DeepSeek), Google Gemini`
        - **Backend:** `FastAPI`
        - **Frontend:** `Streamlit`
        - **Tools:** `Tavily (Search)`, `Alpha Vantage (Financials)`
        """
    )
    st.info("Project created by Shailesh Singh  [GitHub](https://github.com/shailesh-singh-ss/StratAGI) | [LinkedIn](https://www.linkedin.com/in/shailesh-singh-544bb3229)")


# --- Main Application UI ---
st.title("Autonomous Business Strategy Analyst")
st.markdown("Enter a company and its target market to generate a full strategic analysis, including the agents' step-by-step work.")

# Input form for the user
with st.form("analysis_form"):
    col1, col2 = st.columns(2)
    with col1:
        company = st.text_input(
            "Company Name", 
            placeholder="e.g., NVIDIA",
            help="The name of the company you want to analyze."
        )
    with col2:
        market = st.text_input(
            "Target Market", 
            placeholder="e.g., AI Hardware",
            help="The specific market or industry to focus the analysis on."
        )
    
    submit_button = st.form_submit_button(label="Generate Strategic Report")


# --- Logic to handle form submission ---
if submit_button:
    if not company or not market:
        st.error("Please provide both a company name and a target market.")
    else:
        with st.spinner(f"🤖 Agents are collaborating to analyze {company}... This may take a few minutes."):
            try:
                payload = {"company": company, "market": market}
                response = requests.post(BACKEND_URL, json=payload, timeout=300)
                response.raise_for_status()
                
                result = response.json()
                report_data = result.get('report', {})

                st.success("Analysis Complete!")
                st.markdown("---")

                # --- NEW: Section to display the verbose process ---
                st.header("🤖 Agents' Collaborative Process")
                st.markdown("See how each agent contributed to the final report.")

                tasks_output = report_data.get('tasks_output', [])
                if tasks_output:
                    for i, task in enumerate(tasks_output):
                        agent_name = task.get('agent', f'Agent {i+1}')
                        task_description = task.get('description', 'No description provided.')
                        task_output = task.get('raw', 'No output generated.')

                        with st.expander(f"**Step {i+1}: {agent_name}** - {task_description[:50]}..."):
                            st.subheader("Agent's Task")
                            st.markdown(task_description)
                            st.subheader("Agent's Output")
                            st.markdown(task_output)
                else:
                    st.warning("No verbose process data was returned from the backend.")

                st.markdown("---")

                # --- Section to display the final report ---
                st.header("📄 Final Strategic Report")
                final_report_raw = report_data.get('raw', '### Report could not be generated.\n\nPlease check the agent process above for errors.')
                
                # Clean up potential markdown code blocks for clean rendering
                if '```markdown' in final_report_raw:
                    final_report_raw = final_report_raw.replace('```markdown', '').replace('```', '')

                st.markdown(final_report_raw)

            except requests.exceptions.RequestException as e:
                st.error(f"Failed to connect to the backend API. Please ensure it's running. Error: {e}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

else:
    st.info("Your generated report and the agent process will appear here.")
