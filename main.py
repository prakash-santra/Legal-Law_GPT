import os
import streamlit as st
from key import *
from langchain.llms import OpenAI
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper

# we are Providing the key to the OS
os.environ["OPENAI_API_KEY"] = key

# Creating StreaLit User Interface
st.title("👋 Legal IndiaLaw GPT ⚖️")
prompt = st.chat_input("Tell me Your Problem")
if prompt:
    st.write({prompt})
    st.info(prompt)

# Creating the GPT Engine
llm = OpenAI(
  temperature=0.6,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# Creating Sequential Chains

input_template = PromptTemplate(input_variables=["title"], 
                                template="""You are a Lawyer Assistant. Given the User Problem , 
it is your job to find the Proper best and effective solution to face this problem according to Indian Constitution
(Remember you have to generate only the Law solution not anything else).
Your Problem Description is :
Problem: {title}
""")
input_template_chain = LLMChain(llm=llm, prompt=input_template, output_key="solution", verbose=True)

lawSection_template = PromptTemplate(input_variables=["solution"],
                                     template="""ou are a Lawyer Assistant.According to : {solution} this condition. You Have to only give the point that,
                                    this crime falls under which section of Indian Constitution. I do not 
                                    need any description in this section. Show me output like a lawyer""")
lawSection_template_chain = LLMChain(llm=llm, prompt=lawSection_template, output_key="section", verbose=True)

final_chain = SequentialChain(
    chains=[input_template_chain, lawSection_template_chain],
    input_variables=["title"],
    # Here we return multiple variables
    output_variables=["solution", "section"],
    verbose=True)

wiki_template = PromptTemplate(input_variables=["wiki_research"],
                               template="""Getting the data after Wikipedia Research : {wiki_research}
                               and give the most potential ans point wise according to indian constitution
                                 using the data only""")
wiki_chain = LLMChain(llm=llm, prompt=wiki_template, output_key="wiki_search", verbose=True)

# Wikipedia Access
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(), verbose=True)

if prompt:
    finalRes = final_chain({"title":prompt})
    wiki_res = wikipedia.run(finalRes["section"])
    wiki = wiki_chain.run(wiki_res)

    with st.expander("General Solution"):
        st.write(finalRes["solution"])
    with st.expander("Crime Comes Under Section 👇"):
        st.write(finalRes["section"])
    with st.expander("Wikipedia Result"):
        st.write(wiki)
    with st.expander("WikiPedia References"):
        st.info(wiki_res)