from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)

missileOrigin = PromptTemplate(
    input_variables=['missile'],
    template="Where is this {missile} from?"
)

missileStrength = PromptTemplate(
    input_variables=['missile'],
    template="What is the strength point of this {missile}, And why is it deadly? Only one point."
)

origin_chain = missileOrigin | llm | StrOutputParser()
strength_chain = missileStrength | llm | StrOutputParser()

chain = RunnableParallel({
    "origin": origin_chain,
    "strength": strength_chain
})

response = chain.invoke({"missile": "RS-28 Sarmat"})

print("Country of Origin:", response['origin'])
print("Strength:", response['strength'])