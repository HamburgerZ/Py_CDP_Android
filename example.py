import pychrome
from common.android import Android

if __name__ == "__main__":
    android1 = Android()
    socketName = ""
    for i in android1.socketNames:
        android1.forward(i)
        browser = pychrome.Browser(url="http://127.0.0.1:{0}".format(str(android1.remoteDebuggingPort)))
        for j in browser.list_tab():
            if j._kwargs["url"].find("baidu") != -1:
                socketName = i
                break
        android1.remove_forward(i)
    if socketName:
        android1.forward(socketName)
        browser = pychrome.Browser(url="http://127.0.0.1:{0}".format(str(android1.remoteDebuggingPort)))
        print(browser.list_tab()[0]._kwargs)
        tab = browser.list_tab()[0]
        '''
        you can add code to operate the dom of tab.
            usage like:
                    # start tab
                    tab.start()
                    # call method
                    tab.Network.enable()
                    # close tab
                    tab.stop()
        '''
        android1.remove_forward(socketName)
    else:
        print('Not expected socketName!')

