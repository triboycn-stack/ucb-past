# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: action == 'STOP'
# 重复次数: 3, 迭代: 10
# 生成时间: 2026-04-18 16:56:55

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 state == "RUNNING" 且 action == "STOP"
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    # 测试 state == "RUNNING" 且 action == "STOP" 但 counter >= 10
    ("RUNNING", 10, "STOP", "RUNNING", 10, "NO_CHANGE"),
    # 测试无效状态
    ("UNKNOWN", 5, "STOP", "UNKNOWN", 5, "NO_CHANGE"),
    # 测试无效动作
    ("RUNNING", 5, "INVALID", "RUNNING", 5, "NO_CHANGE"),
    # 测试类型错误
    (123, "test", "STOP", 123, "test", "NO_CHANGE"),
    ("RUNNING", "test", "STOP", "RUNNING", "test", "NO_CHANGE"),
    ("RUNNING", 5, 123, "RUNNING", 5, "NO_CHANGE"),
    # 测试边界条件：counter == 9，执行 STOP
    ("RUNNING", 9, "STOP", "STOPPED", 9, "STOPPED"),
    # 测试边界条件：counter == 10，执行 STOP
    ("RUNNING", 10, "STOP", "RUNNING", 10, "NO_CHANGE"),
    # 测试其他状态下的 STOP 动作
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),
    ("STOPPED", 0, "STOP", "STOPPED", 0, "NO_CHANGE"),
    ("COMPLETED", 10, "STOP", "COMPLETED", 10, "NO_CHANGE"),
])
def test_transition_with_stop_action(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result