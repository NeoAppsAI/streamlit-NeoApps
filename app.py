import streamlit as st

# Set the title of the app
st.title("NeoApps.AI")

# Add a brief pitch about NeoApps.AI
st.markdown("""
### What is NeoApps.AI?
NeoApps.AI is an open-source platform designed to automate the journey from idea to deployment. It enables developers and businesses to create, build, and deploy applications rapidly with auto-generated APIs, frontends, and automated business requirements collection. Whether you're building internal tools, MVPs, or custom apps, NeoApps.AI simplifies the process with one-click deployment, integration with major cloud platforms, and a robust ecosystem for extending capabilities with LLMs and fine-tuning.
""")

# Display NeoApps.AI URLs
st.markdown("### Useful Links")
st.markdown("[Visit NeoApps.AI Website](https://neoapps.ai)")  # Replace with your actual NeoApps.AI website URL
st.markdown("[NeoApps.AI GitHub Repository](https://github.com/Neopric-Inc/NeoApps.AI-CodeGenerator)")  # Replace with your GitHub repo URL

# Add social media and communication links
st.markdown("### Connect with Us")
st.markdown("[Discord](https://discord.gg/duCszq92)")  # Replace with your Discord invite link

# List of YouTube video IDs for NeoApps.AI
video_ids = [
    "F5bmjPtciLw",  # Replace with actual YouTube video IDs related to NeoApps.AI
    "i2SOFnlYknU",
    "FzqgCyV2ZVk"
]

# Display videos in a vertical gallery
st.markdown("### NeoApps.AI Video Gallery")
for video_id in video_ids:
    st.video(f"https://www.youtube.com/embed/{video_id}")
