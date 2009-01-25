#-------------------------------------------------------------------------------
#  
#  ArrayEditor test case  
#  
#  Written by: David C. Morrill
#  
#  Date: 01/10/2006
#  
#  (c) Copyright 2006 by Enthought, Inc.
#  License: BSD Style.
#  
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#  Imports:  
#-------------------------------------------------------------------------------

from enthought.traits.api \
    import HasPrivateTraits, Array
    
from enthought.traits.ui.api \
    import View, ArrayEditor
    
#-------------------------------------------------------------------------------
#  'Test' class:
#-------------------------------------------------------------------------------

class Test ( HasPrivateTraits ):
    
    #---------------------------------------------------------------------------
    #  Trait definitions:  
    #---------------------------------------------------------------------------
        
    three = Array( int, (3,3) )
    four  = Array( float, (4,4), editor = ArrayEditor( width = -50 ) )
    
    #---------------------------------------------------------------------------
    #  Traits view definitions:  
    #---------------------------------------------------------------------------
        
    view = View( 'three', '_', 'three', '_', 'three~', '_', 
                 'four',  '_', 'four',  '_', 'four~',
                 title     = 'ArrayEditor Test Case',
                 resizable = True )
                 
#-------------------------------------------------------------------------------
#  Run the test case:  
#-------------------------------------------------------------------------------
                     
if __name__ == '__main__':
    Test().configure_traits()
