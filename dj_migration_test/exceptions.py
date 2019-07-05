class AppNotFound(Exception):
    def __init__(self):
        super().__init__('App not found.')
