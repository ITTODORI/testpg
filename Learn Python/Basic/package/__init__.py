# fungsi init untuk cnofiguration rantai yang terputus 
# pada file package

from . import pack #fungsi '.' adalah local file yang ada pada import
from . import physics

# CUSTUMIZE IMPORT INIT
__all__ =[
    "pack",
    "physics"
]