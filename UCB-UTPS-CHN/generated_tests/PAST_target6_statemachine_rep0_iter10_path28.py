# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: counter < 9
# 重复次数: 0, 迭代: 10
# 生成时间: 2026-04-18 16:50:32

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试条件: counter < 9
    ("RUNNING", 8, "INCREMENT", "RUNNING", 9, "INCREMENTED"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # 类型错误情况
    (123, "test", "START", 123, "test", "NO_CHANGE"),
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    ("IDLE", 5, 123, "IDLE", 5, "NO_CHANGE"),
    # 状态转换测试
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    ("RUNNING", 0, "STOP", "STOPPED", 0, "STOPPED"),
    ("RUNNING", 0, "RESET", "RUNNING", 0, "NO_CHANGE"),
    ("STOPPED", 0, "RESUME", "RUNNING", 0, "RESUMED"),
    ("STOPPED", 0, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    # 无效动作
    ("IDLE", 0, "INVALID", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 0, "INVALID", "RUNNING", 0, "NO_CHANGE"),
    ("STOPPED", 0, "INVALID", "STOPPED", 0, "NO_CHANGE"),
    ("COMPLETED", 0, "INVALID", "COMPLETED", 0, "NO_CHANGE"),
    # 边界条件
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
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