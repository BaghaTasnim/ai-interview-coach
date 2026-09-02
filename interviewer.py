from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_interview_question(topic, level, conversation_history, pdf_text=""):
    
    if pdf_text:
        context = f"\nUse this document content to create interview questions:\n{pdf_text[:3000]}"
    else:
        context = ""
    
    system_prompt = f"""You are a professional technical interviewer for {level} level {topic} positions.{context}
Ask one interview question at a time.
After the candidate answers, give feedback:
- What was good ✅
- What was missing ❌
- A better answer 💡
- Score out of 10

Then ask the next question."""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": system_prompt}
        ] + conversation_history,
        temperature=0.7,
        max_tokens=500
    )
    
    return response.choices[0].message.content