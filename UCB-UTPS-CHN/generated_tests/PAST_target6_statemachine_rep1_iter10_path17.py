# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: not (action == 'RESET')
# 重复次数: 1, 迭代: 10
# 生成时间: 2026-04-18 16:52:36

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 有效状态转换
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("RUNNING", 0, "INCREMENT", "RUNNING", 1, "INCREMENTED"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    
    # 无效动作
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 0, "RESET", "RUNNING", 0, "NO_CHANGE"),
    ("STOPPED", 0, "STOP", "STOPPED", 0, "NO_CHANGE"),
    
    # 边界条件
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 8, "INCREMENT", "RUNNING", 9, "INCREMENTED"),
    
    # 类型错误
    (123, 0, "START", 123, 0, "NO_CHANGE"),
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    ("IDLE", 0, 123, "IDLE", 0, "NO_CHANGE"),
    
    # RESET 在 RUNNING 状态下无效
    ("RUNNING", 0, "RESET", "RUNNING", 0, "NO_CHANGE"),
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    
    # 无效状态
    ("UNKNOWN", 0, "START", "UNKNOWN", 0, "NO_CHANGE"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result