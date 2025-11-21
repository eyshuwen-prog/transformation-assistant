import streamlit as st

st.set_page_config(page_title="About Us – Transformation Assistant", layout="wide")

st.title("About the Transformation Assistant Prototype")

st.markdown("""
### Project Scope

The **Transformation Assistant** is a proof-of-concept Streamlit application that helps managers
and transformation teams **detect early signs of resistance** and **apply change-management
best practices consistently**.

In many transformation projects, qualitative warning signals are buried in:
- meeting notes,
- email threads, and
- informal updates.

Traditional dashboards tend to miss these signals, and external consultants are expensive and
not always available. This prototype demonstrates how a lightweight **LLM-powered assistant**
can augment transformation teams by:

- Monitoring team communications for potential risks, and  
- Providing **contextual, action-oriented guidance** to managers.
""")

st.markdown("""
### Objectives

This prototype aims to:

1. **Identify early warning signs** of resistance or misalignment from unstructured text
   (e.g. meeting notes, emails, chat logs).
2. **Summarise transformation health** in simple language that managers can quickly understand.
3. **Recommend concrete interventions** using established transformation / change-management
   frameworks (e.g. clarify the “why”, quick wins, targeted 1-to-1 conversations).
4. Demonstrate how such an assistant can be integrated into existing workflows as a **daily
   support tool** rather than a one-off report.
""")

st.markdown("""
### Use Cases Covered in This Prototype

This version of the app focuses on two key use cases:

1. **Communications Risk Scanner**
   - User pastes recent **meeting notes** or **email snippets**.
   - The app analyses the text for:
     - sentiment,
     - resistance patterns (e.g. “we are too busy”, “this will not work”),
     - potential risks to timelines or adoption.
   - It outputs a **risk level** (Low / Medium / High) and recommended next steps.

2. **Transformation Knowledge Copilot** (optional extension)
   - User asks questions like:
     - “How should I handle a team that is silently resistant?”
     - “What should I do when leaders are not visibly supporting the change?”
   - The app uses an LLM plus a curated knowledge base of transformation best practices
     to provide **tailored guidance** and examples (e.g. sample talking points, checklist of actions).
""")

st.markdown("""
### Data Sources

For this prototype, we assume the following sources of information:

- **User-provided text:**  
  Meeting notes, email snippets, or summaries manually pasted into the app.
  In a real deployment, these could be integrated via connectors (e.g. internal note-taking tools,
  ticketing systems, or collaboration platforms), but for the hackathon we rely on **manual input**
  and/or mock data.

- **Transformation Best Practices Library:**  
  A curated set of guidelines from:
  - public change-management literature,
  - internal playbooks and governance documents (if available and permitted),
  - organisational SOPs or communication templates.

- **Mock / Anonymised Data:**  
  Because transformation-related communications often contain sensitive information, a real-world
  implementation would require data classification, down-classification, or the use of **mock data
  with the same structure but no real names or confidential details**. :contentReference[oaicite:1]{index=1}
""")

st.markdown("""
### Key Features in This Prototype

- 📊 **Risk Snapshot**  
  Quick view of transformation risk (Low / Medium / High) based on the text provided.

- 🧩 **Resistance Pattern Detection**  
  Highlights common resistance themes (e.g. fear of workload, lack of clarity, low leadership support).

- ✅ **Actionable Recommendations**  
  Provides 2–3 concrete next steps aligned with transformation best practices, such as:
  - clarify the “why” of the change,
  - run short listening sessions,
  - identify quick wins and early adopters.

- 🧮 **Extensible Design**  
  The current prototype uses simplified logic and/or a single LLM call, but the design is intended
  to be extended with:
  - additional data sources,
  - more sophisticated categorisation,
  - evaluation metrics (e.g. user feedback, outcome tracking).
""")

st.markdown("""
### Security and Access (Prototype Level)

- This app is intended primarily as a **demonstration prototype**.
- In a production setting, it is strongly recommended to:
  - **password-protect** the application,
  - enforce access controls (e.g. only transformation team / managers),
  - ensure that only appropriately classified data is used (e.g. mock or down-classified data where necessary). :contentReference[oaicite:2]{index=2}
""")
