# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: state == 'RUNNING'
# 重复次数: 2, 迭代: 11
# 生成时间: 2026-04-18 16:55:02

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 RUNNING 状态下 RESET 不生效
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    # 测试 RUNNING 状态下 STOP 转换
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    # 测试 RUNNING 状态下 INCREMENT 未达10
    ("RUNNING", 5, "INCREMENT", "RUNNING", 6, "INCREMENTED"),
    # 测试 RUNNING 状态下 INCREMENT 达到10
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    # 测试 RUNNING 状态下 INCREMENT 已达10
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # 测试类型错误（state 不是字符串）
    (123, 5, "START", 123, 5, "NO_CHANGE"),
    # 测试类型错误（counter 不是整数）
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    # 测试类型错误（action 不是字符串）
    ("IDLE", 5, 123, "IDLE", 5, "NO_CHANGE"),
    # 测试无效动作
    ("RUNNING", 5, "INVALID", "RUNNING", 5, "NO_CHANGE"),
    # 测试状态转换边界情况（counter=9）
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    # 测试状态转换边界情况（counter=10）
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
])
def test_transition_core_logic(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_message = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_message == expected_result