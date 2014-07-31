import autoposter


class TestApp(object):
    def test_it_can_be_instantiated(self):
        app = autoposter.App()

        assert isinstance(app, autoposter.App)
