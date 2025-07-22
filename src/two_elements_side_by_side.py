# ## ####

import sys
# ## ####
class TwoElementsUI(Page):
    def __init__(self, title: str, body: Body, filename: str):
        super().__init__(self, title=title, body=body, filename=filename)
    # ## ####
# ## ####
class CreateElement:
    def __init__(self, bg_color: str, fg_color: str, width, height):
        if not bg_color or not fg_color or not width or not height:
            print('existing...')
            sys.exit()