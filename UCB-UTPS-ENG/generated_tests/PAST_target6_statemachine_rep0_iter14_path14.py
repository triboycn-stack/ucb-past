# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: action == 'RESET'
# 重复次数: 0, 迭代: 14
# 生成时间: 2026-04-26 06:34:39

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 RESET 在 IDLE 状态下有效
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    # 测试 RESET 在 RUNNING 状态下无效
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    # 测试 RESET 在 STOPPED 状态下有效
    ("STOPPED", 3, "RESET", "IDLE", 0, "RESET"),
    # 测试 RESET 在 COMPLETED 状态下有效
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    # 测试 RESET 在无效状态（如 INVALID）下无效
    ("INVALID", 5, "RESET", "INVALID", 5, "NO_CHANGE"),
    # 测试类型错误时返回 NO_CHANGE
    (123, "test", "RESET", 123, "test", "NO_CHANGE"),
    # 测试非字符串状态时返回 NO_CHANGE
    (123, 5, "RESET", 123, 5, "NO_CHANGE"),
    # 测试非字符串动作时返回 NO_CHANGE
    ("IDLE", 5, 123, "IDLE", 5, "NO_CHANGE"),
])
def test_transition_reset(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_message = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_message == expected_result