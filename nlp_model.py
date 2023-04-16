import pandas as pd
import streamlit as st
import openai


openai.api_key = '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'
def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()


data = [(1, "The response time for my emergency call was too long, and I had to wait for almost an hour.", "Negative"),    (2, "The officer who assisted me was very rude and unprofessional, which made me uncomfortable.", "Negative"),    (3, "The police department should do more to address community concerns and engage with the residents.", "Neutral"),    (4, "I appreciate the efforts of the police department in keeping our neighborhood safe.", "Positive"),    (5, "I was impressed with how well the officers handled a difficult situation during a crisis.", "Positive"),    (6,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  "There needs to be more transparency in how the department handles complaints and investigations.", "Neutral"),    (7, "The police officers who helped me were very friendly and professional, which made me feel safe.", "Positive"),    (8, "I had a great experience with the police department and appreciate their prompt response.", "Positive"),    (9, "The department needs to do a better job in training their officers on how to handle mental health crises.", "Negative"),    (10, "The police department should be more proactive in addressing the issue of racial profiling.", "Neutral")]

columns = ["ID", "Feedback Text", "Feedback"]
df = pd.DataFrame(data=data, columns=columns)

st.title("NLP Model to analyze customer feedback")
st.subheader("Sample Feedback Data")
#drop the first column
df = df.drop(columns=['ID'])
st.write(df.head()) 

#plot the all sentiments of this data
st.subheader("Sentiment Distribution")
#show the plot on screen
st.bar_chart(df['Feedback'].value_counts(), width=0, height=0, use_container_width=True)


st.subheader("User's feedback")
feedback = 'The response time for my emergency call was too long, and I had to wait for almost an hour'
#wait for the 10 seconds before generating the feedback
#show this user feedback on screen
st.write(feedback)
st.write("  ")
st.write("  ")


st.write("Generating feedback...")
st.write("Please wait...")
    
prompt = "Identify key areas for product or service improvement from the feedback below:" + feedback + " write it in points"

st.subheader("Generated Feedback")
st.write(generate_text(prompt))
