# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: state != 'RUNNING'
# 重复次数: 3, 迭代: 12
# 生成时间: 2026-04-18 16:57:11

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 状态不是 RUNNING 的情况
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    ("STOPPED", 0, "RESET", "IDLE", 0, "RESET"),
    
    # 类型错误情况
    (123, "test", "START", 123, "test", "NO_CHANGE"),
    ("RUNNING", "test", "INCREMENT", "RUNNING", "test", "NO_CHANGE"),
    ("RUNNING", 5, 123, "RUNNING", 5, "NO_CHANGE"),
    
    # RUNNING 状态下 RESET 不生效
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    ("RUNNING", 10, "RESET", "RUNNING", 10, "NO_CHANGE"),
    
    # INCREMENT 达到 10 后不生效
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    
    # 无效动作
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 0, "RESUME", "RUNNING", 0, "NO_CHANGE"),
    ("STOPPED", 0, "START", "STOPPED", 0, "NO_CHANGE"),
    ("COMPLETED", 0, "INCREMENT", "COMPLETED", 0, "NO_CHANGE"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result