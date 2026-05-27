# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: not (state != 'RUNNING')
# 重复次数: 1, 迭代: 8
# 生成时间: 2026-04-26 06:35:57

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 状态转换测试
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    ("STOPPED", 3, "RESUME", "RUNNING", 3, "RESUMED"),
    ("STOPPED", 3, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    
    # 类型错误测试
    (123, "test", "START", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", "test", "START", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", 5, 123, "IDLE", 0, "NO_CHANGE"),
    
    # 边界条件测试
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 0, "INCREMENT", "RUNNING", 1, "INCREMENTED"),
    
    # 无效动作测试
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 5, "START", "RUNNING", 5, "NO_CHANGE"),
    ("STOPPED", 3, "INCREMENT", "STOPPED", 3, "NO_CHANGE"),
    ("COMPLETED", 10, "RESUME", "COMPLETED", 10, "NO_CHANGE"),
    
    # 状态不为 RUNNING 的情况
    ("IDLE", 5, "INCREMENT", "IDLE", 5, "NO_CHANGE"),
    ("STOPPED", 5, "INCREMENT", "STOPPED", 5, "NO_CHANGE"),
    ("COMPLETED", 5, "INCREMENT", "COMPLETED", 5, "NO_CHANGE"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result