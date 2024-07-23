import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import backend

st.set_page_config(
    page_title="Main Page",
    page_icon="👋",
)

# Custom CSS to increase font size and change font style
st.markdown("""
<style>
    .big-font {
        font-size: 300%;
        font-style: san-serif; /* Change font style here */
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='big-font'>Welcome to Gradewise.ai! 🤖</h1>", unsafe_allow_html=True)

st.markdown(
    """
    Traditional essay evaluation poses significant challenges for both teachers and students. Teachers often find themselves burdened with the task of manually reviewing numerous essays, leading to time constraints and potential delays in providing feedback. Consequently, students may not receive timely guidance on their writing, impacting their learning and academic performance.

At Gradewise AI, we recognize the need for a more efficient and personalized approach to essay evaluation. Our platform revolutionizes the grading process by leveraging artificial intelligence to automate and enhance feedback delivery. Here's how it works:

Streamlined Submission Process: Users can easily upload a zip file containing PDFs of student essays. This eliminates the need for manual entry and ensures all submissions are organized in one place.

Automated Text Extraction: Our system extracts the text from each essay, making it accessible for analysis by our AI model. This step saves valuable time for teachers and ensures accurate evaluation of student work.

AI-Powered Evaluation: Using advanced natural language processing algorithms, our AI model thoroughly analyzes each essay. It assesses various aspects such as grammar, coherence, argumentation, and vocabulary usage to provide comprehensive feedback.

Personalized Feedback: Gradewise AI generates detailed feedback tailored to each student's essay. This includes suggestions for improvement, areas of strength, and specific examples to illustrate key points. By addressing individual needs, students receive targeted guidance to enhance their writing skills.

#### Grading and Reporting
- In addition to feedback, our platform assigns grades based on predefined criteria or customizable rubrics. Teachers can easily review and track student progress through an intuitive dashboard, which displays overall performance metrics and trends.

With Gradewise AI, educators can optimize their time and resources while providing valuable support to students. By automating essay evaluation and delivering personalized feedback, we empower educators to focus on facilitating learning and fostering academic growth. Our platform not only enhances the teaching experience but also enriches the learning journey for students, ultimately driving improved outcomes and success.
"""
)
st.markdown("## Lets get started!")
page_1 = st.button("Go to step 1 - Upload Student data")
if page_1:
    switch_page("step1️⃣ - upload student data and essay📄")