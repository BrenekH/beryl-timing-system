import sys
import beryl_timing_system
import beryl_plugin

def test_beryl_timing_system_imported():
	assert "beryl_timing_system" in sys.modules

def test_beryl_plugin_imported():
	assert "beryl_plugin" in sys.modules