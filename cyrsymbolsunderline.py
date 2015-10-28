import sublime, sublime_plugin

class CyrSymbolsUnderlineCommand(sublime_plugin.EventListener):

    def on_load_async(self, view):
    	self.underline_cyr_symbols(view)

    def on_modified_async(self, view):
        self.underline_cyr_symbols(view)

    def find_regions(self, view):
        regions = []
        regions += view.find_all(u'[\u0400-\u0500]+')
        return regions

    def underline_cyr_symbols(self, view):
        regions = self.find_regions(view)
        view.add_regions('cyrsymbols', regions, 'comment', "", sublime.DRAW_NO_FILL|sublime.DRAW_NO_OUTLINE|sublime.DRAW_SOLID_UNDERLINE)
