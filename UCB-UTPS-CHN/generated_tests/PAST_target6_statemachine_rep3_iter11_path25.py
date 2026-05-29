# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: not (counter >= 10)
# 重复次数: 3, 迭代: 11
# 生成时间: 2026-04-18 16:57:03

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 无效输入类型
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    (123, 0, "START", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", 0, 123, "IDLE", 0, "NO_CHANGE"),
    
    # IDLE 状态测试
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),
    
    # RUNNING 状态测试
    ("RUNNING", 9, "INCREMENT", "RUNNING", 10, "INCREMENTED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 9, "STOP", "STOPPED", 9, "STOPPED"),
    ("RUNNING", 9, "RESET", "RUNNING", 9, "NO_CHANGE"),
    
    # STOPPED 状态测试
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    ("STOPPED", 5, "RESET", "IDLE", 0, "RESET"),
    ("STOPPED", 5, "START", "STOPPED", 5, "NO_CHANGE"),
    
    # COMPLETED 状态测试
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 10, "STOP", "COMPLETED", 10, "NO_CHANGE"),
    
    # 边界条件测试
    ("RUNNING", 9, "INCREMENT", "RUNNING", 10, "INCREMENTED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 8, "INCREMENT", "RUNNING", 9, "INCREMENTED"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    
    # 无效动作测试
    ("IDLE", 0, "RESUME", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 0, "RESET", "RUNNING", 0, "NO_CHANGE"),
    ("STOPPED", 0, "INCREMENT", "STOPPED", 0, "NO_CHANGE"),
    ("COMPLETED", 0, "START", "COMPLETED", 0, "NO_CHANGE"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result