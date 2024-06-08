#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：MaxKB 
@File    ：deepseek_chat_model.py
@Author  ：Brian Yang
@Date    ：5/12/24 7:44 AM 
"""
from typing import List

from langchain_core.messages import BaseMessage, get_buffer_string
from langchain_openai import ChatOpenAI

from common.config.tokenizer_manage_config import TokenizerManage


class DeepSeekChatModel(ChatOpenAI):
    def get_num_tokens_from_messages(self, messages: List[BaseMessage]) -> int:
        print("-----------------------------------deepseek_chat_model.py DeepSeekChatModel get_num_tokens_from_messages20240601---------------")
        try:
            print("----------------------------------------xdsfdsfsdfsd------------------")
            return super().get_num_tokens_from_messages(messages)
        except Exception as e:
            print(e)
            tokenizer = TokenizerManage.get_tokenizer()
            print("-------------------------exception-----------------------------")
            print(sum([len(tokenizer.encode(get_buffer_string([m]))) for m in messages]))
            return sum([len(tokenizer.encode(get_buffer_string([m]))) for m in messages])

    def get_num_tokens(self, text: str) -> int:
        print("-----------------------------------deepseek_chat_model.py DeepSeekChatModel get_num_tokens------------------")
        try:
            return super().get_num_tokens(text)
        except Exception as e:
            tokenizer = TokenizerManage.get_tokenizer()
            return len(tokenizer.encode(text))
