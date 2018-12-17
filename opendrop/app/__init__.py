import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

from opendrop.app.app import App
from opendrop.app.dependencies.default_gui_factory import DefaultAppGUIFactory
from opendrop.app.dependencies.default_speaker_factory import DefaultAppSpeakersFactory

from opendrop.vendor.glibcoro import glibcoro


def main():
    glibcoro.install()
    default_app_speakers_factory = DefaultAppSpeakersFactory()
    app = App(DefaultAppGUIFactory(), default_app_speakers_factory)
    app.run()


if __name__ == '__main__':
    main()
