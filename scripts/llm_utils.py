from collections import defaultdict
from openai import Completion
import pickle as pkl
from typing import List

from scripts.utils import ensure_folder_exists
def format_with_default(text, formatting_dict, default_value = "<NOT PROVIDED>"):
    return text.format_map(defaultdict(lambda: default_value, formatting_dict))

def create_openai_message(role: str, content: str) -> list:
    return [{"role": role, "content": content}]

def format_and_compile_openai_messages(message_list: List[tuple] = [("system", "You are an LLM"),
                                                                    ("user", "How are you doing?")], 
                                       formatting_dict: dict = {}) -> list:
    messages = []
    for message in message_list:
        messages += create_openai_message(message[0], format_with_default(message[1], formatting_dict))
    return messages

def prompt_gpt(openai_client, model, messages, pkl_out_path: str, pkl_this: bool = True, **kwargs) -> Completion:
    # Prompt GPT
    completion = openai_client.chat.completions.create(model=model, 
                                                       messages=messages, 
                                                       **kwargs)
    # Pickle the completion
    if pkl_this:
        ensure_folder_exists(pkl_out_path)
        pkl.dump(completion, open(pkl_out_path, "wb"))

    return completion



