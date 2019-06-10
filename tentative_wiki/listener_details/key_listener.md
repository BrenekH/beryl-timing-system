# Key Listener
A key listener is a listener that is triggered when a pygame key down event is generated.

To register your custom key listener, you must use the `EventManager.register_key_listener(key, function)` function in the register_listeners function.

The key must be a pygame key value or equivalent integer. ex. `pygame.K_a`

__Extended Example__

```python
import pygame

class Plugin:
	def __init__(self, parent):
		self.parent = parent
		...

	def my_listener(self):
		print("Hello, World!")

	def register_listeners(self):
		self.parent.register_key_listener(pygame.K_SPACE, self.my_listener)
```
