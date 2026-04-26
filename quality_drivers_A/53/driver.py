# Driver stub: 真实驱动类在同目录 de5000.py 中，这里 re-export 以便 unilabos 发现
from .de5000 import DE5000

__all__ = ['DE5000']
