import streamlit as st
import trafilatura

# Setup
st.set_page_config(page_title="Deep Reader", layout="centered", page_icon="📖")

def main():
    st.title("📖 Deep Reader")
    st.caption("Clean reading, zero distractions, zero slop.")

    # Input in the main area for faster flow
    url = st.text_input("Paste URL here:", placeholder="https://example.com/article")
    
    if url:
        with st.spinner("Stripping noise..."):
            downloaded = trafilatura.fetch_url(url)
            
            if downloaded:
                # Extracting as markdown for structure
                content = trafilatura.extract(downloaded, output_format='markdown')
                
                if content:
                    st.divider()
                    st.markdown(content)
                    st.divider()
                    st.button("Clear", on_click=lambda: st.rerun())
                else:
                    st.error("Extraction failed. The content might be hidden behind a login or script.")
            else:
                st.error("Unable to reach the website.")
    
    # Minimalist Footer
    st.markdown("---")

    st.markdown(
        """
        <div style="text-align: center; color: gray; font-size: 0.8em;">
            Developed by George Freedom - For Better Focus !<br>
            <a href="https://www.linkedin.com/in/georgefreedom/" target="_blank">LinkedIn</a> | 
            <a href="https://www.georgefreedom.com" target="_blank">Website (blog)</a>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
