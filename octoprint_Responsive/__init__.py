# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class ResponsivePlugin(octoprint.plugin.AssetPlugin):

	def get_assets(self):
		return dict(
			css=["css/Responsive.css"],
		)

	def get_update_information(self):
		return dict(
			Responsive=dict(
				displayName="OctoPrint-Responsive",
				displayVersion=self._plugin_version,

				type="github_release",
				user="tjjfvi",
				repo="OctoPrint-Responsive",
				current=self._plugin_version,

				pip="https://github.com/tjjfvi/OctoPrint-Responsive/archive/{target_version}.zip"
			)
		)


__plugin_name__ = "OctoPrint-Responsive"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = ResponsivePlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}
