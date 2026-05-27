# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: not isinstance(state, str) or not isinstance(counter, int) or (not isinstance(action, str))
# 重复次数: 0, 迭代: 1
# 生成时间: 2026-04-26 06:32:55

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 有效输入测试
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("RUNNING", 5, "INCREMENT", "RUNNING", 6, "INCREMENTED"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    ("STOPPED", 5, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    
    # 类型错误测试
    (123, 0, "START", 123, 0, "NO_CHANGE"),
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    ("IDLE", 0, 123, "IDLE", 0, "NO_CHANGE"),
    (123, "test", 123, 123, "test", "NO_CHANGE"),
    
    # RUNNING 状态下 RESET 不生效
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    ("RUNNING", 10, "RESET", "RUNNING", 10, "NO_CHANGE"),
    
    # counter 达到 10 后 INCREMENT 不生效
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    
    # 无效动作
    ("IDLE", 0, "INVALID", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 5, "INVALID", "RUNNING", 5, "NO_CHANGE"),
    ("STOPPED", 5, "INVALID", "STOPPED", 5, "NO_CHANGE"),
    ("COMPLETED", 10, "INVALID", "COMPLETED", 10, "NO_CHANGE"),
    
    # 边界条件测试
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("STOPPED", 10, "RESUME", "RUNNING", 10, "RESUMED"),
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result