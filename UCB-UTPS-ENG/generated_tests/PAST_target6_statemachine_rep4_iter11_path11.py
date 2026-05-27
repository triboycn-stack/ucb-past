# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: state != 'RUNNING'
# 重复次数: 4, 迭代: 11
# 生成时间: 2026-04-26 06:42:55

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试状态为 IDLE 且动作是 START
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    # 测试状态为 IDLE 且动作是 RESET
    ("IDLE", 5, "RESET", "IDLE", 5, "RESET"),
    # 测试状态为 RUNNING 且动作是 RESET（应返回 NO_CHANGE）
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    # 测试状态为 RUNNING 且动作是 STOP
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    # 测试状态为 RUNNING 且动作是 INCREMENT，计数器 < 10
    ("RUNNING", 5, "INCREMENT", "RUNNING", 6, "INCREMENTED"),
    # 测试状态为 RUNNING 且动作是 INCREMENT，计数器 == 9
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    # 测试状态为 RUNNING 且动作是 INCREMENT，计数器 >= 10
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # 测试状态为 STOPPED 且动作是 RESUME
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    # 测试状态为 STOPPED 且动作是 RESET
    ("STOPPED", 5, "RESET", "IDLE", 0, "RESET"),
    # 测试状态为 COMPLETED 且动作是 RESET
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    # 测试无效动作
    ("IDLE", 0, "INVALID", "IDLE", 0, "NO_CHANGE"),
    # 测试类型错误（state 不是字符串）
    (123, 0, "START", 123, 0, "NO_CHANGE"),
    # 测试类型错误（counter 不是整数）
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    # 测试类型错误（action 不是字符串）
    ("IDLE", 0, 123, "IDLE", 0, "NO_CHANGE"),
    # 测试 state != 'RUNNING' 的条件分支（如 IDLE 状态下执行 INCREMENT）
    ("IDLE", 5, "INCREMENT", "IDLE", 5, "NO_CHANGE"),
    # 测试 state != 'RUNNING' 的条件分支（如 STOPPED 状态下执行 INCREMENT）
    ("STOPPED", 5, "INCREMENT", "STOPPED", 5, "NO_CHANGE"),
    # 测试 state != 'RUNNING' 的条件分支（如 COMPLETED 状态下执行 INCREMENT）
    ("COMPLETED", 5, "INCREMENT", "COMPLETED", 5, "NO_CHANGE"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result