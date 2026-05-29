# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: not (new_counter == 10)
# 重复次数: 2, 迭代: 6
# 生成时间: 2026-04-18 16:54:14

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试类型错误情况
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    (123, 5, "START", "123", 5, "NO_CHANGE"),
    ("IDLE", 5, 123, "IDLE", 5, "NO_CHANGE"),

    # 测试 IDLE 状态
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),

    # 测试 RUNNING 状态
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 9, "STOP", "STOPPED", 9, "STOPPED"),
    ("RUNNING", 9, "RESET", "RUNNING", 9, "NO_CHANGE"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 5, "INCREMENT", "RUNNING", 6, "INCREMENTED"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 0, "STOP", "STOPPED", 0, "STOPPED"),
    ("RUNNING", 0, "RESET", "RUNNING", 0, "NO_CHANGE"),

    # 测试 STOPPED 状态
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    ("STOPPED", 5, "RESET", "IDLE", 0, "RESET"),
    ("STOPPED", 5, "START", "STOPPED", 5, "NO_CHANGE"),

    # 测试 COMPLETED 状态
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 10, "START", "COMPLETED", 10, "NO_CHANGE"),
    ("COMPLETED", 10, "STOP", "COMPLETED", 10, "NO_CHANGE"),

    # 测试无效动作
    ("IDLE", 0, "RESUME", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 0, "RESUME", "RUNNING", 0, "NO_CHANGE"),
    ("STOPPED", 0, "INCREMENT", "STOPPED", 0, "NO_CHANGE"),
    ("COMPLETED", 0, "INCREMENT", "COMPLETED", 0, "NO_CHANGE"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result