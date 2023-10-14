from autogen import AssistantAgent, UserProxyAgent

import os
work_dir = os.getcwd()

config_list = [{
    'model' : 'gpt-4-0613',
    'api_key' : 'YOUR API KEY HERE'
}
]

llm_config = {'config_list': config_list}

assistant = AssistantAgent(
    name = "assistant",
    llm_config=llm_config,
    is_termination_msg=lambda x:True if "TERMINATE" in x.get("content") else False
)


user_proxy = UserProxyAgent(
    name = "user_proxy",
    human_input_mode= "NEVER",
    is_termination_msg=lambda x:True if "TERMINATE" in x.get("content") else False,
    max_consecutive_auto_reply= 10,
    code_execution_config={
        "work_dir": work_dir,
        "use_docker": True,
    }
)

user_proxy.initiate_chat(
    assistant,
    message = """Find the top 5 arxiv papers that show how people are studying the regulatory and Policy Aspects in AI based systems. Then Summarize and write a Literature review on the same topic"""
)