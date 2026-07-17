from bp2md.repair import BanglaRepair


def test_bangla_repair():

    repair = BanglaRepair()

    assert repair.repair("।।") == "।"
    assert repair.repair("াি") != "াি"