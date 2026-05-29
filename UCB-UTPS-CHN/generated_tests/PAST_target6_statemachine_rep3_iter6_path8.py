# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: not (state != 'RUNNING')
# 重复次数: 3, 迭代: 6
# 生成时间: 2026-04-18 16:56:25

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试类型检查
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    (123, 0, "START", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", 0, 123, "IDLE", 0, "NO_CHANGE"),
    
    # IDLE 状态测试
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),
    
    # RUNNING 状态测试
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    ("RUNNING", 5, "START", "RUNNING", 5, "NO_CHANGE"),
    
    # STOPPED 状态测试
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    ("STOPPED", 5, "RESET", "IDLE", 0, "RESET"),
    ("STOPPED", 5, "INCREMENT", "STOPPED", 5, "NO_CHANGE"),
    
    # COMPLETED 状态测试
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 10, "START", "COMPLETED", 10, "NO_CHANGE"),
    
    # 无效动作测试
    ("IDLE", 0, "INVALID", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 5, "INVALID", "RUNNING", 5, "NO_CHANGE"),
    
    # 边界条件测试
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 0, "INCREMENT", "RUNNING", 1, "INCREMENTED"),
    ("RUNNING", 8, "INCREMENT", "RUNNING", 9, "INCREMENTED"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    
    # 无效状态测试
    ("UNKNOWN", 0, "START", "UNKNOWN", 0, "NO_CHANGE"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result