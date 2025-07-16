# popeye dot py


## ## 👾👾👾👾

# ## ###### import home
#from src import home
#from src.about import page as about
#from src.contact import page as contact
#from src.popeye import page as popeye
#from src.a404 import page as a404
#from src.blackNwhite import  page as blackNwhite
#from src import cars
from src import popeye
# ## ######
body = f"""
    <div id="popeye"></div>
"""

# ## ######

# ## ######
HOME = popeye.popeye
# ## ######
if __name__=="__main__":
    """create a list of pages"""
    pages = [HOME]
    """loop over each page and write them"""
    for page in pages:
        """page logo defaults to None. Change path argument to update/replace"""
        if not page.logo:
            page.logo = Path('assets/logo.png') if page.title == "Home" else Path('../assets/logo.png')
        """write page"""
        page.body = body
        page.write()

#EoF

