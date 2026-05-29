# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: state == 'COMPLETED'
# 重复次数: 2, 迭代: 14
# 生成时间: 2026-04-18 16:55:25

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 state == 'COMPLETED' 的情况
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 5, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 10, "START", "COMPLETED", 10, "NO_CHANGE"),
    ("COMPLETED", 5, "STOP", "COMPLETED", 5, "NO_CHANGE"),
    ("COMPLETED", 10, "INCREMENT", "COMPLETED", 10, "NO_CHANGE"),
    ("COMPLETED", 5, "RESUME", "COMPLETED", 5, "NO_CHANGE"),
    # 类型错误测试
    (123, "test", "RESET", 123, "test", "NO_CHANGE"),
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    ("IDLE", 10, 123, "IDLE", 10, "NO_CHANGE"),
    # 状态转换验证
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    ("STOPPED", 5, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    # 无效动作
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 0, "RESET", "RUNNING", 0, "NO_CHANGE"),
    ("STOPPED", 5, "INCREMENT", "STOPPED", 5, "NO_CHANGE"),
    ("COMPLETED", 10, "START", "COMPLETED", 10, "NO_CHANGE"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result