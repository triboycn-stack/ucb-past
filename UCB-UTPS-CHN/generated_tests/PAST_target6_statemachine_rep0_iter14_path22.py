# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: not (state == 'IDLE')
# 重复次数: 0, 迭代: 14
# 生成时间: 2026-04-18 16:51:04

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试条件: not (state == 'IDLE') → 状态不是 IDLE 的情况
    # RUNNING 状态下执行 RESET
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    # RUNNING 状态下执行 STOP
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    # RUNNING 状态下执行 INCREMENT（counter < 10）
    ("RUNNING", 5, "INCREMENT", "RUNNING", 6, "INCREMENTED"),
    # RUNNING 状态下执行 INCREMENT（counter == 9）
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    # RUNNING 状态下执行 INCREMENT（counter == 10）
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # STOPPED 状态下执行 RESUME
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    # STOPPED 状态下执行 RESET
    ("STOPPED", 5, "RESET", "IDLE", 0, "RESET"),
    # COMPLETED 状态下执行 RESET
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    # 无效动作
    ("RUNNING", 5, "INVALID", "RUNNING", 5, "NO_CHANGE"),
    # 类型错误：state 不是字符串
    (123, 5, "START", 123, 5, "NO_CHANGE"),
    # 类型错误：counter 不是整数
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    # 类型错误：action 不是字符串
    ("IDLE", 5, 123, "IDLE", 5, "NO_CHANGE"),
])
def test_transition_core_logic(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result