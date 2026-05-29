# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: not (not isinstance(state, str) or not isinstance(counter, int) or (not isinstance(action, str)))
# 重复次数: 0, 迭代: 3
# 生成时间: 2026-04-18 16:49:34

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 有效输入测试
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("RUNNING", 5, "INCREMENT", "RUNNING", 6, "INCREMENTED"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    ("STOPPED", 0, "RESET", "IDLE", 0, "RESET"),
    
    # 无效动作测试
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 0, "RESET", "RUNNING", 0, "NO_CHANGE"),
    ("STOPPED", 0, "STOP", "STOPPED", 0, "NO_CHANGE"),
    ("COMPLETED", 0, "START", "COMPLETED", 0, "NO_CHANGE"),
    
    # 边界条件测试
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 0, "STOP", "STOPPED", 0, "STOPPED"),
    
    # 类型错误测试
    (123, 0, "START", 123, 0, "NO_CHANGE"),
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    ("IDLE", 0, 123, "IDLE", 0, "NO_CHANGE"),
    (None, 0, "START", None, 0, "NO_CHANGE"),
    ("IDLE", None, "START", "IDLE", None, "NO_CHANGE"),
    ("IDLE", 0, None, "IDLE", 0, "NO_CHANGE"),
    
    # 状态转换验证测试
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("RUNNING", 0, "STOP", "STOPPED", 0, "STOPPED"),
    ("STOPPED", 0, "RESUME", "RUNNING", 0, "RESUMED"),
    ("COMPLETED", 0, "RESET", "IDLE", 0, "RESET"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result