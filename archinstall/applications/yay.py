from typing import TYPE_CHECKING

from archinstall.lib.log import debug

if TYPE_CHECKING:
	from archinstall.lib.installer import Installer


class YayApp:
	def install(self, install_session: Installer) -> None:
		debug('Installing yay')
		install_session.install_aur_package('yay')
