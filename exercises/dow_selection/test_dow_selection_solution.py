""" Perform test for execution and simple output sanity check
"""

def test_script(run_script):
    assert run_script(__file__, timeout=2)
