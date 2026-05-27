# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: not (state == 'STOPPED')
# 重复次数: 3, 迭代: 9
# 生成时间: 2026-04-18 16:56:48

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 有效输入测试
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("IDLE", 5, "RESET", "IDLE", 5, "RESET"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    ("STOPPED", 5, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    
    # 类型错误测试
    (123, 0, "START", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", "test", "START", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", 0, 123, "IDLE", 0, "NO_CHANGE"),
    
    # 边界条件测试
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 0, "INCREMENT", "RUNNING", 1, "INCREMENTED"),
    
    # 无效动作测试
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 0, "RESET", "RUNNING", 0, "NO_CHANGE"),
    ("STOPPED", 0, "INCREMENT", "STOPPED", 0, "NO_CHANGE"),
    ("COMPLETED", 0, "START", "COMPLETED", 0, "NO_CHANGE"),
    
    # 状态转换逻辑验证
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    ("STOPPED", 0, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 0, "RESET", "IDLE", 0, "RESET"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result