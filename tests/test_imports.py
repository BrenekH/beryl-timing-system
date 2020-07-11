import sys
import beryl_timing_system

def test_beryl_timing_system_imported():
	print(beryl_timing_system.version)
	assert "beryl_timing_system" in sys.modules
