from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import AIMessage
from langchain_core.pydantic_v1 import BaseModel,Field
from langchain_core.output_parsers import JsonOutputParser
from flask import Flask,jsonify,request
from flask_cors import CORS


class JsonCreater(BaseModel):
    Question: str = Field(description="Question")
    Options: list = Field(description="Options for the answer in a list format")
    Answer: str = Field(description="Answer to the question")
    Reason: str = Field(description="Reason for the answer")


def get_schema(_):
    schema = db.get_table_info()
    return schema

def Parse(message: AIMessage) -> str:
    return message.content.split('\n')[1]

def run_query(query):
    return db.run(query)

MySQL_URI = 'mysql+mysqlconnector://root:Niranjan05%40@localhost:3306/Anki'
db = SQLDatabase.from_uri(MySQL_URI)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",google_api_key="AIzaSyBIOJ5f61Wq8S8Nx36IOhS_gdkCN_rBcx8")
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/summary",methods=['POST'])
def summary():
    question = request.json.get('question')
    template = """Based on the table schema given below, write an SQL query responding to that user's question. You do not have permission to modify the structure of the database or the tables. The answer must strictly be only in this format.
    There must be no characters before or after the query. : 
    {schema}

    Question : {question}
    SQL Query:"""
    prompt = ChatPromptTemplate.from_template(template)

    full_template = """Based on the given user's question and Query Response generate MCQ based questions. They must consist of tricky options. Generate 4 options. Only give me the question,options,correct answer and the reason for the correct answer.
    Respond with a JSON object using the following instructions :
    {{
        "Question": "<The question in a string format>",
        "Options": "<The multiple choice options as a list>",
        "Answer": "<The answer must be in a string format>",
        "Reason": "<The reason for the answer>"
    }}
    {schema}

    Question : {question}
    SQL Query : {query}
    SQl Response : {response}
    """
    prompt_response = ChatPromptTemplate.from_template(full_template)

    Sql_Chain = (
        RunnablePassthrough.assign(schema = get_schema)
        | prompt
        | llm
        | Parse
    )
    parser = JsonOutputParser(pydantic_object=JsonCreater)

    full_chain = (
        RunnablePassthrough.assign(query=Sql_Chain).assign(
            schema=get_schema,
            response=lambda vars: run_query(vars["query"]),
        )
        | prompt_response
        | llm
        | parser
    )
    return jsonify(full_chain.invoke({"question":question}))

@app.route("/alternative",methods=['POST'])
def alternative():
    question = request.json.get('question')
    answer = request.json.get('answer')
    template = """Based on the given user's question and answer generate MCQ based questions. They must consist of tricky options. Generate 4 options. Only give me the question,options,correct answer and the reason for the correct answer.
    Respond with a JSON object using the following instructions :
    {{
        "Question": "<The question in a string format>",
        "Options": "<The multiple choice options as a list>",
        "Answer": "<The answer must be in a string format>",
        "Reason": "<The reason for the answer>"
    }}
    Question : {question}
    Answer : {answer}
    """
    parser = JsonOutputParser(pydantic_object=JsonCreater)
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm | parser

    return jsonify(chain.invoke({"question":question,"answer":answer}))

if __name__ == '__main__':
    print("Starting Flask Server...")
    app.run()

