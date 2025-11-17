from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
load_dotenv()

# ChatOpenAl 초기화 
llm = init_chat_model("gpt-4o-mini", model_provider="openai") 

# 프롬프트 템플릿 생성 
prompt = ChatPromptTemplate.from_messages([ 
    ("system", "You are a helpful assistant."), 
    ("user", "{input}") 
]) 

# 문자열 출력 파서 
output_parser = StrOutputParser()

# LLM 체인 구성 
chain = prompt | llm | output_parser
# result = chain.invoke({"input": "hi"}) 
# print(result) 

# 체인 실행
content = "코딩" 
result = chain.invoke({"input": content + " 에 대한 시를 써줘 " }) 
print(result) 

st.title("this is a title")
st.title('Streamlit_ is :blue[cool] :sunglasses:') 

#터미널에서 st run main.py  실행

# 제목 
st.title( "인공지능 시인" ) 

# 시와 주제 입력 받기
content = st.text_input( "시와 주제를 제시해주세요 " )
# st.write("시의 주제는" , content)

# 시 작성 요청하기 
if st.button( "시 작성 요청하기" ) : 
    with st.spinner('작성 중입니다...'): 
        result = chain.invoke({"input": content + " 에 대한 시를 써줘 " }) 
        st.write(result)

