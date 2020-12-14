""" Platzigram middleware catalog. """

class ProfileCompletionMiddleware:
    """ Profile completion middleware.
        Ensure every user that is interacting with the platform
        have their profile picture and biography
    """

    def __init__(self, get_response):
        """ Middleware initialization. """
        self.get_response = get_response