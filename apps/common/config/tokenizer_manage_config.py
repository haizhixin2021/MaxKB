# coding=utf-8
"""
    @project: maxkb
    @Author：虎
    @file： tokenizer_manage_config.py
    @date：2024/4/28 10:17
    @desc:
"""

from smartdoc.const import CONFIG
from transformers import GPT2TokenizerFast



class TokenizerManage:
    tokenizer = None

    @staticmethod
    def get_tokenizer():
        if TokenizerManage.tokenizer is None:
            #print("----------------------tokenizer_path------------------------")
            tokenizer_path = CONFIG.get('TOKENIZER_PATH')
            tokenizer_name = CONFIG.get('TOKENIZER_NAME')
            #print(tokenizer_path)
            TokenizerManage.tokenizer = GPT2TokenizerFast.from_pretrained(
                tokenizer_name,
                cache_dir=tokenizer_path, 
                local_files_only=True,
                resume_download=False,
                force_download=False)
        return TokenizerManage.tokenizer
