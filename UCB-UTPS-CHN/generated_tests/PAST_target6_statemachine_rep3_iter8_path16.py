# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: new_counter == 10
# 重复次数: 3, 迭代: 8
# 生成时间: 2026-04-18 16:56:41

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 new_counter == 10 的情况
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    # 测试类型错误
    ("RUNNING", "invalid", "INCREMENT", "RUNNING", "invalid", "NO_CHANGE"),
    ("RUNNING", 5, 123, "RUNNING", 5, "NO_CHANGE"),
    # 测试 RUNNING 状态下 RESET 不生效
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    # 测试 counter 达到 10 后 INCREMENT 不生效
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # 测试 IDLE 状态下 START 成功
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    # 测试 IDLE 状态下 RESET 成功
    ("IDLE", 5, "RESET", "IDLE", 5, "RESET"),
    # 测试 RUNNING 状态下 STOP 成功
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    # 测试 RUNNING 状态下 INCREMENT 成功（未达到 10）
    ("RUNNING", 5, "INCREMENT", "RUNNING", 6, "INCREMENTED"),
    # 测试 STOPPED 状态下 RESUME 成功
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    # 测试 STOPPED 状态下 RESET 成功
    ("STOPPED", 5, "RESET", "IDLE", 0, "RESET"),
    # 测试 COMPLETED 状态下 RESET 成功
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    # 测试无效动作
    ("IDLE", 0, "INVALID", "IDLE", 0, "NO_CHANGE"),
    # 测试边界条件：counter = 9，INCREMENT 后变为 10 并进入 COMPLETED
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    # 测试边界条件：counter = 10，INCREMENT 不生效
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # 测试空输入
    ("", 0, "", "", 0, "NO_CHANGE"),
    # 测试非法状态
    ("UNKNOWN", 0, "START", "UNKNOWN", 0, "NO_CHANGE"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result