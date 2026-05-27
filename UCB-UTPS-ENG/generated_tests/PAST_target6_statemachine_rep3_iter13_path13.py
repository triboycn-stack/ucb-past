# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: state == 'STOPPED'
# 重复次数: 3, 迭代: 13
# 生成时间: 2026-04-26 06:41:02

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 state == "STOPPED" 的情况
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    ("STOPPED", 5, "RESET", "IDLE", 0, "RESET"),
    ("STOPPED", 5, "START", "STOPPED", 5, "NO_CHANGE"),
    ("STOPPED", 5, "INCREMENT", "STOPPED", 5, "NO_CHANGE"),
    ("STOPPED", 5, "STOP", "STOPPED", 5, "NO_CHANGE"),
    # 边界条件测试
    ("STOPPED", 10, "RESUME", "STOPPED", 10, "NO_CHANGE"),
    ("STOPPED", 9, "RESUME", "RUNNING", 9, "RESUMED"),
    # 非法输入测试
    (123, 5, "RESUME", 123, 5, "NO_CHANGE"),
    ("STOPPED", "test", "RESUME", "STOPPED", "test", "NO_CHANGE"),
    ("STOPPED", 5, 123, "STOPPED", 5, "NO_CHANGE"),
])
def test_transition_state_STOPPED(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result