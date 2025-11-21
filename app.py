import streamlit as st

st.set_page_config(page_title="Transformation Assistant Prototype", layout="wide")

st.title("🧭 Transformation Assistant (Prototype)")

st.write(
    "This prototype helps managers spot early transformation risks and get quick guidance."
)

# Sidebar: basic project info
st.sidebar.header("Project Context")
project_name = st.sidebar.text_input("Project name", "Finance System Rollout")
project_type = st.sidebar.selectbox(
    "Type of transformation",
    ["System rollout", "Org restructure", "Policy change", "Process change", "Other"],
)
phase = st.sidebar.selectbox(
    "Current phase",
    ["Planning", "Pilot", "Rollout", "Stabilisation"],
)

st.sidebar.markdown("---")
st.sidebar.caption("Prototype only – logic is simple keyword-based for now.")

# Main: input section
st.subheader("Team Communications")
notes = st.text_area(
    "Paste recent meeting notes or email snippets:",
    height=200,
    placeholder="E.g. team is complaining about extra workload, some managers are quiet, deadlines keep slipping...",
)

# Simple, fake analysis logic (no LLM yet)
def simple_risk_analysis(text: str) -> dict:
    text_lower = text.lower()
    keywords_high = ["resist", "push back", "complain", "angry", "refuse", "delay", "delayed", "not doing"]
    keywords_medium = ["confused", "unclear", "worried", "concern", "overwhelmed", "too busy"]

    score = 0
    for kw in keywords_high:
        if kw in text_lower:
            score += 2
    for kw in keywords_medium:
        if kw in text_lower:
            score += 1

    if score >= 4:
        level = "🚨 High"
        msg = "There are strong signs of resistance or stress. You may need direct interventions soon."
    elif score >= 2:
        level = "⚠️ Medium"
        msg = "Some early warning signs are present. This is a good time to clarify benefits and listen to concerns."
    else:
        level = "✅ Low"
        msg = "No obvious resistance signals detected from the text. Still keep an eye on morale."

    return {"level": level, "message": msg, "score": score}

if st.button("Analyse"):
    if not notes.strip():
        st.warning("Please paste some notes first.")
    else:
        result = simple_risk_analysis(notes)

        st.subheader("Risk Snapshot")
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Detected Risk Level", result["level"])
        with col2:
            st.metric("Risk Score (prototype)", result["score"])

        st.write(result["message"])

        st.markdown("### Suggested Next Steps (Prototype)")
        if "High" in result["level"]:
            st.markdown(
                """
                - Schedule 1:1s with key influencers or vocal resisters.
                - Run a short listening session: “What’s hardest about this change right now?”
                - Agree on 1–2 quick wins to show that feedback leads to action.
                """
            )
        elif "Medium" in result["level"]:
            st.markdown(
                """
                - Clarify the **why** behind the transformation in concrete, practical terms.
                - Ask team leads to surface questions anonymously (e.g. via a simple form).
                - Share a small success story or quick win from the project.
                """
            )
        else:
            st.markdown(
                """
                - Keep communicating progress in simple, human language.
                - Highlight small wins and recognise early adopters.
                - Check-in regularly; low risk doesn’t mean no risk.
                """
            )

st.markdown("---")
st.caption(
    f"Prototype for project: **{project_name}** ({project_type}, phase: {phase}). "
    "No LLM yet – this is just to prove the Streamlit concept."
)
