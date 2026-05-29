# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: counter == 9
# 重复次数: 2, 迭代: 10
# 生成时间: 2026-04-18 16:54:55

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试条件路径: counter == 9
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    # 边界条件测试
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # 类型错误处理
    (123, "test", "START", 123, "test", "NO_CHANGE"),
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    ("IDLE", 5, 123, "IDLE", 5, "NO_CHANGE"),
    # 状态转换有效性测试
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("RUNNING", 0, "STOP", "STOPPED", 0, "STOPPED"),
    ("STOPPED", 0, "RESUME", "RUNNING", 0, "RESUMED"),
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    # 无效动作
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 0, "RESET", "RUNNING", 0, "NO_CHANGE"),
    ("STOPPED", 0, "STOP", "STOPPED", 0, "NO_CHANGE"),
    ("COMPLETED", 0, "START", "COMPLETED", 0, "NO_CHANGE"),
    # 计数器最大值测试
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # RESET 在 RUNNING 状态下无效
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    # 状态机初始状态
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    # 多次操作测试
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("RUNNING", 0, "INCREMENT", "RUNNING", 1, "INCREMENTED"),
    ("RUNNING", 8, "INCREMENT", "RUNNING", 9, "INCREMENTED"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_message = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_message == expected_result