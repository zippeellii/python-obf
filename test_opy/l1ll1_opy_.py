# coding: UTF-8
import sys
l1_opy_ = sys.version_info [0] == 2
l1ll_opy_ = 2048
l1111_opy_ = 7
def l1l11_opy_ (ll_opy_):
    global l11l_opy_
    l11_opy_ = ord (ll_opy_ [-1])
    l11l1_opy_ = ll_opy_ [:-1]
    l111_opy_ = l11_opy_ % len (l11l1_opy_)
    l1lll_opy_ = l11l1_opy_ [:l111_opy_] + l11l1_opy_ [l111_opy_:]
    if l1_opy_:
        l111l_opy_ = unicode () .join ([unichr (ord (char) - l1ll_opy_ - (l1l1_opy_ + l11_opy_) % l1111_opy_) for l1l1_opy_, char in enumerate (l1lll_opy_)])
    else:
        l111l_opy_ = str () .join ([chr (ord (char) - l1ll_opy_ - (l1l1_opy_ + l11_opy_) % l1111_opy_) for l1l1_opy_, char in enumerate (l1lll_opy_)])
    return eval (l111l_opy_)
def l11ll_opy_(l1l_opy_):
    return reduce(lambda x, y: x + y, l1l_opy_)
l1l1l_opy_ = [1,2,3,4,5]
sum = l11ll_opy_([1,2,3,4])
print l1l11_opy_ (u"࡙ࠫ࡮ࡥࠡࡵࡸࡱࠥࡵࡦࠡࡧ࡯ࡩࡲ࡫࡮ࡵࡵࠣ࡭ࡳࠦ࡬ࡪࡵࡷࠤ࡮ࡹࠧࠀ"), sum
print l1l11_opy_ (u"࡚ࠬࡨࡦࠢࡵࡩࡻ࡫ࡲࡴࡧࡧࠤࡴࡸࡤࡦࡴࠣࡳ࡫ࠦࡥ࡭ࡧࡰࡩࡳࡺࡳࠡ࡫ࡱࠤࡱ࡯ࡳࡵࠢ࡬ࡷࠬࠁ"), l1l1l_opy_[::-1]