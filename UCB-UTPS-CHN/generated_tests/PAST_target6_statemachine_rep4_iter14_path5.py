# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: state == 'COMPLETED'
# 重复次数: 4, 迭代: 14
# 生成时间: 2026-04-18 16:59:37

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 state == 'COMPLETED' 的情况
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 5, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 10, "START", "COMPLETED", 10, "NO_CHANGE"),
    ("COMPLETED", 5, "STOP", "COMPLETED", 5, "NO_CHANGE"),
    ("COMPLETED", 10, "INCREMENT", "COMPLETED", 10, "NO_CHANGE"),
    ("COMPLETED", 5, "INCREMENT", "COMPLETED", 5, "NO_CHANGE"),
    ("COMPLETED", 10, "RESUME", "COMPLETED", 10, "NO_CHANGE"),
    ("COMPLETED", 5, "RESUME", "COMPLETED", 5, "NO_CHANGE"),
    # 边界条件测试
    ("COMPLETED", 9, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    # 非法输入测试
    (123, 10, "RESET", "COMPLETED", 10, "NO_CHANGE"),
    ("COMPLETED", "test", "RESET", "COMPLETED", 10, "NO_CHANGE"),
    ("COMPLETED", 10, 123, "COMPLETED", 10, "NO_CHANGE"),
])
def test_transition_state_completed(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_message = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_message == expected_result