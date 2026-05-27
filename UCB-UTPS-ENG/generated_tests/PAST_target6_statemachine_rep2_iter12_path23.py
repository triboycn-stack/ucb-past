# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: state == 'IDLE'
# 重复次数: 2, 迭代: 12
# 生成时间: 2026-04-18 16:55:09

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 state == 'IDLE' 的情况
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("IDLE", 5, "RESET", "IDLE", 5, "RESET"),
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", 0, "INCREMENT", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", 0, "RESUME", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", 0, "COMPLETED", "IDLE", 0, "NO_CHANGE"),
    # 类型错误测试
    (123, 0, "START", 123, 0, "NO_CHANGE"),
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    ("IDLE", 0, 123, "IDLE", 0, "NO_CHANGE"),
    # 状态转换无效动作
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", 0, "INCREMENT", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", 0, "RESUME", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", 0, "COMPLETED", "IDLE", 0, "NO_CHANGE"),
])
def test_transition_state_idle(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result