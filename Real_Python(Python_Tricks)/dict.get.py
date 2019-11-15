# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:24:15 2019

@author: Zac_Fang
"""
name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

greeting(382)
"Hi Alice!"
greeting(333333)

"Hi there!"
"""When "get()" is called it checks if the given key exists in the dict.
If it does exist, the value for that key is returned.
If it does not exist then the value of the default argument is returned instead.
— Dan Bader (realpython.com)
"""
