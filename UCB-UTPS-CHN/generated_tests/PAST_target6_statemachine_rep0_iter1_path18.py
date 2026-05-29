# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: not (action == 'START')
# 重复次数: 0, 迭代: 1
# 生成时间: 2026-04-18 16:49:17

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 有效输入测试
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("IDLE", 5, "RESET", "IDLE", 5, "RESET"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    ("STOPPED", 3, "RESUME", "RUNNING", 3, "RESUMED"),
    ("STOPPED", 0, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    
    # 无效动作测试
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    ("STOPPED", 0, "STOP", "STOPPED", 0, "NO_CHANGE"),
    ("COMPLETED", 10, "START", "COMPLETED", 10, "NO_CHANGE"),
    
    # 类型错误测试
    (123, 0, "START", 123, 0, "NO_CHANGE"),
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    ("IDLE", 0, 123, "IDLE", 0, "NO_CHANGE"),
    
    # 边界条件测试
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 8, "INCREMENT", "RUNNING", 9, "INCREMENTED"),
    
    # 状态转换无效测试
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    ("RUNNING", 0, "START", "RUNNING", 0, "NO_CHANGE"),
    ("STOPPED", 0, "START", "STOPPED", 0, "NO_CHANGE"),
    ("COMPLETED", 0, "START", "COMPLETED", 0, "NO_CHANGE"),
    
    # 空状态或空动作测试
    ("", 0, "START", "", 0, "NO_CHANGE"),
    ("IDLE", 0, "", "IDLE", 0, "NO_CHANGE"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result