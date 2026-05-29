# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: not (state == 'COMPLETED')
# 重复次数: 3, 迭代: 4
# 生成时间: 2026-04-26 06:39:43

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试类型错误情况
    (123, "test", "START", 123, "test", "NO_CHANGE"),
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    ("IDLE", 5, 123, "IDLE", 5, "NO_CHANGE"),
    
    # IDLE 状态测试
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),
    
    # RUNNING 状态测试
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    ("RUNNING", 5, "RESUME", "RUNNING", 5, "NO_CHANGE"),
    
    # STOPPED 状态测试
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    ("STOPPED", 5, "RESET", "IDLE", 0, "RESET"),
    ("STOPPED", 5, "START", "STOPPED", 5, "NO_CHANGE"),
    
    # COMPLETED 状态测试
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 10, "INCREMENT", "COMPLETED", 10, "NO_CHANGE"),
    ("COMPLETED", 10, "STOP", "COMPLETED", 10, "NO_CHANGE"),
    
    # 无效动作测试
    ("IDLE", 0, "INVALID", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 5, "INVALID", "RUNNING", 5, "NO_CHANGE"),
    ("STOPPED", 5, "INVALID", "STOPPED", 5, "NO_CHANGE"),
    ("COMPLETED", 10, "INVALID", "COMPLETED", 10, "NO_CHANGE"),
    
    # 边界条件测试
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 0, "INCREMENT", "RUNNING", 1, "INCREMENTED"),
    ("RUNNING", 8, "INCREMENT", "RUNNING", 9, "INCREMENTED"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    
    # 状态转换有效性测试（不直接调用 validate_transition，但通过 transition 的返回值验证）
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("RUNNING", 0, "STOP", "STOPPED", 0, "STOPPED"),
    ("STOPPED", 0, "RESUME", "RUNNING", 0, "RESUMED"),
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result