from colorama import Fore
from importlib import import_module
from inspect import getmembers, isclass, isfunction
from typing import List

class Event:
	key = "key"
	loop = "loop"
	period_change = "period change"
	config_change = "config change"

	_all_events = [key, loop, period_change, config_change]

class PluginManager:
	def __init__(self, parent_class):
		self.parent_class = parent_class

		self.__plugins = {}
		self.__plugin_event_registry = {}

		# API Requirements
		self.plugin_requirements = {"display": False}

		# Not Easily Accessible Vars
		self.__cross_plugin_data = {}

	def load_plugins(self, plugins: List[str]):
		"""Loads plugins to be used by the plugin manager

		Arguments:
			plugins {List[str]} -- List of plugins to load
		"""

		requested_requirements = []

		for plugin in plugins:
			# Import the plugin's module
			plugin_module = import_module(plugin)

			# Find all classes in the plugin's module
			all_module_classes = [m[1] for m in getmembers(plugin_module, isclass) if m[1].__module__ == plugin_module.__name__]

			# Find all classes marked with the Class._is_beryl_plugin variable set to True
			beryl_plugin_classes = []
			for module_class in all_module_classes:
				try:
					if not module_class._is_beryl_plugin:
						continue
				except AttributeError:
					continue

				beryl_plugin_classes.append(module_class)

			# Sanity checks
			if len(beryl_plugin_classes) == 0:
				print(f"{Fore.YELLOW}[WARNING] Could not find an Beryl Plugin class in {plugin}. Maybe it is missing the @beryl_plugin decoration?{Fore.RESET}")
			elif len(beryl_plugin_classes) > 1:
				print(f"{Fore.YELLOW}[WARNING] {plugin} provided more than one Beryl Plugin class. The recommended limit is one per module.{Fore.RESET}")

			for plugin_class in beryl_plugin_classes:
				plugin_instance = plugin_class(self)
				plugin_id = plugin_instance.ID

				# Store an instance of the plugin
				self.__plugins[plugin_id] = {"instance": plugin_instance}

				# Discovers and adds the handlers
				for _, func in getmembers(plugin_class, isfunction):
					try:
						if not func._is_beryl_handler:
							continue
					except AttributeError:
						continue

					# Sort into different types
					try:
						# Check if valid event type
						if func._beryl_event not in Event._all_events:
							print(f"{Fore.RED}[ERROR] Function '{func.__name__}' of '{plugin_id}' has invalid event type '{func._beryl_event}'{Fore.RESET}'")

						self.__add_handler_safely(plugin_id, func)

						if func._beryl_event not in self.__plugin_event_registry:
							self.__plugin_event_registry[func._beryl_event] = []

						if not plugin_id in self.__plugin_event_registry[func._beryl_event]:
							self.__plugin_event_registry[func._beryl_event].append(plugin_id)

					except AttributeError:
						print(f"{Fore.RED}[ERROR] '{func.__name__}' of '{plugin_id}' was marked as an Beryl event handler but did not specify the event to handle!{Fore.RESET}")

		# Mark the needed API Requirements
		if "display" in requested_requirements:
			self.plugin_requirements["display"] = True

		print(f"{len(self.__plugins)} plugins loaded")
		return self

	def __add_handler_safely(self, plugin_id, func):
		try:
			self.__plugins[plugin_id][func._beryl_event]
		except KeyError:
			self.__plugins[plugin_id][func._beryl_event] = []

		plugin_event_list = self.__plugins[plugin_id][func._beryl_event]
		if func._beryl_event == Event.key:
			plugin_event_list.append({"func": func, "keys": func._keys})
		else:
			plugin_event_list.append({"func": func})

	def trigger_event(self, event_type, *args):
		"""Triggers all handlers associated to the passed event type

		Arguments:
			event_type -- The event type to trigger

		Returns:
			bool -- True when at least one event handler was called
		"""
		event_triggered = False
		try:
			self.__plugin_event_registry[event_type]
		except KeyError:
			return event_triggered

		for ID in self.__plugin_event_registry[event_type]:
			for handler_obj in self.__plugins[ID][event_type]:
				if event_type == Event.key:
					if "*" in handler_obj["keys"] or args[0] in handler_obj["keys"]:
						handler_obj["func"](self.__plugins[ID]["instance"], *args)
						event_triggered = True
				else:
					handler_obj["func"](self.__plugins[ID]["instance"], *args)
					event_triggered = True

		return event_triggered

	def need_game_display(self):
		return self.plugin_requirements["display"]

	def get_plugin_display(self):
		if self.parent_class.do_game_display:
			return self.parent_class.plugin_display
		else:
			raise ValueError("No plugins specified the need for the plugin display. Yet one tried to access it.")

	# Configs API
	def get_current_config(self, child_class):
		# TODO: Implement
		return "This feature is not yet implemented", self

	def get_current_family_config(self, child_class):
		# TODO: Implement
		return "This feature is not yet implemented", self
