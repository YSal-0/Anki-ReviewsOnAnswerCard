import aqt
from aqt.reviewer import Reviewer
from anki.scheduler.v3 import Scheduler as V3Scheduler
from aqt.utils import  tr

def showRonA (self) -> str:
        default = self._defaultEase()

        assert isinstance(self.mw.col.sched, V3Scheduler)
        labels = self.mw.col.sched.describe_next_states(self._v3.states)
        remain = self._remaining()

        def but(i: int, label: str) -> str:
            if i == default:
                extra = """id="defease" """
            else:
                extra = ""
            due = self._buttonTime(i, v3_labels=labels)
            key = (
                tr.actions_shortcut_key(val=aqt.mw.pm.get_answer_key(i))
                if aqt.mw.pm.get_answer_key(i)
                else ""
            )
            return """
<td align=center><button %s title="%s" data-ease="%s" onclick='pycmd("ease%d");'>\
%s%s</button></td>""" % (
                extra,
                key,
                i,
                i,
                label,
                due,
                )

        buf = "<center><table cellpadding=0 cellspacing=0><tr>"
        for ease, label in self._answerButtonList():
            buf += but(ease, label)
            button_count = self.mw.col.sched.answerButtons(self.card)
            listlength = button_count/2
            #listlength = 2
            if ease == listlength:
                buf += "<td align=center><button><span class=stattxt>%s</span></button></td>" % (remain)
        buf += "</tr></table>"
        return buf

Reviewer._answerButtons = showRonA