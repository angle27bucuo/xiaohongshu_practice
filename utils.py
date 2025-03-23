from langchain.output_parsers import PydanticOutputParser
from prompt_template import system_template_text,user_template_text
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from xiaohongshu_model import Xiaohongshu
import os
def generate_xiaohongshu(theme,api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system",system_template_text),
        ("user",user_template_text)
    ])
    model = ChatOpenAI(model="deepseek-chat",
                       api_key=api_key,
                       base_url="https://api.deepseek.com")
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    chain = prompt|model|output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })
    return result

# print(generate_xiaohongshu("大模型",os.getenv("DEEPSEEK_API_KEY")))