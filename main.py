from langchain_groq import ChatGroq
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def generate_business_name(expertise: str) -> str:
    """Generate a unique name for a business specializing in {expertise}"""
    llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0.7)
    
    prompt = f"Generate 5 creative and a name for a business specialising in {expertise}. Just the name, nothing else."
    response = llm.invoke(prompt)
    
    return response.content.strip()

if __name__ == "__main__":
    business_name = generate_business_name("Business and IT services")
    print(f"Generated name: {business_name}")