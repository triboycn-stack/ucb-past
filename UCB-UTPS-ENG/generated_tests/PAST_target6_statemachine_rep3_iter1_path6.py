# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: action == 'RESUME'
# 重复次数: 3, 迭代: 1
# 生成时间: 2026-04-18 16:55:43

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 RESUME 动作在 STOPPED 状态下有效
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    # 测试 RESUME 动作在非 STOPPED 状态下无效
    ("IDLE", 0, "RESUME", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 5, "RESUME", "RUNNING", 5, "NO_CHANGE"),
    ("COMPLETED", 10, "RESUME", "COMPLETED", 10, "NO_CHANGE"),
    # 测试类型错误情况
    (123, "test", "RESET", 123, "test", "NO_CHANGE"),
    ("IDLE", 10.5, "START", "IDLE", 10.5, "NO_CHANGE"),
    ("RUNNING", 10, 123, "RUNNING", 10, "NO_CHANGE"),
    # 测试边界条件：counter == 9 时 INCREMENT
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    # 测试 counter == 10 时 INCREMENT
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # 测试 RUNNING 状态下 RESET 不生效
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    # 测试 IDLE 状态下 START 成功
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    # 测试 IDLE 状态下 RESET 成功
    ("IDLE", 5, "RESET", "IDLE", 5, "RESET"),
    # 测试 STOPPED 状态下 RESET 成功
    ("STOPPED", 5, "RESET", "IDLE", 0, "RESET"),
    # 测试 COMPLETED 状态下 RESET 成功
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    # 测试无效动作
    ("IDLE", 0, "INVALID", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 5, "INVALID", "RUNNING", 5, "NO_CHANGE"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result