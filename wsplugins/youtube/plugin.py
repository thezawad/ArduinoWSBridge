__author__ = 'apolikamixitos'

import wsplugins.youtube.configuration as settings
import requests

#The plugin class name MUST BE named "WS"
class WS:

    #You can declare the number of the pins (each var for a pin)
    _views=-1
    _likes=-1
    _dislikes=-1
    _favorites=-1
    _comments=-1

    """
    This function look for any updates available from the Facebook account via the GraphAPI
    and updates the class vars with the number of each type
    """
    def YTCheck(self):
        res = requests.get('https://gdata.youtube.com/feeds/api/videos/{}?v=2&alt=json'.format(settings.YT_VIDEO_ID)).json()
        self.ParseResults(res)

    """
    This method parse the returned JSON response and extract the required information and update them
    """
    def ParseResults(self,res):

        self._views = int(res['entry']['yt$statistics']['viewCount'])
        self._likes = int(res['entry']['yt$rating']['numLikes'])
        self._dislikes = int(res['entry']['yt$rating']['numDislikes'])
        self._favorites = int(res['entry']['yt$statistics']['favoriteCount'])
        self._comments = int(res['entry']['gd$comments']['gd$feedLink']['countHint'])

        #print 'Views {}, Likes {}, Dislikes {}, Favs {}, Comments {}'.format(self.views,self.likes,self.dislikes,self.favorites,self.comments)

    #You define the methods that are going to be used to send the data to a specific PIN
    def views(self):
        return self.views

    def likes(self):
        return self.likes

    def dislikes(self):
        return self.dislikes

    def favorites(self):
        return self.favorites

    def comments(self):
        return self.comments

    # this method is required for all the plugins, it must be declared static.
    # returns the instance of the class
    @staticmethod
    def update_values():
        YT = WS()
        YT.YTCheck()
        return YT

