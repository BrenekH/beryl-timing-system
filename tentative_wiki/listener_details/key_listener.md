# Key Listener
A key listener is a listener that is triggered when a pygame key down event is generated.

To register your custom key listener, you must use the `self.register_key_listener(key, function)` function in the register_listeners function.

The key must be a pygame key value or equivalent integer. ex. `pygame.K_a`

To get every key, give an asterisk \(*\) to the handler.

__Extended Example__

```python
import pygame
from beryl_plugin import PluginBase

class Plugin(PluginBase):
	def __init__(self, parent):
		PluginBase.__init__(self, parent, "Name", "example.example1", "example")
		self.parent = parent
		...

	def my_listener(self):
		print("Hello, World!")

	def register_listeners(self):
		self.register_key_listener(pygame.K_SPACE, self.my_listener)
```
