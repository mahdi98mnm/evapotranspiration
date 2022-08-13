"""
library of functions for testing  intrception bucket method
copyright:2022/5/6 by sakineh amiri

"""

from  main_interception_bucket import interception_bucket_method
"""
1- interception =30.33

"""
interception = interception_bucket_method( 'Forest & mixed' , 505.5 ,True )

"""
2- interception =15.165

"""
interception = interception_bucket_method( 'Forest & mixed' , 505.5 ,False )

"""
3- interception =50.55
"""
interception = interception_bucket_method( 'Evergreen forest' , 505.5 ,False )

"""
4- interception = 0

"""
interception = interception_bucket_method( 'desert' , 505.5 ,False )