# ## ####
class CoconutTree:
    def __init__(self, color: str = 'green'):
        self.tree_color = color;
    def get_tree_image(self):
        return self.tree_image
    def set_tree_image(self, tree_image: Path = Path("/assets/tree_image.png")):
        self.tree_image = tree_image
    def run(self):
        # ## ###
        if not self.tree_image:
            return f' '
        return self.tree_image.show()
# ## ####
if __init__=="__main__":
    coconut_tree = CoconutTree()