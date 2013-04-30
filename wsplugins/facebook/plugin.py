__author__ = 'apolikamixitos'


import wsplugins.facebook.libs.facebook as facebook
import wsplugins.facebook.configuration as settings

#The plugin class name MUST BE named "WS"
class WS:

    #You can declare the number of the pins (each var for a pin)
    NbrInbox=0
    NbrFriendRequests=0
    Nbrnotifications=0

    """
    This function look for any updates available from the Facebook account via the GraphAPI
    and updates the class vars with the number of each type
    """
    def FBCheck(self):
        req=''

        if settings.CHECK_INBOX==True:
            req += "inbox";

        if settings.CHECK_NOTIFICATIONS==True:
            req += ',' if req!=''  else ''
            req += "notifications"

        if settings.CHECK_FRIENDREQUESTS==True:
            req += ',' if req!=''  else ''
            req += "friendrequests.fields(unread)"

        dic = {'fields':req}
        graph = facebook.GraphAPI(settings.ACCESS_TOKEN)
        res = graph.get_object("me", **dic)

        self.ParseResults(res)

    """
    This method parse the returned JSON response and extract the required information and update them
    """
    def ParseResults(self,res):

        NbrFriendRequests=0
        Nbrnotifications=0
        NbrInbox=0

        if settings.CHECK_FRIENDREQUESTS==True:
            try:
                NbrFriendRequests=int(res['friendrequests']['summary']['unread_count'])
            except Exception:
                pass

        if settings.CHECK_NOTIFICATIONS==True:
            try:
                Nbrnotifications=int(res['notifications']['summary']['unseen_count'])
            except Exception:
                pass

        if settings.CHECK_INBOX==True:
            try:
                NbrInbox=int(res['inbox']['summary']['unseen_count'])
            except Exception:
                pass

        self.NbrFriendRequests=NbrFriendRequests
        self.Nbrnotifications=Nbrnotifications
        self.NbrInbox=NbrInbox



    # this method is required for all the plugins, it must be declared static.
    # returns the list of pins and the value attributed to them. {PINNUMBER:VALUEUSED}
    @staticmethod
    def GETPINS():
        FB = WS()
        FB.FBCheck()
        return {
            settings.PIN_FRIENDREQUESTS:FB.NbrFriendRequests,
            settings.PIN_NOTIFICATIONS:FB.Nbrnotifications,
            settings.PIN_INBOX:FB.NbrInbox
        }
