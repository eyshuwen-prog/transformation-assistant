import streamlit as st

st.set_page_config(page_title="About Us – Transformation Assistant", layout="wide")

st.title("About This Prototype")
st.write("### Transformation Assistant – Communications Risk Scanner")

st.markdown("""
This Streamlit application is a **working web-based prototype** of a
**Transformation Assistant**. It is designed to help managers and transformation teams:

1. **Detect early warning signs** of resistance in team communications; and  
2. **Receive AI-assisted guidance** on how to respond constructively.

The app focuses on a single, clearly scoped use case:

> **Use Case 1 – Communications Risk Scanner**  
> Analyse meeting notes, emails, or informal updates to identify early transformation risks and suggest targeted interventions.
""")

st.write("### Alignment with Assessment Criteria")

st.markdown("""
**1. Functionality & User Experience**

- The application is deployed as a **public web app** and accessible via URL.  
- The interface is **multi-page**:
  - Home (Prototype)
  - About Us
  - Methodology  
- The main flow is structured into three clear steps:
  1. Enter project context
  2. Paste team communications
  3. Run risk scan and (optionally) call the LLM for deeper guidance  
- Output is presented in a user-friendly way:
  - risk metrics,
  - visual charts,
  - AI-generated summaries and scripts.

**2. Technical Implementation**

- A **rule-based risk engine** provides transparent, deterministic scoring.  
- A **mini LLM feature** (OpenAI) is integrated to:
  - summarise the situation,
  - suggest next steps,
  - generate leadership scripts.  
- Prompt engineering and safety are applied:
  - clear system prompts,
  - simple input sanitisation,
  - explicit instructions to ignore harmful or irrelevant instructions in user text.

**3. Innovation & Creativity**

- The app combines:
  - **keyword-based analytics** (risk score, keyword heatmap),
  - **AI narrative guidance** (summary + leadership script), and
  - a **manager readiness indicator**.  
- This shows how qualitative signals can be turned into:
  - visuals,
  - structured metrics,
  - practical talking points for leaders.

**4. Documentation**

- The **About Us** page explains:
  - scope,
  - objectives,
  - target users,
  - features, and
  - assessment alignment.  
- The **Methodology** page details:
  - data flow,
  - analysis steps,
  - LLM prompts,
  - prompt chaining,
  - safety design, and
  - a clear flowchart.
""")

st.write("### Project Scope")

st.markdown("""
This prototype focuses on the **analysis of unstructured text** related to transformation projects.

**Scope includes:**
- Manual input of team communications (meeting notes, emails, free text)
- Keyword-based detection of risk signals
- Risk scoring and **Manager Readiness** indicator
- LLM-powered:
  - summary and guidance, and
  - leadership script generation

**Scope excludes (for this version):**
- Automatic integration with email, chat, or ticketing systems
- Multi-use-case agents (e.g. search, document Q&A)
- Persistence of data, logging, or analytics dashboards
""")

st.write("### Target Users")

st.markdown("""
- Transformation and innovation teams  
- Project and programme managers  
- Change managers and HR business partners  
- Directors and team leads responsible for major changes  
""")

st.write("### Key Features")

st.markdown("""
- 📌 **Risk Snapshot** – simple High / Medium / Low indicator with score  
- 📌 **Manager Readiness Score** – indicative readiness based on detected risk signals  
- 📌 **Keyword Heatmap** – highlights which words signalled resistance or concern  
- 📌 **AI Summary & Guidance (LLM)** – contextual summary and 3 recommended actions  
- 📌 **Leadership Script Generator (LLM)** – draft talking points for the next team check-in  
""")

st.write("### Data Disclaimer")

st.markdown("""
This prototype is intended for **demonstration and learning**.

- Do **not** enter real sensitive or personal data into the app.  
- Use mock or anonymised samples that resemble real communications.  
- A production deployment would require:
  - strict access controls,
  - data classification review,
  - secure hosting, and
  - formal approval.
""")
