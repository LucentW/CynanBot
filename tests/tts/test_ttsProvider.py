from src.tts.ttsProvider import TtsProvider


class TestTtsProvider:

    def test_allTtsProvidersHaveHumanName(self):
        results: set[str] = set()

        for ttsProvider in TtsProvider:
            results.add(ttsProvider.humanName)

        assert len(results) == len(TtsProvider)

    def test_humanName_withDecTalk(self):
        result = TtsProvider.DEC_TALK.humanName
        assert result == 'DECtalk'

    def test_humanName_withGoogle(self):
        result = TtsProvider.GOOGLE.humanName
        assert result == 'Google'

    def test_humanName_withHalfLife(self):
        result = TtsProvider.HALF_LIFE.humanName
        assert result == 'Half-Life'

    def test_humanName_withMicrosoftSam(self):
        result = TtsProvider.MICROSOFT_SAM.humanName
        assert result == 'Microsoft Sam'

    def test_humanName_withSingingDecTalk(self):
        result = TtsProvider.SINGING_DEC_TALK.humanName
        assert result == 'Singing DECtalk'

    def test_humanName_withStreamElements(self):
        result = TtsProvider.STREAM_ELEMENTS.humanName
        assert result == 'Stream Elements'

    def test_humanName_withTtsMonster(self):
        result = TtsProvider.TTS_MONSTER.humanName
        assert result == 'TTS Monster'
