# Copyright © 2020, Joseph Berry, Rico Tabor (opendrop.dev@gmail.com)
# OpenDrop is released under the GNU GPL License. You are free to
# modify and distribute the code, but always under the same license
# (i.e. you cannot make commercial derivatives).
#
# If you use this software in your research, please cite the following
# journal articles:
#
# J. D. Berry, M. J. Neeson, R. R. Dagastine, D. Y. C. Chan and
# R. F. Tabor, Measurement of surface and interfacial tension using
# pendant drop tensiometry. Journal of Colloid and Interface Science 454
# (2015) 226–237. https://doi.org/10.1016/j.jcis.2015.05.012
#
#E. Huang, T. Denning, A. Skoufis, J. Qi, R. R. Dagastine, R. F. Tabor
#and J. D. Berry, OpenDrop: Open-source software for pendant drop
#tensiometry & contact angle measurements, submitted to the Journal of
# Open Source Software
#
#These citations help us not only to understand who is using and
#developing OpenDrop, and for what purpose, but also to justify
#continued development of this code and other open source resources.
#
# OpenDrop is distributed WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.  You
# should have received a copy of the GNU General Public License along
# with this software.  If not, see <https://www.gnu.org/licenses/>.
from gi.repository import Gtk

from opendrop.app.common.image_processing.image_processor import ImageProcessorPluginViewContext
from opendrop.app.common.image_processing.plugins.define_line import DefineLinePluginModel, define_line_plugin_cs
from opendrop.app.conan.image_processing.plugins import ToolID
from opendrop.mvp import ComponentSymbol, View, Presenter

conan_surface_plugin_cs = ComponentSymbol()  # type: ComponentSymbol[None]


@conan_surface_plugin_cs.view(options=['view_context', 'z_index'])
class ConanSurfacePluginView(View['ConanSurfacePluginPresenter', None]):
    def _do_init(self, view_context: ImageProcessorPluginViewContext, z_index: int) -> None:
        self._view_context = view_context

        self.new_component(
            define_line_plugin_cs.factory(
                model=self.presenter.define_line_plugin_model,
                view_context=view_context,
                tool_id=ToolID.SURFACE,
                color=(0.1, 0.8, 0.1),
                z_index=z_index,
            ),
        )

        tool_ref = view_context.get_tool_item(ToolID.SURFACE)
        self._tool_button_interior = Gtk.Grid(hexpand=True, vexpand=True)
        tool_ref.button_interior.add(self._tool_button_interior)

        tool_button_lbl = Gtk.Label(
            label='Surface line',
            vexpand=True,
            valign=Gtk.Align.CENTER,
        )
        self._tool_button_interior.add(tool_button_lbl)

        self._tool_button_interior.show_all()

    def _do_destroy(self) -> None:
        self._tool_button_interior.destroy()


@conan_surface_plugin_cs.presenter(options=['model'])
class ConanSurfacePluginPresenter(Presenter['ConanSurfacePluginView']):
    def _do_init(self, model: DefineLinePluginModel) -> None:
        self.define_line_plugin_model = model
