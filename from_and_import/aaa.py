import bbb
from bbb import H


H = 'the value was changed!'

bbb.a()

bbb.H = 'the value was changed without the from keyword'

bbb.a()


