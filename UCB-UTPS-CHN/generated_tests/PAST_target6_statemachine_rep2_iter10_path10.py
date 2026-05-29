# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: not (state == 'STOPPED')
# 重复次数: 2, 迭代: 10
# 生成时间: 2026-04-26 06:38:27

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试类型错误情况
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    (123, 0, "START", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", 0, 123, "IDLE", 0, "NO_CHANGE"),
    
    # IDLE 状态测试
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),
    
    # RUNNING 状态测试
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 9, "STOP", "STOPPED", 9, "STOPPED"),
    ("RUNNING", 9, "RESET", "RUNNING", 9, "NO_CHANGE"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 5, "INCREMENT", "RUNNING", 6, "INCREMENTED"),
    
    # STOPPED 状态测试
    ("STOPPED", 0, "RESUME", "RUNNING", 0, "RESUMED"),
    ("STOPPED", 0, "RESET", "IDLE", 0, "RESET"),
    ("STOPPED", 0, "START", "STOPPED", 0, "NO_CHANGE"),
    
    # COMPLETED 状态测试
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 10, "STOP", "COMPLETED", 10, "NO_CHANGE"),
    
    # 无效动作测试
    ("IDLE", 0, "INVALID", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 0, "INVALID", "RUNNING", 0, "NO_CHANGE"),
    
    # 边界条件测试
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 0, "INCREMENT", "RUNNING", 1, "INCREMENTED"),
    
    # 非法输入测试
    (None, 0, "START", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", None, "START", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", 0, None, "IDLE", 0, "NO_CHANGE"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result