# Simple ryu application to demostrate ryu
# This example is provided by Ryu open source documentation.

# import app manager
from ryu.base import app_manager

# Create a Layer 2 switch
class L2Switch(app_manager.RyuApp):
    def __init__(self, *args, **kwargs):
        super(L2Switch, self).__init__(*args, **kwargs)