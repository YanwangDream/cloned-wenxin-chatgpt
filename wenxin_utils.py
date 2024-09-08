import os
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import QianfanLLMEndpoint
from langchain.chains import ConversationChain
def get_wenxinchat_response(memory,prompt,api_key,secret_key):
    os.environ["QIANFAN_AK"] = api_key
    os.environ["QIANFAN_SK"] = secret_key
    model = QianfanLLMEndpoint(temperature=0.9,model="ernie-speed-128k",streaming=True)
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke(prompt)
    # print(response)
    return response["response"]


# memory = ConversationBufferMemory(return_messages=True)
# print(get_wenxinchat_response(memory,"牛顿提出过哪些知名的定律？"))
# print(get_wenxinchat_response(memory,"你是小明一名科学家"))
# print(get_wenxinchat_response(memory,"我上一个问题是什么？"))