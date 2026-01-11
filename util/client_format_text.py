from typing import Optional

from util.client_hot_sub import hot_sub
from util.client_strip_punc import strip_punc
from util.client_quicker import 触发Quicker操作
from util.hot_sub_rule import Quicker词典

__all__ = ['format_text']

async def format_text(text: str) -> Optional[str]:
    """
    格式化文本，进行热词替换、末尾标点消除，并检查是否触发 Quicker 操作。
    
    参数:
        text (str): 输入的文本字符串。
    
    返回:
        Optional[str]: 格式化后的文本字符串，或 None 如果触发了 Quicker 操作。
    """
# 热词替换
    text = hot_sub(text)

    # 消除末尾标点
    text = strip_punc(text)

    # 触发 Quicker 操作
    if text in Quicker词典:
        await 触发Quicker操作(Quicker词典[text])
        return "[QUICKER] " + text
    
    return text
    
