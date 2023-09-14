# 👋 Legal-Law_GPT ⚖
Get Instant solution and sections to better understand the Laws related to specific activities or behaviors.And provide a wikipedia research about your Crime and provide You a better approach to handel the Situation.

# 📚 API References for Better Understanding
To help you gain a deeper understanding of this project, we've provided comprehensive API references that detail the endpoints, data structures, and usage of the APIs utilized within this codebase. These references are designed to assist both developers familiar with the project and newcomers looking to explore its functionality.
# FOLLOW These 👇
1. LangChain API ("https://python.langchain.com/docs/get_started/introduction")
            
2. LangChain LLM Chains ("https://python.langchain.com/docs/modules/chains/foundational/llm_chain")
            
3. LangChain Sequential Chains ("https://python.langchain.com/docs/modules/chains/foundational/sequential_chains")
   ```python
   from langchain.llms import OpenAI
   from langchain.chains import LLMChain
   from langchain.prompts import PromptTemplate
   
 5. Prompt Template ("https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/")

       input_template = PromptTemplate(input_variables=["title"],template="""Your Problem Description is :{title}""")
 6.LangChain API For WikiPedia Ref : ("https://python.langchain.com/docs/integrations/tools/wikipedia")
 7. OPENAI_API_KEY Generate ("https://platform.openai.com/account/api-keys")
    >NOTE : You have To provide Your API key inside the key.py File(key = "for xample here..."
 8. Streamlit Docs ("https://docs.streamlit.io/library/api-reference")


# Code Explanation Here 👇
 ```python
    # Legal IndiaLaw GPT ⚖️

![Legal IndiaLaw GPT](insert_image_url_here) <!-- You can add an image or logo here -->

This is a Streamlit-powered Legal Assistant powered by the GPT-3 model from OpenAI. It helps users find legal solutions based on Indian Constitution and provides information from Wikipedia for reference.

## Getting Started

### Prerequisites

Before running this application, make sure you have the following prerequisites installed:

- Python
- Streamlit
- OpenAI API Key
- Other dependencies (specified in `requirements.txt`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
```
# Install the required dependencies:
```python
pip install -r requirements.txt
```
```
```
# Set up your OpenAI API key:
```python
# Set your OpenAI API key in a key.py file
os.environ["OPENAI_API_KEY"] = "your_api_key_here"

```
```
```
# Usage
Run the Streamlit app::
```python
streamlit run your_app.py
```

## Features
    1. Chat interface for interacting with the Legal Assistant.
    2. Generates legal solutions based on the Indian Constitution.
    3. Identifies the section of the Indian Constitution related to the legal problem.
    4. Provides Wikipedia references for additional information.

## Acknowledgments
>       1. Thanks to OpenAI for the powerful GPT-3 model.
        2. Inspiration for this project came from the need for accessible legal assistance in India.

```python
    
You can customize this README to include additional information about your project, such as installation instructions, usage examples, license details, and acknowledgments. Be sure to replace `insert_image_url_here` with the URL of your project's logo or a relevant image.
```
## Request Feedback in README:
>        If you find this project helpful or have suggestions for improvements, we'd love to hear from you! Please consider leaving feedback by opening an issue or reaching out to us.

## If you find this project useful, please consider giving it a star ⭐ to show your support.
 
# My Awesome Project 👇  

![Example Image](https://github.com/prakash-santra/Legal-Law_GPT/assets/101620255/f90b2935-dceb-42a7-9580-69d3f9503d98)

![2](https://github.com/prakash-santra/Legal-Law_GPT/assets/101620255/eedb227f-84f0-44e1-9eb6-8f4d3fb63a9e)

![3](https://github.com/prakash-santra/Legal-Law_GPT/assets/101620255/e21f4373-f860-4e3b-93de-414b47e01b31)

![4](https://github.com/prakash-santra/Legal-Law_GPT/assets/101620255/3f4760f8-1448-4c97-b956-0de76d6b5664)

![5](https://github.com/prakash-santra/Legal-Law_GPT/assets/101620255/57caf7c7-5a24-4765-9143-856b4da2f7f7)

![6](https://github.com/prakash-santra/Legal-Law_GPT/assets/101620255/86afd699-a0bb-4ffc-966d-763331b8ae9a)

![7](https://github.com/prakash-santra/Legal-Law_GPT/assets/101620255/9528eff4-dccf-4145-8b3f-8b5cca6c05d9)








