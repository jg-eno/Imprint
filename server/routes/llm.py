from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import AIMessage
from langchain_core.pydantic_v1 import BaseModel,Field
from langchain_core.output_parsers import JsonOutputParser
from flask import Flask,jsonify,request
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from config import Config

class JsonCreater(BaseModel):
    Question: str = Field(description="Question")
    Options: list = Field(description="Options for the answer in a list format")
    Answer: str = Field(description="Answer to the question")
    Reason: str = Field(description="Reason for the answer")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",google_api_key=Config.GOOGLE_API_KEY)
llm_bp = Blueprint("llm", __name__)

@llm_bp.route('/llm/generate', methods=['POST'])
#@jwt_required()
def add_card():
    data = request.get_json()
    question = data.get("question")
    answer = data.get("answer")

    if not question or not answer:
        return jsonify({"error": "Values question and answer is required"}), 400

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


if __name__ == "__main__":
    print(
        "Please run imprint/server/app.py instead. See imprint/README.md for details."
    )
