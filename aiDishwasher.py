from langchain_openai import ChatOpenAI
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os
import json


class AiDishwasher:
    def __init__(self):
        load_dotenv()
        model = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
        self.config = {"configurable": {"session_id": "AI assistant"}}
        self.with_message_history = RunnableWithMessageHistory(model, self.get_session_history)
        self.system_prompt = os.getenv("SYSTEM_PROMPT")
        self.store = {}
        self.response = {}

    def get_session_history(self, session_id: str):
        if session_id not in self.store:
            self.store[session_id] = InMemoryChatMessageHistory()
        return self.store[session_id]

    def add_system_prompt(self):
        initial_system_message = SystemMessage(content=self.system_prompt)
        self.with_message_history.invoke([initial_system_message], config=self.config)

    def start(self):
        self.add_system_prompt()
        while True:
            user_input = input("Jaki program mam włączyć ?: ")
            if user_input.lower() in ["koniec", "wyłącz się"]:
                break
            else:
                response = self.with_message_history.invoke([HumanMessage(content=user_input)], config=self.config)
                self.response = json.loads(response.content)
                print(self.response)
                if self.response["program"] is not None:
                    with open("./output/output.json", "w") as file:
                        json.dump(self.response, file)
                    break
