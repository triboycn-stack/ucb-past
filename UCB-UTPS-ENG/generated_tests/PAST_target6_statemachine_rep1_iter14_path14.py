# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: action == 'RESET'
# 重复次数: 1, 迭代: 14
# 生成时间: 2026-04-26 06:36:43

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 RESET 在 IDLE 状态下
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    # 测试 RESET 在 RUNNING 状态下（无效）
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    # 测试 RESET 在 STOPPED 状态下
    ("STOPPED", 3, "RESET", "IDLE", 0, "RESET"),
    # 测试 RESET 在 COMPLETED 状态下
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    # 测试 RESET 在无效状态（如 UNKNOWN）
    ("UNKNOWN", 0, "RESET", "UNKNOWN", 0, "NO_CHANGE"),
    # 测试类型错误（state 不是字符串）
    (123, 0, "RESET", 123, 0, "NO_CHANGE"),
    # 测试类型错误（counter 不是整数）
    ("IDLE", "test", "RESET", "IDLE", "test", "NO_CHANGE"),
    # 测试类型错误（action 不是字符串）
    ("IDLE", 0, 123, "IDLE", 0, "NO_CHANGE"),
    # 测试 RESET 在 RUNNING 状态下，但 counter 已达 10
    ("RUNNING", 10, "RESET", "RUNNING", 10, "NO_CHANGE"),
])
def test_transition_reset(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result