
class FavoriteList(list):
    """
    a FavoriteList is an associacion of a JobID and an energy, sorted by energy
    """
    
    def __init__(self):
            super(FavoriteList, self).__init__()
            