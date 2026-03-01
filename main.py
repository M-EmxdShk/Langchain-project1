import whoisdomain as whois
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

@tool
def check_domain_availability(domain_name: str) -> str:
    """
    Checks if a .com domain is available or already taken.
    Input should be a string like 'google.com' or 'mybrand.com'.
    """
    try:
        # I have queried the WHOIS servers
        domain = whois.query(domain_name)
        
        if domain is None or not domain.registrar:
            return f"The domain {domain_name} is AVAILABLE!"
        else:
            return f"The domain {domain_name} is TAKEN by {domain.registrar}."
    except Exception as e:
        return f"Could not verify {domain_name}. It might be available."


def generate_and_check_business(expertise: str):
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
    
    llm_with_tools = llm.bind_tools([check_domain_availability])
    
    prompt = f"Find a cool business name for {expertise}. Check if the .com is available before suggesting it."
    
    response = llm_with_tools.invoke(prompt)
    if response.tool_calls:
        for tool_call in response.tool_calls:
            result = check_domain_availability.invoke(tool_call["args"])
            print(f"Tool Result: {result}")
            
    print(f"AI Response: {response.content}")

if __name__ == "__main__":
    generate_and_check_business("AI-powered gardening")