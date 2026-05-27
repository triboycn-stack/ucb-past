# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: not (action == 'INCREMENT')
# 重复次数: 4, 迭代: 3
# 生成时间: 2026-04-26 06:41:48

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 IDLE 状态下的 START 动作
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    # 测试 IDLE 状态下的 RESET 动作
    ("IDLE", 5, "RESET", "IDLE", 5, "RESET"),
    # 测试 RUNNING 状态下的 STOP 动作
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    # 测试 RUNNING 状态下的 INCREMENT 动作（counter < 10）
    ("RUNNING", 5, "INCREMENT", "RUNNING", 6, "INCREMENTED"),
    # 测试 RUNNING 状态下的 INCREMENT 动作（counter == 9）
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    # 测试 RUNNING 状态下的 INCREMENT 动作（counter >= 10）
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # 测试 RUNNING 状态下的 RESET 动作（不生效）
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    # 测试 STOPPED 状态下的 RESUME 动作
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    # 测试 STOPPED 状态下的 RESET 动作
    ("STOPPED", 5, "RESET", "IDLE", 0, "RESET"),
    # 测试 COMPLETED 状态下的 RESET 动作
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    # 测试无效动作（不在有效动作列表中）
    ("IDLE", 0, "INVALID", "IDLE", 0, "NO_CHANGE"),
    # 测试类型错误（state 不是字符串）
    (123, 0, "START", 123, 0, "NO_CHANGE"),
    # 测试类型错误（counter 不是整数）
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    # 测试类型错误（action 不是字符串）
    ("IDLE", 0, 123, "IDLE", 0, "NO_CHANGE"),
    # 测试边界条件：counter == 9，INCREMENT 后变为 COMPLETED
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    # 测试边界条件：counter == 10，INCREMENT 不生效
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # 测试空动作序列（无动作）
    ("IDLE", 0, "", "IDLE", 0, "NO_CHANGE"),
    # 测试多个动作序列
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("RUNNING", 0, "INCREMENT", "RUNNING", 1, "INCREMENTED"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result == expected_result