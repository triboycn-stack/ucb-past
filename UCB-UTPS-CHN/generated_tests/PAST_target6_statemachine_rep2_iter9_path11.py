# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: state != 'RUNNING'
# 重复次数: 2, 迭代: 9
# 生成时间: 2026-04-18 16:54:44

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试状态转换核心逻辑：state != 'RUNNING'
    # IDLE 状态
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", 0, "INCREMENT", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", 0, "RESUME", "IDLE", 0, "NO_CHANGE"),
    
    # STOPPED 状态
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    ("STOPPED", 5, "RESET", "IDLE", 0, "RESET"),
    ("STOPPED", 5, "START", "STOPPED", 5, "NO_CHANGE"),
    ("STOPPED", 5, "INCREMENT", "STOPPED", 5, "NO_CHANGE"),
    ("STOPPED", 5, "STOP", "STOPPED", 5, "NO_CHANGE"),
    
    # COMPLETED 状态
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 10, "START", "COMPLETED", 10, "NO_CHANGE"),
    ("COMPLETED", 10, "INCREMENT", "COMPLETED", 10, "NO_CHANGE"),
    ("COMPLETED", 10, "STOP", "COMPLETED", 10, "NO_CHANGE"),
    ("COMPLETED", 10, "RESUME", "COMPLETED", 10, "NO_CHANGE"),
    
    # 类型错误处理
    (123, 0, "START", 123, 0, "NO_CHANGE"),
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    ("IDLE", 0, 123, "IDLE", 0, "NO_CHANGE"),
    (None, None, None, None, None, "NO_CHANGE"),
    
    # 边界条件测试
    ("RUNNING", 9, "INCREMENT", "RUNNING", 10, "INCREMENTED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 9, "STOP", "STOPPED", 9, "STOPPED"),
    ("RUNNING", 9, "RESET", "RUNNING", 9, "NO_CHANGE"),
    
    # 非法动作
    ("IDLE", 0, "INVALID", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 0, "INVALID", "RUNNING", 0, "NO_CHANGE"),
    ("STOPPED", 0, "INVALID", "STOPPED", 0, "NO_CHANGE"),
    ("COMPLETED", 0, "INVALID", "COMPLETED", 0, "NO_CHANGE"),
])
def test_transition_core_logic(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result